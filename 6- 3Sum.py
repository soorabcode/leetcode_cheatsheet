# Day 6 
# Problem - 3Sum 
# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] 
# such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0
# Notice that the solution set must not contain duplicate triplets

# Solution 
# Sort The Given Array 
# Initialise The Duplicate Array 
# Loop The Array 
# First Input A Number ( a ) 
# Then Solve It As b + c = - a 
#  Calculate the sum of the current triplet 

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ret = [] 
        nums.sort()  
        for i in range(len(nums)): 
            if i > 0 and nums[i] == nums[i - 1]: 
                continue
            l = i + 1  
            r = len(nums) - 1  
            while l < r:  
                total = nums[i] + nums[l] + nums[r] 
                if total > 0: 
                    r -= 1
                elif total < 0:  
                    l += 1
                else:  
                    ret.append([nums[i], nums[l], nums[r]])  
                    l += 1  
                    r -= 1  
                    while l < r and nums[l] == nums[l - 1]: 
                        l += 1
                    while l < r and nums[r] == nums[r + 1]: 
                        r -= 1
        return ret 