#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tkinter Endless Runner: Dino Game (Single File, 800+ lines)

Features
========
- Pure Tkinter Canvas rendering (no external assets required)
- Player with run, jump, and duck states (animation simulated by simple shapes)
- Obstacles: Cactus (ground), Bird (three flight levels) with animated wings
- Collectibles: Coins (score bonus) with subtle spin animation
- Power-ups: Shield (one-hit protection), SlowMo (brief slow motion)
- Particles: Dust, landing poofs, collision sparks
- Clouds and parallax ground for depth
- Day/Night cycle with sky tint and stars
- Scoring, high-score persistence (local file), and difficulty scaling
- Pause/Resume, Game Over, Restart, and Settings overlay
- Keyboard Controls: 
    * Space/Up = Jump, Down = Duck
    * P = Pause, R = Restart, M = Mute SFX (synthetic beeps)
    * 1/2/3 = Difficulty presets, C = Toggle color mode
    * F1 = Show/Hide Debug HUD
- Modular architecture, readable methods, and plenty of comments

Notes
=====
- The game avoids external images/sounds; everything is drawn with Canvas shapes.
- Sound effects are optional (simple `winsound.Beep` on Windows; noop on others).
- The code aims for clarity and breadth; performance is good for typical laptop screens.

Run
===
python dino_runner.py

"""
from __future__ import annotations
import sys
import os
import math
import time
import random
import json
import platform
from dataclasses import dataclass, field
from typing import List, Tuple, Optional, Callable, Dict

try:
    import tkinter as tk
    from tkinter import ttk
except Exception as e:  # pragma: no cover
    raise

# Optional simple beep on Windows
WINDOWS = platform.system().lower().startswith('win')
if WINDOWS:
    try:
        import winsound
    except Exception:  # pragma: no cover
        winsound = None
else:
    winsound = None

# ------------------------------ Utility ------------------------------------ #

def clamp(v: float, lo: float, hi: float) -> float:
    return max(lo, min(hi, v))


def lerp(a: float, b: float, t: float) -> float:
    return a + (b - a) * t


def now_ms() -> int:
    return int(time.time() * 1000)


def beep(freq: int = 440, dur: int = 80):
    if winsound is not None:
        try:
            winsound.Beep(freq, dur)
        except Exception:
            pass

# ------------------------------ Constants ---------------------------------- #

W = 900
H = 300
GROUND_Y = 240
FPS = 60
DT_MS = int(1000 / FPS)
GRAVITY = 0.75
JUMP_VELOCITY = -12.5
DUCK_HEIGHT = 26
RUN_HEIGHT = 40
PLAYER_X = 120

# Colors; day/night themes switch by blending sky
DAY_SKY = '#c8e9ff'
NIGHT_SKY = '#031935'
GROUND_COLOR = '#7a5f35'
GROUND_DARK = '#4e4129'
CLOUD_COLOR = '#ffffff'
PLAYER_COLOR = '#2b9348'
PLAYER_ACCENT = '#55a630'
CACTUS_COLOR = '#228B22'
BIRD_COLOR = '#333333'
COIN_COLOR = '#f4c542'
SHIELD_COLOR = '#3b82f6'
SLOWMO_COLOR = '#a78bfa'
TEXT_COLOR = '#111111'
TEXT_INV = '#f7f7f7'
STAR_COLOR = '#cddbff'

# Difficulty presets (base speed, spawn rates)
DIFF_PRESETS = {
    1: dict(base_speed=6.0, obs_min=900, obs_max=1400, coin_min=900, coin_max=1400),
    2: dict(base_speed=7.5, obs_min=700, obs_max=1200, coin_min=900, coin_max=1400),
    3: dict(base_speed=9.0, obs_min=600, obs_max=1000, coin_min=700, coin_max=1200),
}

# High-score file
HS_FILE = os.path.join(os.path.dirname(__file__), 'dino_highscore.json')

# ------------------------------ Data Classes -------------------------------- #

@dataclass
class Timer:
    duration: int
    start_ms: int = field(default_factory=now_ms)

    def reset(self, duration: Optional[int] = None):
        if duration is not None:
            self.duration = duration
        self.start_ms = now_ms()

    def done(self) -> bool:
        return now_ms() - self.start_ms >= self.duration

    def progress(self) -> float:
        return clamp((now_ms() - self.start_ms) / max(1, self.duration), 0.0, 1.0)


@dataclass
class Rect:
    x: float
    y: float
    w: float
    h: float

    def bbox(self) -> Tuple[float, float, float, float]:
        return (self.x, self.y, self.x + self.w, self.y + self.h)

    def intersects(self, other: 'Rect') -> bool:
        ax1, ay1, ax2, ay2 = self.bbox()
        bx1, by1, bx2, by2 = other.bbox()
        return (ax1 < bx2 and ax2 > bx1 and ay1 < by2 and ay2 > by1)

    def inset(self, dx: float, dy: float) -> 'Rect':
        return Rect(self.x + dx, self.y + dy, max(0, self.w - 2*dx), max(0, self.h - 2*dy))

# ------------------------------ Entities ------------------------------------ #

class Entity:
    def __init__(self, game: 'Game'):
        self.g = game
        self.dead = False

    def update(self, dt: float):
        pass

    def draw(self):
        pass


class Particle(Entity):
    def __init__(self, game: 'Game', x: float, y: float, vx: float, vy: float, life: int, size: int, color: str, gravity: float = 0.0):
        super().__init__(game)
        self.x, self.y = x, y
        self.vx, self.vy = vx, vy
        self.life = Timer(life)
        self.size = size
        self.color = color
        self.gravity = gravity
        self.alpha = 1.0

    def update(self, dt: float):
        self.vy += self.gravity
        self.x += self.vx
        self.y += self.vy
        t = self.life.progress()
        self.alpha = 1.0 - t
        if self.life.done():
            self.dead = True

    def draw(self):
        s = self.size * (0.5 + 0.5 * self.alpha)
        x1, y1, x2, y2 = self.x - s, self.y - s, self.x + s, self.y + s
        fill = self._fade(self.color, self.alpha)
        self.g.c.create_oval(x1, y1, x2, y2, fill=fill, outline='')

    @staticmethod
    def _fade(hex_color: str, alpha: float) -> str:
        # blend with sky to fade
        r, g, b = hex_to_rgb(hex_color)
        sr, sg, sb = hex_to_rgb(DAY_SKY)
        r = int(lerp(sr, r, alpha))
        g = int(lerp(sg, g, alpha))
        b = int(lerp(sb, b, alpha))
        return rgb_to_hex(r, g, b)


class Cloud(Entity):
    def __init__(self, game: 'Game'):
        super().__init__(game)
        self.y = random.randint(20, 120)
        self.x = W + random.randint(0, 200)
        self.speed = random.uniform(0.8, 1.5)
        self.scale = random.uniform(0.7, 1.4)

    def update(self, dt: float):
        self.x -= self.speed
        if self.x < -120:
            self.dead = True

    def draw(self):
        s = 20 * self.scale
        c = CLOUD_COLOR
        self.g.c.create_oval(self.x, self.y, self.x + 3*s, self.y + 2*s, fill=c, outline='')
        self.g.c.create_oval(self.x + 2*s, self.y - 0.5*s, self.x + 4*s, self.y + 1.5*s, fill=c, outline='')
        self.g.c.create_oval(self.x - s, self.y + 0.3*s, self.x + s, self.y + 2.2*s, fill=c, outline='')


class GroundSeg(Entity):
    def __init__(self, game: 'Game', x: float, width: float, speed_ref: Callable[[], float]):
        super().__init__(game)
        self.x = x
        self.y = GROUND_Y
        self.w = width
        self.h = 6
        self.speed_ref = speed_ref

    def update(self, dt: float):
        self.x -= self.speed_ref()
        if self.x + self.w < 0:
            self.dead = True

    def draw(self):
        y = self.y
        self.g.c.create_rectangle(self.x, y, self.x + self.w, y + self.h, fill=GROUND_COLOR, outline='')
        # little bumps
        for i in range(5):
            bx = self.x + (i + 0.5) * self.w / 5
            bw = self.w / 8
            self.g.c.create_rectangle(bx, y + 3, bx + bw, y + self.h, fill=GROUND_DARK, outline='')


class Obstacle(Entity):
    def rect(self) -> Rect:
        raise NotImplementedError


class Cactus(Obstacle):
    def __init__(self, game: 'Game', speed_ref: Callable[[], float]):
        super().__init__(game)
        self.x = W + 20
        self.y = GROUND_Y - 35
        self.w = random.choice([20, 26, 32])
        self.h = random.choice([32, 38, 44])
        self.speed_ref = speed_ref
        self.tilt = random.choice([-1, 0, 1])

    def update(self, dt: float):
        self.x -= self.speed_ref()
        if self.x + self.w < 0:
            self.dead = True

    def draw(self):
        x1, y1 = self.x, self.y + (44 - self.h)
        x2, y2 = self.x + self.w, self.y + self.h
        self.g.c.create_rectangle(x1, y1, x2, y2, fill=CACTUS_COLOR, outline='')
        # arms
        arm_h = self.h * 0.35
        if self.w >= 26:
            self.g.c.create_rectangle(x1 - 6, y1 + 10, x1 + 2, y1 + 10 + arm_h, fill=CACTUS_COLOR, outline='')
        if self.w >= 32:
            self.g.c.create_rectangle(x2 - 2, y1 + 6, x2 + 6, y1 + 6 + arm_h, fill=CACTUS_COLOR, outline='')

    def rect(self) -> Rect:
        return Rect(self.x, self.y + (44 - self.h), self.w, self.h)


class Bird(Obstacle):
    def __init__(self, game: 'Game', speed_ref: Callable[[], float]):
        super().__init__(game)
        self.x = W + 20
        self.alt = random.choice([GROUND_Y - 60, GROUND_Y - 90, GROUND_Y - 120])
        self.y = self.alt
        self.w = 38
        self.h = 24
        self.flap_t = 0.0
        self.speed_ref = speed_ref

    def update(self, dt: float):
        self.x -= self.speed_ref() * 1.15
        self.flap_t += 0.2
        if self.x + self.w < 0:
            self.dead = True

    def draw(self):
        body = (self.x, self.y, self.x + self.w, self.y + self.h)
        self.g.c.create_oval(*body, fill=BIRD_COLOR, outline='')
        # wings
        wing_phase = math.sin(self.flap_t)
        spread = 10 + 8 * wing_phase
        self.g.c.create_polygon(self.x + 10, self.y + 12,
                                self.x - spread, self.y + 2,
                                self.x - spread, self.y + 22,
                                fill=BIRD_COLOR, outline='')

    def rect(self) -> Rect:
        return Rect(self.x + 4, self.y + 2, self.w - 8, self.h - 4)


class Coin(Entity):
    def __init__(self, game: 'Game', speed_ref: Callable[[], float]):
        super().__init__(game)
        self.x = W + 20
        self.y = random.choice([GROUND_Y - 40, GROUND_Y - 80, GROUND_Y - 120])
        self.r = 9
        self.spin = 0.0
        self.speed_ref = speed_ref
        self.taken = False

    def update(self, dt: float):
        self.x -= self.speed_ref()
        self.spin += 0.25
        if self.x + self.r < 0:
            self.dead = True
        if not self.taken and self.g.player.rect().intersects(self.rect()):
            self.collect()

    def rect(self) -> Rect:
        return Rect(self.x - self.r, self.y - self.r, 2*self.r, 2*self.r)

    def collect(self):
        self.taken = True
        self.dead = True
        self.g.score += 25
        self.g.emit_spark(self.x, self.y)
        self.g.sfx_coin()

    def draw(self):
        # simulate spin by changing width
        phase = (math.sin(self.spin) + 1) / 2  # 0..1
        rx = lerp(self.r * 0.4, self.r, phase)
        ry = self.r
        self.g.c.create_oval(self.x - rx, self.y - ry, self.x + rx, self.y + ry, fill=COIN_COLOR, outline='#d4a52f', width=2)
        self.g.c.create_oval(self.x - rx*0.5, self.y - ry*0.5, self.x + rx*0.5, self.y + ry*0.5, outline='#d4a52f')


class PowerUp(Entity):
    kind: str

    def rect(self) -> Rect:
        raise NotImplementedError


class ShieldPU(PowerUp):
    def __init__(self, game: 'Game', speed_ref: Callable[[], float]):
        super().__init__(game)
        self.kind = 'shield'
        self.x = W + 20
        self.y = GROUND_Y - 90
        self.r = 10
        self.speed_ref = speed_ref
        self.pulse = 0.0

    def update(self, dt: float):
        self.x -= self.speed_ref()
        self.pulse += 0.2
        if self.x + self.r < 0:
            self.dead = True
        if self.g.player.rect().intersects(self.rect()):
            self.g.player.gain_shield()
            self.g.emit_spark(self.x, self.y, color=SHIELD_COLOR)
            self.g.sfx_power()
            self.dead = True

    def rect(self) -> Rect:
        return Rect(self.x - self.r, self.y - self.r, 2*self.r, 2*self.r)

    def draw(self):
        p = (math.sin(self.pulse) + 1) / 2
        rr = lerp(self.r, self.r * 1.5, p)
        self.g.c.create_oval(self.x - rr, self.y - rr, self.x + rr, self.y + rr, outline=SHIELD_COLOR, width=2)
        self.g.c.create_arc(self.x - rr, self.y - rr, self.x + rr, self.y + rr, start=200, extent=140, style=tk.ARC, outline=SHIELD_COLOR, width=3)


class SlowMoPU(PowerUp):
    def __init__(self, game: 'Game', speed_ref: Callable[[], float]):
        super().__init__(game)
        self.kind = 'slowmo'
        self.x = W + 20
        self.y = GROUND_Y - 130
        self.r = 10
        self.speed_ref = speed_ref
        self.t = 0.0

    def update(self, dt: float):
        self.x -= self.speed_ref()
        self.t += 0.25
        if self.x + self.r < 0:
            self.dead = True
        if self.g.player.rect().intersects(self.rect()):
            self.g.activate_slowmo()
            self.g.emit_spark(self.x, self.y, color=SLOWMO_COLOR)
            self.g.sfx_power()
            self.dead = True

    def rect(self) -> Rect:
        return Rect(self.x - self.r, self.y - self.r, 2*self.r, 2*self.r)

    def draw(self):
        # hourglass symbol
        r = self.r
        x, y = self.x, self.y
        self.g.c.create_polygon(x - r, y - r, x + r, y - r, x - r/2, y, fill='', outline=SLOWMO_COLOR)
        self.g.c.create_polygon(x - r, y + r, x + r, y + r, x + r/2, y, fill='', outline=SLOWMO_COLOR)
        self.g.c.create_line(x - r, y - r, x + r, y - r, fill=SLOWMO_COLOR)
        self.g.c.create_line(x - r, y + r, x + r, y + r, fill=SLOWMO_COLOR)


class Player(Entity):
    def __init__(self, game: 'Game'):
        super().__init__(game)
        self.x = PLAYER_X
        self.y = GROUND_Y - RUN_HEIGHT
        self.vy = 0.0
        self.on_ground = True
        self.ducking = False
        self.anim_t = 0.0
        self.shield = False
        self.inv_timer: Optional[Timer] = None

    def rect(self) -> Rect:
        h = DUCK_HEIGHT if self.ducking and self.on_ground else RUN_HEIGHT
        return Rect(self.x - 14, self.y, 28, h)

    def gain_shield(self):
        self.shield = True
        self.g.emit_shield_burst(self.x, self.y + 10)

    def hit(self):
        if self.shield:
            self.shield = False
            self.g.emit_spark(self.x + 10, self.y + 10)
            self.inv_timer = Timer(600)
            self.g.sfx_shield_break()
            return False  # not dead
        return True  # dead

    def update(self, dt: float):
        self.anim_t += 0.25

        # apply gravity
        self.vy += GRAVITY * self.g.speed_scale
        self.y += self.vy

        # ground collision
        ground = GROUND_Y - (DUCK_HEIGHT if self.ducking else RUN_HEIGHT)
        if self.y >= ground:
            if not self.on_ground and self.vy > 1.5:
                self.g.emit_land_dust(self.x, GROUND_Y)
                self.g.sfx_land()
            self.y = ground
            self.vy = 0
            self.on_ground = True
        else:
            self.on_ground = False

        # end of invulnerability after shield hit
        if self.inv_timer and self.inv_timer.done():
            self.inv_timer = None

    def jump(self):
        if self.on_ground:
            self.vy = JUMP_VELOCITY * (0.88 if self.ducking else 1.0)
            self.on_ground = False
            self.g.emit_jump_dust(self.x, GROUND_Y)
            self.g.sfx_jump()

    def set_duck(self, down: bool):
        self.ducking = down and self.on_ground
        if self.ducking:
            self.y = GROUND_Y - DUCK_HEIGHT
        elif self.on_ground:
            self.y = GROUND_Y - RUN_HEIGHT

    def draw(self):
        inv = self.inv_timer is not None and (now_ms() // 80) % 2 == 0
        color = PLAYER_ACCENT if inv else PLAYER_COLOR
        # body
        r = self.rect()
        self.g.c.create_rectangle(r.x, r.y, r.x + r.w, r.y + r.h, fill=color, outline='')
        # legs animation (simple two-frame)
        if self.on_ground and not self.ducking:
            phase = int(self.anim_t) % 2
            lx = r.x + 4
            rx = r.x + r.w - 4
            y = r.y + r.h
            if phase == 0:
                self.g.c.create_line(lx, y, lx - 6, y + 10, width=3)
                self.g.c.create_line(rx, y, rx + 6, y + 10, width=3)
            else:
                self.g.c.create_line(lx, y, lx + 6, y + 10, width=3)
                self.g.c.create_line(rx, y, rx - 6, y + 10, width=3)
        # head
        head_r = 9 if not self.ducking else 7
        self.g.c.create_oval(r.x + r.w - 10 - head_r, r.y - head_r,
                             r.x + r.w - 10 + head_r, r.y + head_r, fill=color, outline='')
        # eye
        self.g.c.create_oval(r.x + r.w - 8, r.y - 3, r.x + r.w - 5, r.y, fill='#111', outline='')
        # shield aura
        if self.shield:
            self.g.c.create_oval(r.x - 6, r.y - 8, r.x + r.w + 6, r.y + r.h + 6, outline=SHIELD_COLOR, width=2)


# ------------------------------ Game Class ---------------------------------- #

class Game:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title('Tkinter Dino Runner')
        self.root.geometry(f'{W}x{H}')
        self.root.resizable(False, False)

        self.c = tk.Canvas(root, width=W, height=H, bg=DAY_SKY, highlightthickness=0)
        self.c.pack(fill='both', expand=True)

        # State
        self.running = True
        self.paused = False
        self.game_over = False
        self.muted = False
        self.debug = False
        self.color_mode = 0  # 0 normal, 1 high-contrast

        # Difficulty
        self.diff = 2
        self.base_speed = DIFF_PRESETS[self.diff]['base_speed']
        self.speed = self.base_speed
        self.speed_scale = 1.0
        self.distance = 0.0

        # Day/Night
        self.time_t = 0.0
        self.sky = DAY_SKY
        self.stars = [(random.randint(0, W), random.randint(0, H//2)) for _ in range(40)]

        # Entities
        self.player = Player(self)
        self.entities: List[Entity] = []
        self.obstacles: List[Obstacle] = []
        self.collectibles: List[Entity] = []
        self.powerups: List[PowerUp] = []
        self.ground: List[GroundSeg] = []
        self.spawn_ground()
        self.clouds: List[Cloud] = [Cloud(self) for _ in range(3)]
        self.particles: List[Particle] = []

        # Score
        self.score = 0
        self.high = self.load_high()
        self.combo = 0

        # Timers
        self.next_obstacle = Timer(self.rng_obs_interval())
        self.next_coin = Timer(self.rng_coin_interval())
        self.next_power = Timer(random.randint(9000, 14000))
        self.slowmo_timer: Optional[Timer] = None

        # UI
        self.banner_timer: Optional[Timer] = Timer(2500)

        # Bindings
        self.root.bind('<KeyPress>', self.on_key)
        self.root.bind('<KeyRelease>', self.on_key_up)

        # Main loop
        self.last_ms = now_ms()
        self.loop()

    # ------------------------- Persistence ---------------------------------- #
    def load_high(self) -> int:
        try:
            if os.path.exists(HS_FILE):
                with open(HS_FILE, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                return int(data.get('high', 0))
        except Exception:
            pass
        return 0

    def save_high(self):
        try:
            with open(HS_FILE, 'w', encoding='utf-8') as f:
                json.dump({'high': int(self.high)}, f)
        except Exception:
            pass

    # ------------------------- Spawning ------------------------------------- #
    def spawn_ground(self):
        self.ground.clear()
        seg_w = 180
        for i in range((W // seg_w) + 3):
            x = i * seg_w
            self.ground.append(GroundSeg(self, x=x, width=seg_w, speed_ref=self.get_speed))

    def rng_obs_interval(self) -> int:
        d = DIFF_PRESETS[self.diff]
        return random.randint(d['obs_min'], d['obs_max'])

    def rng_coin_interval(self) -> int:
        d = DIFF_PRESETS[self.diff]
        return random.randint(d['coin_min'], d['coin_max'])

    def get_speed(self) -> float:
        s = self.speed * (0.5 if self.slowmo_timer and not self.slowmo_timer.done() else 1.0)
        return s

    def maybe_spawn(self):
        if self.next_obstacle.done():
            kind = random.choice(['cactus'] * 3 + ['bird'])
            if kind == 'cactus':
                self.obstacles.append(Cactus(self, self.get_speed))
            else:
                self.obstacles.append(Bird(self, self.get_speed))
            self.next_obstacle.reset(self.rng_obs_interval())

        if self.next_coin.done():
            self.collectibles.append(Coin(self, self.get_speed))
            self.next_coin.reset(self.rng_coin_interval())

        if self.next_power.done():
            if random.random() < 0.5:
                self.powerups.append(ShieldPU(self, self.get_speed))
            else:
                self.powerups.append(SlowMoPU(self, self.get_speed))
            self.next_power.reset(random.randint(12000, 18000))

        # Clouds occasionally
        if random.random() < 0.015:
            self.clouds.append(Cloud(self))

        # Ground recycling
        if len(self.ground) == 0 or (self.ground and self.ground[-1].x + self.ground[-1].w < W):
            last_x = self.ground[-1].x + self.ground[-1].w if self.ground else 0
            self.ground.append(GroundSeg(self, x=last_x, width=180, speed_ref=self.get_speed))

    # ------------------------- Effects -------------------------------------- #
    def emit_jump_dust(self, x: float, y: float):
        for _ in range(6):
            ang = random.uniform(-math.pi, 0)
            sp = random.uniform(1, 3)
            vx = math.cos(ang) * sp
            vy = math.sin(ang) * sp
            self.particles.append(Particle(self, x, y, vx, vy, life=random.randint(250, 450), size=random.randint(2, 3), color=GROUND_DARK))

    def emit_land_dust(self, x: float, y: float):
        for _ in range(10):
            ang = random.uniform(math.pi, 2*math.pi)
            sp = random.uniform(0.5, 2.2)
            vx = math.cos(ang) * sp
            vy = math.sin(ang) * sp
            self.particles.append(Particle(self, x, y, vx, vy, life=random.randint(280, 520), size=random.randint(2, 4), color=GROUND_COLOR))

    def emit_spark(self, x: float, y: float, color: str = COIN_COLOR):
        for _ in range(12):
            ang = random.uniform(0, 2*math.pi)
            sp = random.uniform(1.2, 3.8)
            vx = math.cos(ang) * sp
            vy = math.sin(ang) * sp
            self.particles.append(Particle(self, x, y, vx, vy, life=random.randint(300, 600), size=random.randint(2, 3), color=color))

    def emit_shield_burst(self, x: float, y: float):
        for _ in range(16):
            ang = random.uniform(0, 2*math.pi)
            sp = random.uniform(1.0, 2.6)
            vx = math.cos(ang) * sp
            vy = math.sin(ang) * sp
            self.particles.append(Particle(self, x, y, vx, vy, life=random.randint(500, 800), size=random.randint(2, 3), color=SHIELD_COLOR))

    # ------------------------- Audio ---------------------------------------- #
    def sfx_jump(self):
        if not self.muted:
            beep(660, 60)

    def sfx_land(self):
        if not self.muted:
            beep(330, 40)

    def sfx_coin(self):
        if not self.muted:
            beep(880, 50)

    def sfx_power(self):
        if not self.muted:
            beep(520, 60)

    def sfx_shield_break(self):
        if not self.muted:
            beep(200, 120)

    def sfx_hit(self):
        if not self.muted:
            beep(150, 180)

    # ------------------------- Input ---------------------------------------- #
    def on_key(self, e):
        if e.keysym in ('space', 'Up'):
            if self.game_over:
                self.restart()
            else:
                self.player.jump()
        elif e.keysym == 'Down':
            self.player.set_duck(True)
        elif e.keysym.lower() == 'p':
            if not self.game_over:
                self.paused = not self.paused
        elif e.keysym.lower() == 'r':
            self.restart()
        elif e.keysym.lower() == 'm':
            self.muted = not self.muted
        elif e.keysym == 'F1':
            self.debug = not self.debug
        elif e.keysym.lower() == 'c':
            self.color_mode = (self.color_mode + 1) % 2
        elif e.keysym in ('1', '2', '3'):
            self.set_difficulty(int(e.keysym))

    def on_key_up(self, e):
        if e.keysym == 'Down':
            self.player.set_duck(False)

    # ------------------------- Difficulty ----------------------------------- #
    def set_difficulty(self, level: int):
        self.diff = clamp(level, 1, 3)
        d = DIFF_PRESETS[self.diff]
        self.base_speed = d['base_speed']
        self.speed = self.base_speed
        self.next_obstacle.reset(self.rng_obs_interval())
        self.next_coin.reset(self.rng_coin_interval())
        self.banner_timer = Timer(1500)

    # ------------------------- Game Control --------------------------------- #
    def activate_slowmo(self):
        self.slowmo_timer = Timer(3500)

    def check_collisions(self):
        pr = self.player.rect().inset(2, 2)
        for o in list(self.obstacles):
            if pr.intersects(o.rect()):
                if self.player.hit():
                    self.game_over = True
                    self.sfx_hit()
                    self.save_high_if_needed()
                else:
                    # consume obstacle if shielded
                    o.dead = True
                    self.emit_spark(o.rect().x + 6, o.rect().y + 6)
                break

    def save_high_if_needed(self):
        if self.score > self.high:
            self.high = self.score
            self.save_high()

    def update_speed(self, dt: float):
        # Speed slowly ramps with distance
        self.distance += self.get_speed()
        target = self.base_speed + min(6.0, self.distance / 1800.0)  # cap growth
        self.speed = lerp(self.speed, target, 0.02)
        # periodic tiny wobble for feel
        self.speed += 0.07 * math.sin(self.distance / 240.0)
        self.speed = clamp(self.speed, 4.0, 16.0)

    def update_time_of_day(self):
        # cycle every ~45 seconds
        self.time_t += 0.002
        phase = (math.sin(self.time_t) + 1) / 2
        self.sky = blend_hex(DAY_SKY, NIGHT_SKY, phase)

    def update(self, dt: float):
        if self.paused or self.game_over:
            return

        self.update_speed(dt)
        self.update_time_of_day()
        self.maybe_spawn()

        # Update entities
        self.player.update(dt)

        for arr in (self.clouds, self.ground, self.obstacles, self.collectibles, self.powerups, self.particles):
            for e in list(arr):
                e.update(dt)
            arr[:] = [e for e in arr if not e.dead]

        # collisions
        self.check_collisions()

        # scoring (distance)
        self.score += int(self.get_speed() * 0.2)
        if self.score % 500 == 0:
            # celebratory ping
            self.sfx_coin()

    def draw_background(self):
        # sky
        bg = self.sky if self.color_mode == 0 else invert_hex(self.sky)
        self.c.create_rectangle(0, 0, W, H, fill=bg, outline='')
        # stars at night
        night_k = hex_mix_ratio(self.sky, NIGHT_SKY)
        if night_k > 0.6:
            for (sx, sy) in self.stars:
                if random.random() < 0.97:
                    self.c.create_oval(sx, sy, sx + 1.8, sy + 1.8, fill=STAR_COLOR, outline='')
        # clouds
        for cl in self.clouds:
            cl.draw()

    def draw_ground(self):
        for g in self.ground:
            g.draw()
        # baseline
        self.c.create_line(0, GROUND_Y + 6, W, GROUND_Y + 6, fill=GROUND_DARK)

    def draw_entities(self):
        for a in self.collectibles:
            a.draw()
        for p in self.powerups:
            p.draw()
        for o in self.obstacles:
            o.draw()
        self.player.draw()
        for p in self.particles:
            p.draw()

    def draw_ui(self):
        txt = f"Score: {self.score:06d}    High: {self.high:06d}"
        color = TEXT_COLOR if self.color_mode == 0 else TEXT_INV
        self.c.create_text(W - 10, 18, text=txt, anchor='ne', font=('Consolas', 12, 'bold'), fill=color)

        if self.banner_timer and not self.banner_timer.done():
            t = 1.0 - self.banner_timer.progress()
            msg = f"Difficulty {self.diff}  |  P:Pause  R:Restart  M:Mute  F1:Debug  C:Contrast"
            self.c.create_text(W/2, 40, text=msg, fill=color, font=('Consolas', 12, 'bold'))

        if self.paused:
            self.c.create_rectangle(W/2 - 120, H/2 - 50, W/2 + 120, H/2 + 50, fill=blend_hex(self.sky, '#000000', 0.35), outline='')
            self.c.create_text(W/2, H/2 - 10, text='PAUSED', font=('Consolas', 18, 'bold'), fill=color)
            self.c.create_text(W/2, H/2 + 14, text='Press P to resume', font=('Consolas', 11), fill=color)

        if self.game_over:
            self.c.create_rectangle(W/2 - 150, H/2 - 60, W/2 + 150, H/2 + 60, fill=blend_hex(self.sky, '#000000', 0.35), outline='')
            self.c.create_text(W/2, H/2 - 16, text='GAME OVER', font=('Consolas', 20, 'bold'), fill=color)
            self.c.create_text(W/2, H/2 + 12, text='Press R to restart', font=('Consolas', 11), fill=color)

        if self.debug:
            dbg = [
                f"Entities: obs={len(self.obstacles)} col={len(self.collectibles)} pwr={len(self.powerups)} parts={len(self.particles)}",
                f"Speed: {self.get_speed():.2f} (base {self.base_speed:.1f}) dist={self.distance:.0f}",
                f"Player y={self.player.y:.1f} vy={self.player.vy:.2f} on_ground={self.player.on_ground} duck={self.player.ducking}",
                f"SlowMo: {'ON' if (self.slowmo_timer and not self.slowmo_timer.done()) else 'off'}",
            ]
            y = H - 56
            for line in dbg:
                self.c.create_text(10, y, text=line, anchor='nw', fill=color, font=('Consolas', 10))
                y += 14

    def draw(self):
        self.c.delete('all')
        self.draw_background()
        self.draw_ground()
        self.draw_entities()
        self.draw_ui()

    def loop(self):
        if not self.running:
            return
        ms = now_ms()
        dt = (ms - self.last_ms) / 16.6667  # normalize to ~60fps units
        self.last_ms = ms
        try:
            self.update(dt)
            self.draw()
        except Exception as e:
            # Fail-safe overlay
            self.c.delete('all')
            self.c.create_text(W/2, H/2 - 20, text='An error occurred', font=('Consolas', 16, 'bold'), fill='red')
            self.c.create_text(W/2, H/2 + 10, text=str(e), font=('Consolas', 10), fill='red')
        finally:
            self.root.after(DT_MS, self.loop)

    def restart(self):
        self.paused = False
        self.game_over = False
        self.score = 0
        self.distance = 0
        self.speed = self.base_speed
        self.slowmo_timer = None

        self.player = Player(self)
        self.obstacles.clear()
        self.collectibles.clear()
        self.powerups.clear()
        self.particles.clear()
        self.clouds = [Cloud(self) for _ in range(2)]
        self.spawn_ground()
        self.next_obstacle.reset(self.rng_obs_interval())
        self.next_coin.reset(self.rng_coin_interval())
        self.next_power.reset(random.randint(9000, 14000))

    # ------------------------- Helpers -------------------------------------- #
    def end(self):  # pragma: no cover
        self.running = False
        self.root.destroy()

# ------------------------------ Color Utils -------------------------------- #

def hex_to_rgb(hx: str) -> Tuple[int, int, int]:
    hx = hx.lstrip('#')
    return tuple(int(hx[i:i+2], 16) for i in (0, 2, 4))  # type: ignore


def rgb_to_hex(r: int, g: int, b: int) -> str:
    return f"#{r:02x}{g:02x}{b:02x}"


def blend_hex(a: str, b: str, t: float) -> str:
    ar, ag, ab = hex_to_rgb(a)
    br, bg, bb = hex_to_rgb(b)
    r = int(lerp(ar, br, t))
    g = int(lerp(ag, bg, t))
    b = int(lerp(ab, bb, t))
    return rgb_to_hex(r, g, b)


def invert_hex(h: str) -> str:
    r, g, b = hex_to_rgb(h)
    return rgb_to_hex(255 - r, 255 - g, 255 - b)


def hex_mix_ratio(a: str, b: str) -> float:
    # return rough similarity of a to b (0..1 where 1 means equal to b)
    ar, ag, ab = hex_to_rgb(a)
    br, bg, bb = hex_to_rgb(b)
    da = abs(ar - br) + abs(ag - bg) + abs(ab - bb)
    return 1.0 - clamp(da / (255*3), 0.0, 1.0)

# ------------------------------ Main ---------------------------------------- #

def main():
    root = tk.Tk()
    Game(root)
    root.mainloop()


if __name__ == '__main__':
    main()
