# Day 16
# Missing Number
# Given an array nums containing n distinct 
# numbers in the range [0, n], return the only 
# number in the range that is missing from the array 

# sort()
# if the index ind matches the value at nums[ind]
# return index

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        for ind in range(len(nums)):
            if ind != nums[ind]:
                return ind
        return len(nums)