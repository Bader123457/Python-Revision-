from collections import Counter 
#from collections import defaultdict
string = "hellomynameis" 

counter = Counter(string) 
print(counter)
print(counter['e']) # 2 

# this is very useful to pair up letters in a string with their count 


myMap = {}
myMap["alice"] = 88 
myMap["bob"] = 77 
print(myMap)
# we have now created a hashmap that looks like this {'alice': 88, 'bob': 77}
print(len(myMap)) # prints the no. of keys 

print(myMap["alice"]) # will print the value of the key alice 

# to loop through keys in a hasmap 
for key in myMap.keys() :
    print(key) 

# to loop through values 
for val in myMap.values() :
    print(val) 

#to go through both 
for key,value in myMap.items() :
    print(key,value) 




"""
for more help this article is useful 
https://www.edureka.co/blog/hash-tables-and-hashmaps-in-python/
"""



# here is how to loop through an array and create a hashmap of the count of its elements 


nums = [4, 5, 4, 6, 5, 4]

counter = {} 

for num in nums:
    if num in counter :
        counter[num] += 1 
    else:
        counter[num] = 1 
        
print(counter)
