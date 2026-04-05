# Day 109
# Flood Fill 
# You are given an image represented by an m x n grid of integers image, where image[i][j] represents the pixel value of the image. You are also given three integers sr, sc, and color. Your task is to perform a flood fill on the image starting from the pixel image[sr][sc].
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        original = image[sr][sc]
        
        if original == color:
            return image
        
        rows, cols = len(image), len(image[0])
        
        def dfs(r, c):
            if r < 0 or c < 0 or r >= rows or c >= cols:
                return
            
            if image[r][c] != original:
                return
            
            image[r][c] = color
            
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)
        
        dfs(sr, sc)
        return image