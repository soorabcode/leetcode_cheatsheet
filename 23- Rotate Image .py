# Day 23 
# 48. Rotate Image
# You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
# You have to rotate the image in-place, which means you have to 
# modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

        # Step 1: Transpose the matrix
        # Step 2: Reverse each row
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for i in range(n):
            matrix[i].reverse()
