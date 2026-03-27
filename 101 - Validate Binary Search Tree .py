# Day 101 
# Validate Binary Search Tree 
# Given the root of a binary tree, determine if it is a valid binary search tree (BST).
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.prev = float('-inf')
        
        def inorder(node):
            if not node:
                return True
            
            if not inorder(node.left):
                return False
            
            if node.val <= self.prev:
                return False
            
            self.prev = node.val
            
            return inorder(node.right)
        
        return inorder(root)