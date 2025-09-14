# the sliding window is an algorithm that is mainly used when trying to find sub-arrays or sub-strings 
# they are very useful and transform time complexity from O(N^2) to O(N) 

# for example let's say we have an array and we want to find the subarray with the maximum sum but it has to be of size k 
# we start by creating a subarray (window) from index 0 to k-1 and then we slide it by one so the window is now at i+1 to k all we need to do is to subtract i from the sum and add k to the sum 
  