# Day 46 
# 438. Find All Anagrams in a String
# Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.
from typing import List
from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []
        p_count = Counter(p)
        window = Counter()
        res = []
        left = 0
        for right in range(len(s)):
            window[s[right]] += 1
            if right - left + 1 > len(p):
                if window[s[left]] == 1:
                    del window[s[left]]
                else:
                    window[s[left]] -= 1
                left += 1
            if window == p_count:
                res.append(left)
        return res
