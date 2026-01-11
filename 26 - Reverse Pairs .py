# Day 26 
# Reverse Pairs 
# Given an integer array nums, return the number of reverse pairs in the array.

# A reverse pair is a pair (i, j) where:
# 0 <= i < j < nums.length and
# nums[i] > 2 * nums[j] 
class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        def merge_sort(arr):
            if len(arr) <= 1:
                return arr, 0
            mid = len(arr) // 2
            left, cnt_left = merge_sort(arr[:mid])
            right, cnt_right = merge_sort(arr[mid:])
            count = cnt_left + cnt_right
            j = 0
            for i in range(len(left)):
                while j < len(right) and left[i] > 2 * right[j]:
                    j += 1
                count += j
            merged = []
            i = j = 0
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    merged.append(left[i])
                    i += 1
                else:
                    merged.append(right[j])
                    j += 1
            merged.extend(left[i:])
            merged.extend(right[j:])
            return merged, count
        _, result = merge_sort(nums)
        return result
