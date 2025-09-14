# what are modules in python ?
# a module in python is a file that we can use in other files or other programs 
# a module will containt code to perform a specific task 
# here is an example 
import numpy  
# numpy is a module that contains code which we can import into our current file/program 

# using that module name we can access a function inside, ex: 

print(numpy.add(4,5)) #9 

# here is another example 
import math 
print(f"the value of pi is {math.pi}") # the value of pi is 3.141592653589793
# here we used the modules name to access a function it has (math.pi) 

# in python we can also import by renaming here is an example 
import math as m 
print(m.pi) # same as doing math.pi but we chaned the module name from math to m 
# however after you do this math.pi would be invalid since you made it m so only m.pi is valid 


# we can import something specific from the module without importing the module itself ex:
from math import pi 
print(pi) # here we didn't have to do math.pi since we imported pi itself 
# in this situation pi is a constant defined in the math module let's look at another example 

from random import randint

print(randint(1, 6))  # prints a random number between 1 and 6
# randint here is a function in the random module so we are just importing whatever we want from the module whether it's a function or a constant or anything 


# to import everything inside our module we do this 
from math import * 
# it's not good to do and is risky because it can cause overlap 


# in python we can use the dir() function to list all the funcion names in a module, here is an example 

print(dir(numpy)) # this will list all the function inside numpy 

# anything with __blahblahblah__ is just an attribute 


# there are 2 types of modules in python 
# 1- builtin like random , pandas, numpy , math and more 
# these are already are built into your python programmer all you need to do to use is just import x 
# where x is a builtin module 

# 2- custom modules 
# modules that we design our selves and import for example I design a file called Main.py then inside this file I do 
# import Main or from Main import function 




