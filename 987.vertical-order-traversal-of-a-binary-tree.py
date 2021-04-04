#
# @lc app=leetcode id=987 lang=python3
#
# [987] Vertical Order Traversal of a Binary Tree
#
# https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/description/
#
# algorithms
# Medium (37.69%)
# Likes:    1345
# Dislikes: 2343
# Total Accepted:    131.6K
# Total Submissions: 338.5K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# Given the root of a binary tree, calculate the vertical order traversal of
# the binary tree.
# 
# For each node at position (row, col), its left and right children will be at
# positions (row + 1, col - 1) and (row + 1, col + 1) respectively. The root of
# the tree is at (0, 0).
# 
# The vertical order traversal of a binary tree is a list of top-to-bottom
# orderings for each column index starting from the leftmost column and ending
# on the rightmost column. There may be multiple nodes in the same row and same
# column. In such a case, sort these nodes by their values.
# 
# Return the vertical order traversal of the binary tree.
# 
# 
# Example 1:
# 
# 
# Input: root = [3,9,20,null,null,15,7]
# Output: [[9],[3,15],[20],[7]]
# Explanation:
# Column -1: Only node 9 is in this column.
# Column 0: Nodes 3 and 15 are in this column in that order from top to bottom.
# Column 1: Only node 20 is in this column.
# Column 2: Only node 7 is in this column.
# 
# Example 2:
# 
# 
# Input: root = [1,2,3,4,5,6,7]
# Output: [[4],[2],[1,5,6],[3],[7]]
# Explanation:
# Column -2: Only node 4 is in this column.
# Column -1: Only node 2 is in this column.
# Column 0: Nodes 1, 5, and 6 are in this column.
# ⁠         1 is at the top, so it comes first.
# ⁠         5 and 6 are at the same position (2, 0), so we order them by their
# value, 5 before 6.
# Column 1: Only node 3 is in this column.
# Column 2: Only node 7 is in this column.
# 
# 
# Example 3:
# 
# 
# Input: root = [1,2,3,4,6,5,7]
# Output: [[4],[2],[1,5,6],[3],[7]]
# Explanation:
# This case is the exact same as example 2, but with nodes 5 and 6 swapped.
# Note that the solution remains the same since 5 and 6 are in the same
# location and should be ordered by their values.
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the tree is in the range [1, 1000].
# 0 <= Node.val <= 1000
# 
# 
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict

class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        self.vals = collections.defaultdict(lambda: collections.defaultdict(list))
        self.dfs(root, 0, 0)
        return [[v for y in sorted(self.vals[x]) for v in sorted(self.vals[x][y])] for x in sorted(self.vals)]

    def dfs(self, node, x, y):
        if node: 
            self.vals[x][y].append(node.val)
            self.dfs(node.left, x - 1, y + 1)
            self.dfs(node.right, x + 1, y + 1)
# @lc code=end

