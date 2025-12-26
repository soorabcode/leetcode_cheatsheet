# Day 10 
# Problem : Minimum Size Subarray Sum 
#Given an array of positive integers nums and a 
# positive integer target, return the minimal length of a 
# subarray whose sum is greater than or equal to target
# If there is no such subarray, return 0 instead. 
# Solution 
# Begin To Loop The Array 
# Sum The Elements And Check If It's Equal To Target Or Not 

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if not nums:
            return 0
        
        size = len(nums) + 1
        start = 0
        current_sum = 0
        
        for end in range(len(nums)):
            current_sum += nums[end]
            while current_sum >= target and start <= end:
                size = min(size, end - start + 1)
                current_sum -= nums[start]
                start += 1
        
        return size if size != len(nums) + 1 else 0

