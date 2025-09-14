# what are sets in python?
# A Set is an unordered collection data type that is iterable, mutable, and has no duplicate elements. Python’s set class represents the mathematical notion of a set.
# what's different about sets in ptython is that they don't allow duplicates. 
# python sets are defined using {} 
# they also have properties of sets in venn diagrams 
# let's look at the venn diagram properties:
# Set Union:  Set union simply bundles all elements across all sets together. It can be performed in Python either through the .union() set method or the | (pipe) operator:, ex:
A = {1,2,4,6,8} 
B = {1,2,3,4,5} 
# Set union using .union()
print(A.union(B))
 
# Set union using the | operator
print(A | B) # the U looking property in venn diagrams is that one   

# Set Intersection:
#The set intersection operator returns only the elements that are common to both sets. We can perform a set intersection in Python using either the .intersection() set method or the & (ampersand) operator:

 
# Use the method
print(A.intersection(B))
 
# Use the & operator
print(A & B)  


#Set Difference:
# Performing a set difference between sets A and B means returning only the elements present in A that are not present in B. In Python, we can use the .difference() set method or the - (minus) operator for finding the difference between two sets:
# Use the method
print(A.difference(B))
 
# Use the - operator
print(A - B)             


# Set Symmetric Difference
#The set symmetric difference operator returns the elements that are unique to either A or B, ignoring the elements that are common to both sets. In Python, we use the .symmetric_difference() set method in order to perform it:
print(A.symmetric_difference(B))
 

# we can also check if elements are in sets, ex: 
print(1 in A) # True  
print(16 in B) # False 

# moving on , 
# we create sets like this 
C = {1,2,3} 
# or also we can do this 
D = set([1,1,2,2,3,3,4,4,5,5]) # we apply the set function to a list 
print(D) # {1, 2, 3, 4, 5}, won't allow duplicates 
# you can also do this 
my_set = set()
my_set.add(2)
my_set.add(4)
print(my_set) # {2,4}   

# sets are unordered and unindexed 
utensils = {"fork","spoon","knife"} 
utensils.add("napkin") # adds an elemnt to our set 
utensils.remove("fork") # removes the fork element from our set 
# if we do utensils.clear() the whole set will be wiped out 
dishes = {"bowl","plate","cup"} 
# let's say we want to add our set dishes to our set utensils 
utensils.update(dishes) # adds togehter these 2 sets 
 
for x in utensils : 
    print(x) # elements in the set will print but they won't be in the same order 
    # because sets in python are not ordered, which makes them faster than a list since lists are orded 
     


