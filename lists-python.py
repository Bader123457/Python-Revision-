# what is  a list?
# a list is just like a dynamic array however it can store elements of different types 
# what is the difference between a list and an array in python?
# a list allows for the storing for different type of elements while all elements in array need to be of the same type 
# we create a list using [], example:
letters = ["a","b","c"] 
# we can also have a list of lists also known as 2d lists or nested lists, example 
matrix = [[0,1],[1,2],[3,4]]
# lists also have a very good property, where we can add as many elements as we want using *, ex:
zeros = ["0"] * 10 # this creates a list of 10 zeros 
print(zeros)
# we can also concatenate or join together two lists just by the + button, ex:
combined = letters + zeros # this will join together both these lists that we made
print(combined)

# now let's say in a list we wanted numbers from 0 to 20 instead of doing it manually we can do it easily using this list function 
numbers = list(range(21)) # places all numbers inside the list numbers from 0 to 20 
print(numbers) 

# to get the number of elemts in a list or its size we use the len() function, ex:
print(len(letters)) # outputs the size of the letters list which is 3 

# moving on 
# in lists each elements has an index where the first elements has index 0 and we can access elements in lists by their index, ex: 
new_letters = ["a","b","c","d"]
print(new_letters[0]) # will print a 
print(new_letters[3]) # will print d 

# lists in python are mutuable so we can change elemts by accessing their index , ex 
new_letters[0] = "A" 
print(new_letters) # new list is [A,b,c,d] 
# now we go to something called slicing , very useful 
print(new_letters[0:3]) # this prints out every element in our list from the elemnent in the 0th index to the element in the 2nd index 
# the index on the left it will start from and the one on the right it will print the one before it 
# there is also different properties, look : 
print(new_letters[0:]) # this print out every element from the first one till the last one, very useful if you don't know the number of elements 
print(new_letters[:2]) # this will print every element from the one with the 0th index till the first one (the one before the 2nd index) so the 0th and the 1st
# when we write nothing on the left for slicing it assumes 0 


# we can also do some different properties 
new_numbers = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20] 
print(new_numbers[::2]) # this will jump by 2 everytime printing out an elements so in this example it will print 0,2,4,.....,20
# you can also reverse a list by doing this 
print(new_numbers[::-1]) 




# moving on 
# lists looping 
list_1 = ["a","b","c"] 
#let's say we want to print out every element in this list using a for loop, this is how to do it:
for letter in list_1 :
    print(letter) 

# we can also use a better for loop 
for letter in enumerate(list_1): # enumerate creates a tuple of the element along with its index
    print(letter) 



# moving on 
# we will go through built in list functions, there are 11 overall 
people = ["Badr","Taimor","Muhammed"] 
people.append("Omar") # Omar gets added to the end of the list 
print(people) # ['Badr','Taimor','Muhammed','Omar'] 
new_people = people.copy() # copies out the whole list so now people and new_people are exactly the same 
print(new_people) # ['Badr','Taimor','Muhammed','Omar'] 
people.clear() # wipes out the whole list clean , so this function fully removes all elements inside that list 
print(people) # []
people = ["Badr","Badr","Badr","Taimor","Muhammed","Omar"] 
x= people.count("Badr") # counts the number of times the specified elements is in the list ( in this case the specified element is Badr) 
print(x) # 3 

# now the .extend() function is different it's used to join together 2 lists, ex: 
people_2 = ["Talha","Hameed","Ishtiaque"] 
people.extend(people_2) 
# now the list people_2 should be found inside people 
print(people) # it is 
print(people.index("Omar")) # finds the index the element Omar is inside 

people.insert(5,"Rauf") # this function inserts the element Rauf at index number 5 , all the other elements remain they just shift to the rigth if they are after it 
print(people) 

people.pop() # removes the last element from the list which in this case is Ishtiaque  
print(people) 
# you can also use it to remove an element you don't want using the index , ex:
people.pop(1) # will remove element with index 1 
print(people)  


people.remove("Talha") # .remove() is used to remove any element we want but this time not the index is needed instead what is needed is the element itself 
print(people)   

people.reverse() # reverses the list 
print(people) 


people.sort() # sorts our list alphabetically 
print(people)
# you can also sort it out however you want using a lambda function key,  


# Moving on and finally 
# the differences between list,tuple,set 
# list : mutable,allows duplicates , indexing,[], ordered 
# tuple : ordered, not mutable, allows duplicates,indexing,
# it's syntax looks like this : tuple = (5,10) you must include a comma 
# set : not ordered, mutable,doesn't allow duplicates , doesn't allow indexing , looks like this:
# hashset = {10,20,30}








           










