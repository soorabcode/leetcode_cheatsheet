# Day 7 
# Problem : Product Of Array Except Self
# Given an integer array nums, return an array answer such that answer[i] 
# is equal to the product of all the elements of nums except nums[i].
# The product of any prefix or suffix of nums is 
# guaranteed to fit in a 32-bit integer.
# You must write an algorithm that runs in O(n) time 
# and without using the division operation.


# Solution 
# first we do multiplication of left to right as 
# example : [ 1 , 2 , 3 ] 
# left -> [ 1 , 1 , 2 ] 
# Again from right as [ 3 , 2 , 1 ] 
# right -> [ 1 , 3 , 6 ] 
# output = left * right 



class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1]
        for i in range(len(nums) - 1, 0, -1):
            output.append(output[-1] * nums[i])
        output = output[::-1]
        left = 1
        for i in range(len(nums)):
            output[i] = output[i] * left
            left *= nums[i]
        
        return output