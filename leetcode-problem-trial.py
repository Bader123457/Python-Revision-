nums = [2,10,10,30,30,30]

hashset = set() 
for num in nums:
    if not num in hashset: 
        hashset.add(num) 
    else:
        pass 

new_list=list(hashset) 
k = len(new_list)
print(k) 
print(new_list) 
