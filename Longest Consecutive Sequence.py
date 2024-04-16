# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

# You must write an algorithm that runs in O(n) time.

# Example 1:

# Input: nums = [100,4,200,1,3,2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.


# The first approach that comes to our mind is to use the brute force approach. We can sort the array and then we can use 2 pointers to iterate through the array. If the element at i is equal to the element at j-1 then we can increment the count else we can update the count to 1. We can keep track of the maximum count and return it as the output.

def longestConsecutive(nums):
    if not nums: # if the array is empty then we can return 0
        return 0
    nums.sort() # sorting the array
    count = 1 # initializing the count to 1
    max_count = 1 # initializing the max_count to 1
    for i in range(1, len(nums)): # iterating through the array
        if nums[i] == nums[i-1]+1: # if the element at i is equal to the element at i-1+1 then we can increment the count
            count += 1
        elif nums[i] == nums[i-1]: # if the element at i is equal to the element at i-1 then we can continue
            continue
        else: # if the element at i is not equal to the element at i-1+1 then we can update the count to 1
            count = 1
        max_count = max(max_count, count) # updating the max_count
    return max_count # returning the max_count as the output

# time complexity: O(nlogn) because we are sorting the array
# space complexity: O(1) because we are not using any extra space other than the input array nums

# Let's test the code with the given example:

nums = [100,4,200,1,3,2]

print(longestConsecutive(nums)) # it should return 4 as the output

# the optimizes solution for this problem is to use a set to store the elements of the array. we can iterate through the array and add the elements to the set. then we can iterate through the array again and check if the element-1 is present in the set or not. if the element-1 is not present in the set then we can increment the count and check if the element+1 is present in the set or not. if the element+1 is present in the set then we can increment the count and update the max_count. we can return the max_count as the output.

def longestConsecutive(nums):
    if not nums: # if the array is empty then we can return 0
        return 0
    s = set(nums) # creating a set to store the elements of the array
    max_count = 0 # initializing the max_count to 0
    for i in nums: # iterating through the array
        if i-1 not in s: # if the element-1 is not present in the set then we can increment the count
            count = 1
            while i+1 in s: # if the element+1 is present in the set then we can increment the count
                count += 1
                i += 1
            max_count = max(max_count, count) # updating the max_count
    return max_count # returning the max_count as the output

# time complexity: O(n) because we are iterating through the array only once and checking if the element-1 and element+1 is present in the set or not
# space complexity: O(n) because we are using a set to store the elements of the array

# Let's test the code with the given example:

nums = [100,4,200,1,3,2]

print(longestConsecutive(nums)) # it should return 4 as the output



