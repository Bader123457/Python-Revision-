# what is a decorator in python?
# a python decorator function that takes in another function adds some functionality to it then returns it 
# in python everything is an object from arrays,variables,functions,classes and more 

# we can pass functions as arguments to other functions 
# here is an example 
def inc(x) :
    return x+1 


def operate(func,x): # here a function is an argument
    result = func(x) 
    return result 

print(operate(inc,2)) # 3
# here our parameter is the inc function we created 


# the main takeaway here is that a function can take another function as an argument 


# we can also define a function iside a function (nested functions)
# ex:

def print_message(message):
    greeting = "hello" 

    def printer():
        print(greeting,message)

    printer() 
print_message("I am 19 years of age  ") 

# output will be hello I am 19 years of age 
 

# now we are done with all of this 
# let's create a decorator 

def printer():
    print("hello world") 

def display_info(func):
    def inner():
        print("executing", func.__name__,"function") 
        func()
        print("finished") 
    return inner 
print(display_info(printer))




# here is a very good example for it 

def my_decorator(func):
    def wrapper():
        print("Something happens *before* the function is called.")
        func()
        print("Something happens *after* the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()


# it's syntax comes after @ 
# so we applied say_hello() to my_decorator()


