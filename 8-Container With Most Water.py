# Day 8 
# Problem : Container With Maximum Amount Of Water 
# You are given an integer array height of length n. There are n vertical lines drawn such that the 
# two endpoints of the ith line are (i, 0) and (i, height[i]).
# Find two lines that together with the x-axis form a container, such that the container contains the most water.
# Return the maximum amount of water a container can store.

# Solution 
# Set Beginning As 0 And End As n - 1 
# till beginning < end
# max_area  = max of ( max_area , min(height[beginning],height[end])*(end - begining ) 
# As We Know Area = Height * Width 
# Height Is Limited By Whichever Is Lower Either Beginning Or End 
# Weight = Difference Of End And Beginning 
# if height[beginning] > height[end] , then , end = end -1 
# else , beginning = beginning + 1 
# return max_area 


class Solution:
    def maxArea(self, height: List[int]) -> int:
        beg = 0
        end = len(height) - 1
        max_area = 0
        while beg < end:
            max_area = max(max_area, min(height[beg], height[end]) * (end - beg))
            if height[beg] >= height[end]:
                end = end - 1
            else:
                beg = beg + 1
        return max_area
