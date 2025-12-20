# Day 4 
# Problem : Contains Duplicate 
# Given an integer array nums, return true if any value appears at least 
# twice in the array, and return false if every element is distinct. 
# ( Array Hashmap )

# Solution : 
# Create a set from the list, which automatically removes any duplicate elements
# Compare the length of the set with the original 
# If lengths differ, it means there were duplicates in the list

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)