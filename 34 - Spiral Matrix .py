# Day 34
# Spiral Matrix
# Given an m x n matrix, return all elements of the matrix in spiral order.
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        while matrix:
            res += matrix.pop(0)
            matrix = list(zip(*matrix))[::-1]
        return res
