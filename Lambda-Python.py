# Lambda functions in python are small anonymous functions for a one time use  
# they are essentially the same as standard python functions but they are shorter and anonymous 
# they are also known as anonymous functions 
#they are allowed as much arguments but only 1 expression 


# ex :
# normal function 
def add(x,y) :
    return x+y 
print(add(4,5)) #9 

# however this is how to create a lambda function 
lambda x,y : x+y 
# we start by the lambda keyword 
# then we put the inputs in this case x,y 
# then we do : then what we need to return 
# you don't need the return keyword : acts for it 
# structure:
# lambda inputs : our_return 

add2 = lambda x,y : x+y 
print(add2(4,5)) # 9 

# you could instead of assigning a variable do this 
print((lambda x,y : x+y)(4,5)) 

# let's try another ex 
# here we have an array 
nums = [3,4,5,6,7] # we will use it later 

# what we want to do is create a function that applies any function we want to any array we want 
# so 
def my_map(my_func,my_arr) :
    res = [] 
    for item in my_arr:
        new_item = my_func(item) # we are applying our chosen function to each element in the array
        res.append(new_item) 
    return res 

cubed = my_map(lambda x: x**3 , nums) 
print(cubed)  # [27, 64, 125, 216, 343]
# in cubed the function we are doing is we are cubing elements on our nums array 
# we made the function simply with lambda by lambda x: x**3



"""
section 2 
"""

#simple lambda function to double
double = lambda x: x*2 
print(double(4)) # 8

lambda x,y : x+y 
print(add(1,4)) #5 

# to compare with lambda 
# let's use this example 
max_val = lambda x,y : x if x>y else y 
print(max_val(1,2)) 

full_name = lambda first_name,last_name : first_name + " " + last_name 
print(full_name("Badreldin","Elsayed"))


is_even = lambda x: "even" if x%2 == 0 else "odd" 
print(is_even(16)) # "even" 


# there is also something called lambda key 
# we implement the lambda function based on a key we want 
# let's say we have a list and we want to sort the elements based upon their length 

words = ["apple", "banana", "pear", "kiwi", "grape"]
sorted_words = sorted(words, key=lambda w: len(w))
print(sorted_words)
# ['pear', 'kiwi', 'apple', 'grape', 'banana']

# here our lambda function is acting as a key that puts the elements based upon their length 
