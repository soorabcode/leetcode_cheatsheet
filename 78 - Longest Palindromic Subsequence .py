# Day 78 
# Longest Palindromic Subsequence 
# Given a string s, find the longest palindromic subsequence's length in s.
# A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        t = s[::-1]
        n = len(s)

        prev = [0] * (n + 1)

        for i in range(1, n + 1):
            curr = [0] * (n + 1)
            for j in range(1, n + 1):
                if s[i - 1] == t[j - 1]:
                    curr[j] = 1 + prev[j - 1]
                else:
                    curr[j] = max(prev[j], curr[j - 1])
            prev = curr

        return prev[n]