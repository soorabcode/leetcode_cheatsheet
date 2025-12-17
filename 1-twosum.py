#Problem : Two Sum
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

#Solution
# Create a dictionary to store numbers we've seen and their indices
# Iterate over the list with index and value
# Calculate the complement needed to reach the target
# If the complement is already in the seen dictionary, return the indices
# Otherwise, add the current number and its index to the dictionary
# If no solution is found, return an empty list (though the problem assumes one exists)
class Solution:
    def twoSum(self, nums, target):
        seen = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i
        return []