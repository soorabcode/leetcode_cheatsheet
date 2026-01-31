# Day 47 
# Permutation in String 
# Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.
# In other words, return true if one of s1's permutations is the substring of s2.
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        from collections import Counter
        len1, len2 = len(s1), len(s2)
        if len1 > len2:
            return False
        count1 = Counter(s1)
        window = Counter(s2[:len1])
        if window == count1:
            return True
        for i in range(len1, len2):
            window[s2[i]] += 1
            window[s2[i - len1]] -= 1
            if window[s2[i - len1]] == 0:
                del window[s2[i - len1]]
            if window == count1:
                return True
        return False
