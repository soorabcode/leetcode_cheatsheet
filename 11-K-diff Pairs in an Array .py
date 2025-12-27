# Day 11 
# Problem : K-diff Pairs in an Array 
# Given an array of integers nums and an integer k
# return the number of unique k-diff pairs in the array 
# A k-diff pair is an integer pair (nums[i], nums[j])
# where the following are true:
# 0 <= i, j < nums.length
# i != j
# |nums[i] - nums[j]| == k
# Notice that |val| denotes the absolute value of val.

class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        c = Counter(nums)
        count = 0
        if k == 0:
            for key, v in c.items():
                if v > 1:
                    count += 1
        else:
            for key, v in c.items():
                if key + k in c:
                    count += 1
        return count

