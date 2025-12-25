# Day 9 
# Problem : SubarraySum Equals K 
# Given an array of integers nums and an integer k ,
# return the total number of subarrays whose sum equals to k .
# A subarray is a contiguous non-empty sequence of elements within an array .

# Solution 
# Loop The Array 
# Initialise First Count 
# The Check Whether The Count = K Or Not 

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sums = defaultdict(int)
        count = 0
        current_sum = 0
        prefix_sums[0] = 1
        for num in nums:
            current_sum += num
            count += prefix_sums[current_sum - k]
            prefix_sums[current_sum] += 1
        return count
