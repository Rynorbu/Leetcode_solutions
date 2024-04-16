# # Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

# # Example 1:

nums = [1,2,3,1]

# # This question says that we have to return true if any value appears 2 times, 3 or 4 times but atleast twice in the array, and return false if every element is distinct.

# # The first approach that comes to our mind is to use the brute force approach. We can use 2 loops and check if any element is repeated or not. If it is repeated then we can return true else we can return false.

def containsDuplicate(nums):
     for i in range(len(nums)):  # this loop will iterate through the array
         for j in range(i+1, len(nums)): # this loop will iterate through the array starting from i+1 till the end of the array
             if nums[i] == nums[j]: # if the element at i is equal to the element at j then we can return true

                  return True # if the element is repeated then we can return true
     return False # if no element is repeated then we can return false

# # Time complexity: O(n^2) because we are using 2 loops to iterate through the array
# # Space complexity: O(1) beacuse we are not using any extra space other than the input array nums 

# # But this approach will take O(n^2) time complexity and O(1) space complexity.

# # We can use a better approach to solve this problem. We can use a set to store the elements of the array. If the length of the set is equal to the length of the array then we can return false else we can return true.

# # This approach will take O(n) time complexity and O(n) space complexity.

# # Let's see the code for the above approach.

def containsDuplicate(nums):
     s = set() # creating a set to store the elements of the array 
     for i in nums: # iterating through the array
         if i in s: # if the element is already present in the set then we can return true
             return True 
         s.add(i) # if the element is not present in the set then we can add the element to the set
     return False# if no element is repeated then we can return false

# Time complexity: O(n) because we are iterating through the array only once and adding the elements to the set only once
# Space complexity: O(n) because we are using a set to store the elements of the array 

# now lets use the concept of double pointers to solve this problem. in this double pointer approach we will sort the array and then we will use 2 pointers to iterate through the array. if the element at i is equal to the element at j then we can return true else we can return false.

def containsDuplicate(nums):
    nums.sort() # sorting the array
    i = 0 # initializing the first pointer to 0
    j = 1 # initializing the second pointer to 1
    while j < len(nums): # iterating through the array
        if nums[i] == nums[j]: # if the element at i is equal to the element at j then we can return true
            return True
        i += 1 # incrementing the first pointer
        j += 1 # incrementing the second pointer
    return False # if no element is repeated then we can return false

# time complexity: O(nlogn) because we are sorting the array
# space complexity: O(1) because we are not using any extra space other than the input array nums
