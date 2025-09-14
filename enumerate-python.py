# in python we can pair up a element with its index like this 
counter = 0 
arr = [3,2,4,-1] 

for num in arr:
    print(f"this element {num} has index {counter} ") 
    counter += 1 
# however this is really inefficent and requires mutliple steps 
# a very good way would be 

for idx,num in enumerate(arr):
    print([idx,num]) 
    # here I have paired each index with its corresponding element in a list  
    # in enumerate a,b a is the index and b is the element 


print(list(enumerate(arr)))
# this will create a list of tuples of index-value pairs since enumerate creates tuples of these pairs


