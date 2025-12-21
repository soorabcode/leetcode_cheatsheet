# Day 5 
# Problem : Maximum SubArray 
# Given an integer array nums
# Find the subarray with the largest sum, and return its sum. 

# Used Concepts : Array & Kaden's Algorithm 
# Solution : 
# Loop Nums Of Array 
# Current Sum = Max ( Current Sum + Num , Num ) 
# Maximum Sum = Max ( Maximum Sum , Current Sum )
# Return Maximum Sum 

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        max_sum = nums[0]
        curr_sum = 0
        for num in nums:
            curr_sum = max(curr_sum + num, num)
            max_sum = max(max_sum, curr_sum)
        return max_sum
