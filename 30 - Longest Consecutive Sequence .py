# Day 30
# Longest Consecutive Sequence
# Given an unsorted array of integers nums, return the length of the longest 
# consecutive elements sequence 
# You must write an algorithm that runs in O(n) time 
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0
        for num in num_set : 
            if num - 1 not in num_set:
                current_num = num
                current_length = 1
                while current_num + 1 in num_set:
                    current_num += 1
                    current_length += 1
                longest = max(longest, current_length)
        return longest
