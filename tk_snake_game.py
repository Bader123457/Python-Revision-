"""
Tkinter Snake Game

Controls:
- Arrow keys or WASD: Move
- P: Pause/Resume
- R: Restart
- Esc or Q: Quit

Run: python tk_snake_game.py
"""

import random
import tkinter as tk
from pathlib import Path


class SnakeGame(tk.Tk):
    CELL = 20
    COLS = 30
    ROWS = 20
    WIDTH = COLS * CELL
    HEIGHT = ROWS * CELL

    BG = "#1e1e1e"
    GRID = "#2a2a2a"
    SNAKE = "#8aff80"
    SNAKE_HEAD = "#00ff66"
    FOOD = "#ff5c5c"
    TEXT = "#e6e6e6"

    BASE_DELAY = 120  # ms
    MIN_DELAY = 50

    def __init__(self):
        super().__init__()
        self.title("Snake — Tkinter")
        self.resizable(False, False)
        self.configure(bg=self.BG)

        self._after_id = None
        self.running = False
        self.paused = False

        self.high_score_path = Path(".snake_high_score.txt")
        self.high_score = self._load_high_score()

        self._build_ui()
        self._bind_keys()
        self.reset_game()

    # UI setup
    def _build_ui(self):
        top = tk.Frame(self, bg=self.BG)
        top.pack(fill=tk.X, padx=10, pady=(10, 6))

        self.score_var = tk.StringVar(value="Score: 0")
        self.high_var = tk.StringVar(value=f"High: {self.high_score}")
        self.status_var = tk.StringVar(value="Press any arrow key to start")

        score_lbl = tk.Label(top, textvariable=self.score_var, fg=self.TEXT, bg=self.BG, font=("Segoe UI", 11, "bold"))
        score_lbl.pack(side=tk.LEFT)

        high_lbl = tk.Label(top, textvariable=self.high_var, fg=self.TEXT, bg=self.BG, font=("Segoe UI", 11))
        high_lbl.pack(side=tk.LEFT, padx=(12, 0))

        status_lbl = tk.Label(top, textvariable=self.status_var, fg="#bdbdbd", bg=self.BG, font=("Segoe UI", 10))
        status_lbl.pack(side=tk.RIGHT)

        self.canvas = tk.Canvas(self, width=self.WIDTH, height=self.HEIGHT, bg=self.BG, highlightthickness=0)
        self.canvas.pack(padx=10, pady=(0, 10))

        controls = tk.Frame(self, bg=self.BG)
        controls.pack(pady=(0, 10))

        tk.Button(controls, text="Start", command=self.start_game).pack(side=tk.LEFT)
        tk.Button(controls, text="Pause", command=self.toggle_pause).pack(side=tk.LEFT, padx=6)
        tk.Button(controls, text="Reset", command=self.reset_and_stop).pack(side=tk.LEFT)

    def _bind_keys(self):
        # Movement keys
        self.bind("<Up>", lambda e: self.queue_direction((0, -1)))
        self.bind("<Down>", lambda e: self.queue_direction((0, 1)))
        self.bind("<Left>", lambda e: self.queue_direction((-1, 0)))
        self.bind("<Right>", lambda e: self.queue_direction((1, 0)))

        self.bind("w", lambda e: self.queue_direction((0, -1)))
        self.bind("s", lambda e: self.queue_direction((0, 1)))
        self.bind("a", lambda e: self.queue_direction((-1, 0)))
        self.bind("d", lambda e: self.queue_direction((1, 0)))

        # Control keys
        self.bind("p", lambda e: self.toggle_pause())
        self.bind("P", lambda e: self.toggle_pause())
        self.bind("r", lambda e: self.reset_and_stop(start_after=True))
        self.bind("R", lambda e: self.reset_and_stop(start_after=True))
        self.bind("<Escape>", lambda e: self.quit())
        self.bind("q", lambda e: self.quit())

    # Game state
    def reset_game(self):
        mid_x = self.COLS // 2
        mid_y = self.ROWS // 2
        self.snake = [(mid_x - 1, mid_y), (mid_x, mid_y)]  # tail -> head
        self.direction = (1, 0)
        self.pending_dir = []  # queue to prevent instant reverse
        self.score = 0
        self.delay = self.BASE_DELAY
        self.paused = False
        self.running = False
        self.food = self._random_free_cell()
        self._draw()
        self._update_labels()
        self.status_var.set("Press any arrow key or Start")

    def reset_and_stop(self, start_after=False):
        self.stop_loop()
        self.reset_game()
        if start_after:
            self.start_game()

    def start_game(self):
        if not self.running:
            self.running = True
            self.paused = False
            self.status_var.set("Playing — P to pause")
            self._loop()

    def toggle_pause(self):
        if not self.running:
            return
        self.paused = not self.paused
        if self.paused:
            self.status_var.set("Paused — P to resume")
        else:
            self.status_var.set("Playing — P to pause")
            self._loop()

    def stop_loop(self):
        if self._after_id is not None:
            try:
                self.after_cancel(self._after_id)
            except Exception:
                pass
            self._after_id = None

    def queue_direction(self, new_dir):
        # Kick off the game on first input
        if not self.running:
            self.start_game()

        if self.pending_dir and self.pending_dir[-1] == new_dir:
            return
        # Prevent 180-degree reversal from current effective direction
        last_dir = self.pending_dir[0] if self.pending_dir else self.direction
        if (last_dir[0] + new_dir[0] == 0) and (last_dir[1] + new_dir[1] == 0):
            return
        self.pending_dir.append(new_dir)

    # Loop
    def _loop(self):
        if not self.running or self.paused:
            return
        self._step()
        self._after_id = self.after(self.delay, self._loop)

    def _step(self):
        # Apply any queued direction change
        if self.pending_dir:
            self.direction = self.pending_dir.pop(0)

        head_x, head_y = self.snake[-1]
        dx, dy = self.direction
        new_head = (head_x + dx, head_y + dy)

        # Wall collision
        if not (0 <= new_head[0] < self.COLS and 0 <= new_head[1] < self.ROWS):
            self._game_over()
            return

        # Self collision
        if new_head in self.snake:
            self._game_over()
            return

        self.snake.append(new_head)

        if new_head == self.food:
            self.score += 1
            self._maybe_speed_up()
            self.food = self._random_free_cell()
        else:
            # Move forward: remove tail
            self.snake.pop(0)

        self._draw()
        self._update_labels()

    def _maybe_speed_up(self):
        # Increase speed every 3 points
        if self.score % 3 == 0 and self.delay > self.MIN_DELAY:
            self.delay = max(self.MIN_DELAY, int(self.delay * 0.9))

    # Rendering
    def _draw(self):
        c = self.canvas
        c.delete("all")
        self._draw_grid()
        # Draw food
        fx, fy = self.food
        self._draw_cell(fx, fy, fill=self.FOOD, oval=True)
        # Draw snake
        for i, (x, y) in enumerate(self.snake):
            is_head = (i == len(self.snake) - 1)
            color = self.SNAKE_HEAD if is_head else self.SNAKE
            self._draw_cell(x, y, fill=color)

    def _draw_grid(self):
        c = self.canvas
        cs = self.CELL
        for x in range(0, self.WIDTH, cs):
            c.create_line(x, 0, x, self.HEIGHT, fill=self.GRID)
        for y in range(0, self.HEIGHT, cs):
            c.create_line(0, y, self.WIDTH, y, fill=self.GRID)

    def _draw_cell(self, x, y, fill, oval=False):
        cs = self.CELL
        x1 = x * cs
        y1 = y * cs
        x2 = x1 + cs
        y2 = y1 + cs
        pad = 1
        if oval:
            self.canvas.create_oval(x1 + pad, y1 + pad, x2 - pad, y2 - pad, fill=fill, outline="")
        else:
            self.canvas.create_rectangle(x1 + pad, y1 + pad, x2 - pad, y2 - pad, fill=fill, outline="")

    # Helpers
    def _random_free_cell(self):
        occupied = set(self.snake) if hasattr(self, "snake") else set()
        free = [(x, y) for x in range(self.COLS) for y in range(self.ROWS) if (x, y) not in occupied]
        return random.choice(free) if free else (0, 0)

    def _update_labels(self):
        self.score_var.set(f"Score: {self.score}")
        self.high_var.set(f"High: {self.high_score}")

    def _game_over(self):
        self.running = False
        self.stop_loop()
        if self.score > self.high_score:
            self.high_score = self.score
            self._save_high_score(self.high_score)
        self._draw()
        self._update_labels()
        self._draw_game_over()
        self.status_var.set("Game Over — R to restart")

    def _draw_game_over(self):
        # Overlay message
        overlay = self.canvas.create_rectangle(0, 0, self.WIDTH, self.HEIGHT, fill="#000000", stipple="gray25", outline="")
        msg = "Game Over\nR: Restart   Q/Esc: Quit"
        self.canvas.create_text(
            self.WIDTH // 2,
            self.HEIGHT // 2,
            text=msg,
            fill=self.TEXT,
            font=("Segoe UI", 16, "bold"),
            justify=tk.CENTER,
        )
        return overlay

    # High score persistence
    def _load_high_score(self) -> int:
        try:
            if self.high_score_path.exists():
                return int(self.high_score_path.read_text().strip() or 0)
        except Exception:
            pass
        return 0

    def _save_high_score(self, value: int):
        try:
            self.high_score_path.write_text(str(int(value)))
        except Exception:
            pass


def main():
    app = SnakeGame()
    # Center window roughly on screen
    app.update_idletasks()
    w = app.WIDTH + 20
    h = app.HEIGHT + 90
    try:
        sw = app.winfo_screenwidth()
        sh = app.winfo_screenheight()
        x = (sw - w) // 2
        y = (sh - h) // 3
        app.geometry(f"{w}x{h}+{x}+{y}")
    except Exception:
        pass
    app.mainloop()


if __name__ == "__main__":
    main()

