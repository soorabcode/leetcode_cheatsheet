# day 67 
# 60. Permutation Sequence
# Given n and k, return the kth permutation sequence.

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        numbers = [str(i) for i in range(1, n + 1)]
        k -= 1  # convert to 0-based index
        result = []

        for i in range(n, 0, -1):
            fact = factorial(i - 1)
            index = k // fact
            result.append(numbers[index])
            numbers.pop(index)
            k %= fact

        return ''.join(result)