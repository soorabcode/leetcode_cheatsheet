# Day 29
# Majority Element II 
# Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        count1 = count2 = 0
        cand1 = cand2 = None
        for n in nums:
            if cand1 == n:
                count1 += 1
            elif cand2 == n:
                count2 += 1
            elif count1 == 0:
                cand1 = n
                count1 = 1
            elif count2 == 0:
                cand2 = n
                count2 = 1
            else:
                count1 -= 1
                count2 -= 1
        result = []
        N = len(nums)
        if nums.count(cand1) > N // 3:
            result.append(cand1)
        if cand2 != cand1 and nums.count(cand2) > N // 3:
            result.append(cand2)
        return result
