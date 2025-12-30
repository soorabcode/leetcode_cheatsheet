# Day 14 
# Problem : Number Of 1 Bits 
# Given a positive integer n, write a function that returns 
# the number of set bits in its binary representation
# (also known as the Hamming weight). 

# Solution : 
# count = count + n&1 
# Loop The Above 


class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            count += n & 1
            n >>= 1
        return count