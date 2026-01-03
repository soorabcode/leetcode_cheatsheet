# Day 18 
# Sort Colors
# Given an array nums with n objects colored red, white, 
# or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.
# We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.
# You must solve this problem without using the library's sort function.

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        red = 0
        white = 0
        blue = len(nums) - 1
        
        while white <= blue:
            curr = nums[white]
            if curr == 0:
                nums[white] = nums[red]
                nums[red] = 0
                red += 1
                white += 1
            elif curr == 1:
                white += 1
            else:
                nums[white] = nums[blue]
                nums[blue] = 2
                blue -= 1