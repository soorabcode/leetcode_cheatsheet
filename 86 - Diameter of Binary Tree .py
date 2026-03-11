# Day 86
# Diameter of Binary Tree
# Given the root of a binary tree, return the length of the diameter of the tree. 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0
        
        def height(node):
            if not node:
                return 0
            
            left = height(node.left)
            right = height(node.right)
            
            self.diameter = max(self.diameter, left + right)
            
            return 1 + max(left, right)
        
        height(root)
        return self.diameter