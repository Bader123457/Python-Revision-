# dictonaries are one of the basic data types in python they consist of a key with its along value
# {key:value} 
# they are ordered and changable but don't allow duplicates
# an example of a key and a value could be an item and its price 
# let's create a dictionary for capitals 
capitals = {"USA" : "Washington",
            "India" : "New Delhi", 
            "China" : "Beijing",
            "Russia":"Moscow"}
# here are the rules of dictionary syntax 
# they are made using {} just like sets 
# to attach a key to a value we use : 
# when we want to add another keys and values we use a comma (,) 

# to obtain the value of a key we use the .get() function,ex:
print(capitals.get("USA")) # Washington 
# we need the key to get the value , for example just like we need to get a supermarket item to know it's price 
print(capitals.get("India")) # New Delhi 

# if python is asked to get a key that doesn't exist it will return None, ex:
print(capitals.get("Japan"))

# let's try this this with an if-else statement: 
if capitals.get("Egypt") == None:
    print("capital not found")
else:
    print("capital found")

# to check if a key is in a dictionary we use the .get() method 

# moving on, let's update our dictionary 
capitals.update({"Germany":"Berlin"}) # this will update the dictionary to contain all the key-value pairs but also with Germany:Berlin
print(capitals) # should include all our key-value pairs along with Germany:Berlin 

# you can also update the value of a key,ex:
capitals.update({"USA":"Detroit"})
print(capitals) 

# we can remove a key-value pair by using the .pop() function but all we need is the key
capitals.pop("China") # China : Beijing will be removed 
print(capitals)

# to remove just the latest key-value pair we do this 
capitals.popitem() # don't need to pass in a value
print(capitals)

# capitals.clear() clears the whole dictionary 

# to get all the keys in a dictionary without the values we do this 
keys = capitals.keys() 
print(keys)

# we can also do this 
for key in capitals.keys():
    print(key) 

# to get all the values is very similar 
values = capitals.values() 
print(values)
# we can also do this 
for value in capitals.values():
    print(value) 


# moving on , to items 
items = capitals.items()
print(items) 
# what .items() does is that it returns the dictionary as a 2D-List of tuples 
# we can use that to print the key and values seperately 
for key,value in capitals.items():
    print(f"{key}:{value}") # print-f statement used 


tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 4127
print(tel)
# {'jack': 4098, 'sape': 4139, 'guido': 4127}

print(tel['jack']) # 4098 

del tel['sape']
tel['irv'] = 4127
print(tel) # {'jack': 4098, 'guido': 4127, 'irv': 4127}

print(list(tel)) #['jack', 'guido', 'irv']
# that just converts it to a list 

print(sorted(tel)) # sorts the keys in alphabetical order 

print('guido' in tel) # True

print('jack' not in tel) # False 



# dictionaries allows us to index values by a key we choose instead of numbers like in arrays 


 