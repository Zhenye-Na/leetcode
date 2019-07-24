#
# @lc app=leetcode id=987 lang=python3
#
# [987] Vertical Order Traversal of a Binary Tree
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import defaultdict

class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        vals = collections.defaultdict(lambda: collections.defaultdict(list))
        def dfs(node, x, y):
            if node: 
                vals[x][y].append(node.val)
                dfs(node.left, x - 1, y + 1)
                dfs(node.right, x + 1, y + 1)

        dfs(root, 0, 0)
        return [[v for y in sorted(vals[x]) for v in sorted(vals[x][y])] for x in sorted(vals)]

