# Day 79 
# Ones and Zeroes
# You are given an array of binary strings strs and two integers m and n.
# Return the size of the largest subset of strs such that there are at most m 0's and n 1's in the subset.
# A set x is a subset of a set y if all elements of x are also elements of y.

class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        # dp[i][j] = max number of strings with i zeros and j ones
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        for s in strs:
            zeros = s.count('0')
            ones = s.count('1')
            for i in range(m, zeros - 1, -1):
                for j in range(n, ones - 1, -1):
                    dp[i][j] = max(
                        dp[i][j],
                        1 + dp[i - zeros][j - ones]
                    )
        
        return dp[m][n]