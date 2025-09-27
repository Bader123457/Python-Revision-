# they are 2 major functions in python they are used to check the content of a collection 

# any will return True if any element in the collection is true 
# all will only return True if one element in the collection is True 

print(any([True,False,False])) # True 
print(any([False,False,False])) # False

# only 1 value has to be true 

print(all([False,True,True,True])) # False 
print(all([True,True,True,True])) # True 

# all of them have to be True 



# let's use it now 

numbers = [-1,-2,-4,0,3,-7] 
has_positive = False 
for n in numbers :
    if n > 0 :
        has_positive = True 
        break 

# instead of doing this we can 

has_positive = any(n>0 for n in numbers) 


