# Given an array of strings strs, group the anagrams together. You can return the answer in any order.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

# Example 1:

# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

# Question says;
# we have given an array of strings. we have to group the anagrams together. an anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once. we have to return the answer in any order.

# how can we solve this problem?

# we can use a dictionary to store the anagrams. we can sort the string and use the sorted string as the key and the original string as the value. if the sorted string is already present in the dictionary then we can append the original string to the value of the key else we can create a new key with the sorted string and the original string as the value.

# let's see the code for the above approach.

def groupAnagrams(strs):
    d = {} # creating a dictionary to store the anagrams
    for s in strs: # iterating through the array of strings
        sorted_s = ''.join(sorted(s)) # sorting the string
        if sorted_s in d: # if the sorted string is already present in the dictionary then we can append the original string to the value of the key
            d[sorted_s].append(s)
        else: # if the sorted string is not present in the dictionary then we can create a new key with the sorted string and the original string as the value
            d[sorted_s] = [s]
    return list(d.values()) # returning the values of the dictionary as a list

# time complexity: O(n*mlogm) where n is the number of strings in the array and m is the length of the string
# space complexity: O(n) where n is the number of strings in the array

# let's test the code with the given example.

strs = ["eat","tea","tan","ate","nat","bat"]
print(groupAnagrams(strs)) # it should return [["eat","tea","ate"],["tan","nat"],["bat"]] as the output

# the output is [["eat","tea","ate"],["tan","nat"],["bat"]] which is the correct output.

# let's test the code with some more testcases.


