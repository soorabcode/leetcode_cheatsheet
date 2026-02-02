# Day 49 
# Minimum Window Substring 
# Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".
# The testcases will be generated such that the answer is unique.
from collections import Counter, defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""
        need = Counter(t)
        window = defaultdict(int)
        have = 0
        need_count = len(need)
        res_len = float("inf")
        res = (-1, -1)
        l = 0
        for r in range(len(s)):
            char = s[r]
            window[char] += 1
            if char in need and window[char] == need[char]:
                have += 1
            while have == need_count:
                if (r - l + 1) < res_len:
                    res = (l, r)
                    res_len = r - l + 1
                window[s[l]] -= 1
                if s[l] in need and window[s[l]] < need[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return "" if res_len == float("inf") else s[l:r+1]
