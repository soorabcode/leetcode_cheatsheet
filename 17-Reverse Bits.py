# Day 17
# Reverse Bits
# Reverse bits of a given 32 bits signed integer.

class Solution:
    def reverseBits(self, n: int) -> int:
        reversed_n = 0
        for _ in range(32):
            reversed_n = (reversed_n << 1) | (n & 1)
            n >>= 1
        return reversed_n