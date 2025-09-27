# they are 2 major functions in python they are used to check the content of a collection 

# any will return True if any element in the collection is true 
# all will only return True if one element in the collection is True 

print(any([True,False,False])) # True 
print(any([False,False,False])) # False

# only 1 value has to be true 

print(all([False,True,True,True])) # False 
print(all([True,True,True,True])) # True  