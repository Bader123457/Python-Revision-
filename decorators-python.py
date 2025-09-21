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




