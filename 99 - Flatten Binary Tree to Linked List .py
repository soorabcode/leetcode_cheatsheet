 # Day 99 
 # Flatten Binary Tree to Linked List
 # Given the root of a binary tree, flatten the tree into a "linked list":
 # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        curr = root
        
        while curr:
            if curr.left:
                prev = curr.left
                while prev.right:
                    prev = prev.right
                
                prev.right = curr.right
                
                curr.right = curr.left
                curr.left = None
            
            curr = curr.right