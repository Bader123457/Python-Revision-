# what are iterators in python ?

# iterators are methods that iterate collections like lists,tuples,etc 
# They are able to loop through the object and return its elements 

# A python iterator object must implement 2 special methods 
# 1 - iter()
# 2 - next() 
# together they are known as the iterator protocol 

# let's look at an example 
arr = [4,7,0] 

iterator = iter(arr) # we created an iterator from our list 
# get the first element from the iterator 
print(next(iterator)) # 4 
# second element 
print(next(iterator)) # 7 
# third element 
print(next(iterator)) # 0 

"""
Here, first we created an iterator from the list using the iter() method.
And then used the next() function to retrieve the elements of the iterator in sequential order.
"""

# this exactly the same as doing 

for num in arr:
    print(num) 
