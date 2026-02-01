# Day 48 
# Longest Substring Without Repeating Characters
# Given a string s, find the length of the longest substring without duplicate characters.
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l , res = 0 , 0 
        for r in range(len(s)):
            while s[r] in charSet : 
                charSet.remove(s[l])
                l+=1 
            charSet.add(s[r])
            res = max ( res , r - l + 1)
        return res
