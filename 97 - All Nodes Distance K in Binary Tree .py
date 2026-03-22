# Day 97 
# All Nodes Distance K in Binary Tree 
# Given the root of a binary tree, the value of a target node target, and an integer k, return an array of the values of all nodes that have a distance k from the target node.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
from typing import List

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        if not root:
            return []

        parent_map = {}
        def dfs(node, parent=None):
            if node:
                parent_map[node] = parent
                dfs(node.left, node)
                dfs(node.right, node)
        dfs(root)

        queue = deque([(target, 0)])
        visited = set([target])
        result = []

        while queue:
            node, dist = queue.popleft()
            if dist == k:
                result.append(node.val)
            elif dist < k:
                for neighbor in (node.left, node.right, parent_map[node]):
                    if neighbor and neighbor not in visited:
                        visited.add(neighbor)
                        queue.append((neighbor, dist + 1))
        return result