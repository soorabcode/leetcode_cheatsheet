# Day 82 
# Binary Tree Preorder Traversal 
# Given the root of a binary tree, return the preorder traversal of its nodes' values.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        def dfs(node):
            if not node:
                return
            
            result.append(node.val)
            dfs(node.left)      
            dfs(node.right)      

        dfs(root)
        return result