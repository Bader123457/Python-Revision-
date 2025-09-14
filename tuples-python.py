# what are tuples
# A Tuple is a collection of Python objects separated by commas. In some ways, a tuple is similar to a list in terms of indexing, nested objects, and repetition but a tuple is immutable, unlike lists that are mutable
#Similar to lists, a tuple is a collection of values that are declared using parentheses. So instead of this list:

#names = ['Olivia', 'Nathan', 'Bethany', 'Jacob']
#We format tuples like this:
names = ('Olivia', 'Nathan', 'Bethany', 'Jacob')

# other than the difference between [] and () , you can't change elements inside a tuple 
name = ("Badr",) # for it to be a tuple you need to make a comma after the first element even if there is only one element 
print(type(name)) # <class 'tuple'>

# there are 4 types of tuples 
# 1:
empty_tuple = () # that's a tuple even though it's empty 
print(empty_tuple)

#2:
#The next type of tuple is one with integers, which looks like this:
integer_tuple = (1, 2, 3)

#3:
#Next, we have a tuple with mixed data types, which might look like this:
mixed_tuple = (0, "Hello", 1.2, "World!")

#4:
#Finally, we have the nested tuple which is a tuple within a tuple and looks like this:
nested_tuple = ("aardvark", [0, 1, 2], (2, 1, 0))

# accessing tuples is easy unless they are nested, ex 
# let's say we want to access 2 in the integer_tuple:
print(integer_tuple[1]) # 2 
# easy just like in lists 

# now in nested loops it's different, let's say we wanted to access the k in the first word 
print(nested_tuple[0][7]) # prints k 
# you need 2 indexes [i][j] 
# i is the tuple you want to access inside the nested tuple and j is the element you want to access inside that tuple 
#If I want to print out the element 3 in tuple 0 
# print(nested_tuple[0][3])

# slicing works in tuples just liked it does in lists 


#We can use concatenation and repetition with tuples. Concatenation is done with the + operator like so:

print(('T', 'h', 'e') + ('N', 'e', 'w') + ('S', 't', 'a', 'c', 'k') )

#We can use repetition with the * operator like so:

print(("The New Stack",) * 3) # prints The New Stack 3 times inside a tuple 