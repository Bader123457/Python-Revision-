# what is a function in python?
# A function is a block of reusable code 
#Groups together several lines of code, Gives that group a name,Lets you run that group by simply calling its name.
#Think of it like a blender in your kitchen: you throw in ingredients, press a button (call the function), and get a result (a smoothie).
#Why Use Functions?
#Organize your code into reusable parts, Make code easier to read and debug, allow you to avoid repetition (DRY principle: Don’t Repeat Yourself).

# to activate a function we place () after its name 
# how functions are useful : 
print("Happy birthday to you") 
# if we want to repeat this 3 times we can copy and paste it or create a for loop, both ineffiecent 
# here is where functions are helpful, we can write the block of code once and reuse it whenever we need to 
# ex: 
def happy_birthday(): # def defines the function, after we need its name then () : are essential syntax for functions 
    print("Happy birthday to you, function ") # block of code the function will execute 
happy_birthday() # to call the function or execute it to be more specific we write its name and then () 
# if we want to repeat this 2 more times we just do  this 
happy_birthday()
happy_birthday() 

# moving on 
def say_hi (name) : # in this case name is known as something called a parameter which is a variable in a function's definition 
     print(f"hi {name}, how are you?") 
say_hi("Badr") # now this is an argument, the value which we will place into the parameter here to be placed into our function 
say_hi("Omar")
say_hi("Muhammed") 
# able to repeat again for different arguments 

# now let's say we did say_hi("Badr", 19) 
# this would cause an error since we only have 1 parameter but I am placing 2 arguments
# let's try a function with more than 1 parameter 
def say_hello (name,age,nationality) : # here we have 3 different parameters 
     print(f"hi {name} ")
     print(f" you are {age} years old")
     print(f"and you are from the country of {nationality}")

say_hello("Urslan",19,"Pakistan")  # the number of argumets when we call a function always needs to be the same as the number of parameters 
say_hello("Abdulrahman",22,"Oman") # also important note the order of the arguments matters since we need a matching set to the parameters  
say_hello("Aqil",19,"India")

# moving onto return statemnts 
# return is a statement used to end a function and send the result back to the caller 
# print just displays data while return just hands data we need back 
# ex: 
def add(x,y) : # 2 parameters which is the numbers we will add together 
     z = x + y 
     return z # return here used to give us the sum back 
print(add(1,2)) # our 2 arguments are 1 and 2 so z = 3  
# here we needed to print the function and call it in order for it to be displayed 
# in the other functions we didn't need print because it had print statemnts inside the function 

# another example  
def exponent (a,b) : 
     z = a**b 
     return z  
print(exponent(4,2)) # output should be 16 

# more complex example 
def create_name(first,last): # creating function with 2 parameters 
     first = first.capitalize()
     last = last.capitalize()
     return first + " " + last # returning the concatenated full name with space in the middle 
full_name = create_name("badreldin", "elsayed") 
print(full_name) # we assigned a variable the calling of the function and then we printed it out 
# we can also do this as usual 
print(create_name("ahmed","hawash")) 


def addition(*args) : # the * here allows us to accept as many parameters because if our parameters were like a,b,c we would only be able to add 3 numbers 
     return sum(args) 
print(addition(1,2,3,4,5,6,7,8,9,10)) # now here we can as many numbers as we want since we applied the * 
# how it works is that it creates a tuple of the following numbers we made 

# another example 
def demo(*things):
    print(things)

demo("apple", "banana", "cherry")  # creates a tuple of these fruits  and prints them out 

def greet(*names):
    for name in names: # if we want to use the * and use our functions on seperate lines we use a for loop just like we used in this example 
        print(f"Hello, {name}!")

greet("Alice", "Bob", "Charlie")


# now let's do the question chatpgt gave us 
def area_of_rectangle(height,width) : 
     area = height * width 
     return area 
print(area_of_rectangle(3,5))   


def create(l,r): 
     l = l + 1 
     r = r + 1 
     return l , r 
print(create(1,2))





     


    



  
