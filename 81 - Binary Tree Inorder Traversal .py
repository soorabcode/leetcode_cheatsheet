# Day 81
# Binary Tree Inorder Traversal 
# Given the root of a binary tree, return the inorder traversal of its nodes' values.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        def inorder(node):
            if not node:
                return
            
            inorder(node.left)     
            result.append(node.val) 
            inorder(node.right)             
        inorder(root)
        return result