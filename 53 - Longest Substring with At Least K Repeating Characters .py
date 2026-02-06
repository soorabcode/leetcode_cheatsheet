# Day 53 
# Longest Substring with At Least K Repeating Characters
# Given a string s and an integer k, return the length of the longest substring of s such that the frequency of each character in this substring is greater than or equal to k.
# if no such substring exists, return 0.
class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        freq = {}
        for c in s :
            freq[c] = freq.get(c,0) + 1
        for i,c in enumerate(s):
            if freq[c] < k : 
                left = self.longestSubstring(s[:i],k)
                right = self.longestSubstring(s[i+1:],k)
                return max(left , right )
        return len(s)