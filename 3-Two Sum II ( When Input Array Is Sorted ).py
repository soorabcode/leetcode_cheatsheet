# Day 3 
# Problem : Two Sum II ( When Input Array Is Sorted ) 
# Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, 
# find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] 
# and numbers[index2] where 1 <= index1 < index2 <= numbers.length.
# Return the indices of the two numbers, index1 and index2, added by one as an integer 
# array [index1, index2] of length 2.

# Solution : 
# b , e refering to begging and endings index of array 
# if arr[b] + arr[e] > target , then , e = e - 1
# elif arr[b] + arr[e]  target , then , b = b + 1
# else , then , return b , e 


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        beg, end = 0, len(numbers) - 1
        while beg < end:
            total = numbers[beg] + numbers[end]
            if total == target:
                return [beg + 1, end + 1]
            if total > target:
                end -= 1
            else:
                beg += 1