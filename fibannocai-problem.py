
n = 10
a, b = 0, 1
for k in range(n):
    print(a, end=' ')
    a, b = b, a + b





nums = [1,10,19,2,3,4,7,8,9,11,8 ] 

L = 0 
R = len(nums) - 1 
while L < R:
    if nums[L] < nums[R]:
        L = L+ 1
        
    if nums[L] > nums[R]:
        R = R - 1 

print(max(nums[L],nums[R])) 



