# REPL is a python interactive shell , it stands for read , evaluate , print, loop 
# to activate it just type python into powershell. 
exponent = 2 ** 2 # same as 2 to the power of 2 which is 4 
print(exponent)
# a ** b is the same as a to the power of b 
binary_num = 0b11000111
print(binary_num)
# we use 0b to represent binary numbers in python and 0x to represent hexadecimals 
hex_num = 0xff
print(hex_num)

# this is extremely basic but there are 5 data types in python 
# integer,float,boolean,character,string 
# integer is whole numbers like 
num = 22 
# float is decimaled numbers like 
f = 3.44 
# boolean is either True or False values 
print(5>10)
# the output here is False because 5 is not greater than 10 
# now for string, it's a group of concatenated characters, it's anythin in python found in " " it's usually used for names , ex:
name = "Badr" # Badr is a string 

# characters data type don't exist in python it's just a string of length one 
char = "a"
print(type(char)) # answer should be <class 'str'>


#now moving from data types to variables in python 
# unlike java in python you can declare variables like this 
# x = 10 
# instead of like this, int x = 10; 
#python declaration of variables is much simpler 
# to name variables in python 
# Rule 1 :you can only use letters,numbers or underscores 
# Rule 2 : you can start a variable name with a letter or an underscore but not a number 
#Rule 3 : you can't use spaces when giving your variable a name 
# Rule 4 : Variables are case sensitive just like everything in python 
# moving on , python allows us to assign multiple variables to the same value on the same line, ex:
x = y = z = 10 
print(x+y+z) # answer should be 30 

# also you can use a comma to name two different variables instead of using two lines ,ex:
c,d = 1,2 
print(c) # 1
print(d) # 2

# ; is used to make a new line ex:
name = "Badr" ; print(f"hi {name} ")
# Q : What is a constant in python and what is a variable 
# A: Constant is a value which remains the same before and after we run the code howeveer variable changes value once code is runned 
