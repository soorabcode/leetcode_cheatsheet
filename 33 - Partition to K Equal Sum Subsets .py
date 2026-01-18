# Day 33 
# Partition to K Equal Sum Subsets 
# Given an integer array nums and an integer k,
# return true if it is possible to divide this array into k non-empty subsets 
# whose sums are all equal

class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total_sum = sum(nums)
        if total_sum % k != 0:
            return False
        target = total_sum // k
        nums.sort(reverse=True) 
        if nums[0] > target:
            return False
        used = [False] * len(nums)
        def backtrack(start, curr_sum, subsets_formed):
            if subsets_formed == k - 1:
                return True
            if curr_sum == target:
                return backtrack(0, 0, subsets_formed + 1)
            for i in range(start, len(nums)):
                if used[i] or curr_sum + nums[i] > target:
                    continue  
                used[i] = True
                if backtrack(i + 1, curr_sum + nums[i], subsets_formed):
                    return True
                used[i] = False
                if curr_sum == 0:
                    break
            return False
        return backtrack(0, 0, 0)
