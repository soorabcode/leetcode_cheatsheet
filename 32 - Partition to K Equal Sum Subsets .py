# Day 32
# Partition to K Equal Sum Subsets
# Given an integer array nums and an integer k, 
# return true if it is possible to divide this array 
# into k non-empty subsets whose sums are all equal
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
        def backtrack(start, current_sum, subsets_remaining):
            if subsets_remaining == 1:
                return True
            if current_sum == target:
                return backtrack(0, 0, subsets_remaining - 1)
            for i in range(start, len(nums)):
                if not used[i] and current_sum + nums[i] <= target:
                    used[i] = True
                    if backtrack(i + 1, current_sum + nums[i], subsets_remaining):
                        return True
                    used[i] = False
                    if current_sum == 0:
                        return False
            return False
        return backtrack(0, 0, k)
