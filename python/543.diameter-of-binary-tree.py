#
# @lc app=leetcode id=543 lang=python3
#
# [543] Diameter of Binary Tree
#
# https://leetcode.com/problems/diameter-of-binary-tree/description/
#
# algorithms
# Easy (49.08%)
# Likes:    4492
# Dislikes: 280
# Total Accepted:    456.6K
# Total Submissions: 924K
# Testcase Example:  '[1,2,3,4,5]'
#
# Given the root of a binary tree, return the length of the diameter of the
# tree.
# 
# The diameter of a binary tree is the length of the longest path between any
# two nodes in a tree. This path may or may not pass through the root.
# 
# The length of a path between two nodes is represented by the number of edges
# between them.
# 
# 
# Example 1:
# 
# 
# Input: root = [1,2,3,4,5]
# Output: 3
# Explanation: 3is the length of the path [4,2,1,3] or [5,2,1,3].
# 
# 
# Example 2:
# 
# 
# Input: root = [1,2]
# Output: 1
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the tree is in the range [1, 10^4].
# -100 <= Node.val <= 100
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
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.d = 0
        self.dfs(root)
        return max(self.d - 1, 0)


    def dfs(self, root):
        if not root:
            return 0

        left = self.dfs(root.left)
        right = self.dfs(root.right)

        self.d = max(
            self.d,
            left + right + 1
        )

        return max(left, right) + 1
# @lc code=end

