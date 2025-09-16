# the sliding window is an algorithm that is mainly used when trying to find sub-arrays or sub-strings 
# they are very useful and transform time complexity from O(N^2) to O(N) 
# there are 2 types of sliding window fixed and dynamic 

# fixed sliding window :
# when we know the size of our subarray 


# here is a good example 
# let's imagine we have an array and a value k  
# what we need to do is find a maximum sum subarray of size k 
# here we use sliding window 

nums = [8,3,-2,4,5,-1,0,5,3,9.-6] 
k = 5 

# here we would start from 8 and create a window up to 5 which has size k 
# then we compute the sum which is 
print(sum(nums[0:5])) # this subarray or window has k (5) elements inside the ans is 13 
# then we do nums[1:6] and then nums[2:7] and so on 
# we compute the sum each time and take the largest one as our answer 

# do this has time complexity of O(N*k) which is slow 

# so instead of doing it this way we follow the sliding window 
# we do it very similar but instead of computing the sum each time what we do is that we subtract the element removed from the window and sum the element added to the window 
# here is an example 
first_sub = [8,3,-2,4,5] # first window 
second_sub = [3,-2,4,5,-1] # second window 
# instead of computing the sum on both these windows we just compute the sum of the first window
# and then we subtract 8 (removed from window) from it and add -1 (new element to our window) 
# so the new sum is 18 -8 +-1 = 9  
# remember our subarray(our window) is size k

# to our sum we add the one that entered the window and subtract the one that left 
# to every window we only perform 1 addition and 1 subtraction 

# here is the psuedocode for it 
"""
currsum = best = sum(nums[0:k]) # we initalize our sum with the first window 
for R in range(k,len(nums)) :  # we then loop through all the elements not inside our current window 
    currsum = currsum + nums[R] - nums[R-k]  # we then slide our window 
    # here we add the element that enetered the window and subtract the one that left 
    best = max(best,currsum) 
    # each iteration will update the current sum if the best was ever higher it's safely stored 
    # if we find a better one best will become it 



"""


# moving on 
# Dynamic Sliding Windows 

# we have no idea what the size of our subarray can be 

# good example problem 

# you have a integer array nums find the longest subarray with sum < s where s is an integer value 

arr = [4,5,2,0,1,8,12,3,6,9] 
s = 15 

# to do this using sw we need to pointers L,R
# we place L before the beginning of the arr and we place R at arr[0] (4)

# we then process the window 
# we then keep shifting R by one to the right each time as long as the sum is less than 15 (s) 

# if the sum ever exceedes 15 then we start shrinking our window by moving our left pointer L 
# the left pointer (L) initially points to before the beginning of the arr 


# here is the pseudocode for it 

"""
L,currsum,bestsum = -1,0,0 
for R in range(len(arr)) : # our right pointer will move by going through a for loop from the beginning of the array to the end 
    currsum += arr[R] # we update our currsum each time R moves 
    if currsum >= s : # at any point if our window breaks the condition and becomes bigger than s 
        currsum -= arr[L]  # we shrink our window 
        L += 1  # we shift our left pointer 

    bestsum = max(bestsum,currsum)


        

"""

# the sliding winow is able to shift the right pointer one step at a time while shifting the left one when needed 


# V1 DONE 

# ARTICLE PART 

# check out this article 

# https://www.geeksforgeeks.org/dsa/window-sliding-technique/



# look at this sw problem for revision and this code 

"""
Example Problem - Maximum Sum of a Subarray with K Elements
Given an array arr[] and an integer k, we need to calculate the maximum sum of a subarray having size exactly k.

Input  : arr[] = [5, 2, -1, 0, 3], k = 3
"""
# here is my answer code 
nums = [5, 2, -1, 0, 3] 
k = 3
L,R = 0,0 
currsum = sum(nums[L:R-k+1]) 
best = 0 


for R in range(len(nums)):
    
    
    best = max(currsum,best)
    
    currsum -= nums[L]
    currsum += nums[R] 
    L += 1 
    
print(best) 


    

