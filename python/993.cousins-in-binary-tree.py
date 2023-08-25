#
# @lc app=leetcode id=993 lang=python3
#
# [993] Cousins in Binary Tree
#
# https://leetcode.com/problems/cousins-in-binary-tree/description/
#
# algorithms
# Easy (52.44%)
# Likes:    3711
# Dislikes: 178
# Total Accepted:    251.1K
# Total Submissions: 455.8K
# Testcase Example:  '[1,2,3,4]\n4\n3'
#
# Given the root of a binary tree with unique values and the values of two
# different nodes of the tree x and y, return true if the nodes corresponding
# to the values x and y in the tree are cousins, or false otherwise.
# 
# Two nodes of a binary tree are cousins if they have the same depth with
# different parents.
# 
# Note that in a binary tree, the root node is at the depth 0, and children of
# each depth k node are at the depth k + 1.
# 
# 
# Example 1:
# 
# 
# Input: root = [1,2,3,4], x = 4, y = 3
# Output: false
# 
# 
# Example 2:
# 
# 
# Input: root = [1,2,3,null,4,null,5], x = 5, y = 4
# Output: true
# 
# 
# Example 3:
# 
# 
# Input: root = [1,2,3,null,4], x = 2, y = 3
# Output: false
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the tree is in the range [2, 100].
# 1 <= Node.val <= 100
# Each node has a unique value.
# x != y
# x and y are exist in the tree.
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
    def __init__(self):
        self.height = {}
        self.parent = {}

    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        self.findDepth(root, 0, TreeNode())

        return self.height[x] == self.height[y] and self.parent[x] != self.parent[y]

    def findDepth(self, root, depth, parent):
        if not root:
            return

        self.height[root.val] = depth
        self.parent[root.val] = parent.val

        self.findDepth(root.left, depth + 1, root)
        self.findDepth(root.right, depth + 1, root)
# @lc code=end

