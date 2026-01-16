# Day 31 
# Maximum Product Subarray 
# Given an integer array nums, find a subarray that has the largest product, and return the product.
# The test cases are generated so that the answer will fit in a 32-bit integer
# Note that the product of an array with a single element is the value of that element
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        cur_max = cur_min = result = nums[0]
        for i in range(1, len(nums)):
            if nums[i] < 0:
                cur_max, cur_min = cur_min, cur_max
            cur_max = max(nums[i], cur_max * nums[i])
            cur_min = min(nums[i], cur_min * nums[i])
            result = max(result, cur_max)
        return result
