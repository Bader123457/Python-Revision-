# the sliding window is an algorithm that is mainly used when trying to find sub-arrays or sub-strings 
# they are very useful and transform time complexity from O(N^2) to O(N) 

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