# day 66
# Combination Sum III 
# Find all valid combinations of k numbers that sum up to n such that the following conditions are true:
# Only numbers 1 through 9 are used.
# Each number is used at most once.
# Return a list of all possible valid combinations. The list must not contain the same combination twice, and the combinations may be returned in any order.
from typing import List

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result = []

        def backtrack(start, k, remaining, path):
            if k == 0 and remaining == 0:
                result.append(path[:])
                return
            
            if k == 0 or remaining < 0:
                return
            
            for i in range(start, 10):  
                if i > remaining:
                    break
                backtrack(i + 1, k - 1, remaining - i, path + [i])

        backtrack(1, k, n, [])
        return result
