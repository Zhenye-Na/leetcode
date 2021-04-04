#
# @lc app=leetcode id=687 lang=python3
#
# [687] Longest Univalue Path
#
# https://leetcode.com/problems/longest-univalue-path/description/
#
# algorithms
# Medium (37.14%)
# Likes:    2232
# Dislikes: 554
# Total Accepted:    112.1K
# Total Submissions: 299.2K
# Testcase Example:  '[5,4,5,1,1,5]'
#
# Given the root of a binary tree, return the length of the longest path, where
# each node in the path has the same value. This path may or may not pass
# through the root.
# 
# The length of the path between two nodes is represented by the number of
# edges between them.
# 
# 
# Example 1:
# 
# 
# Input: root = [5,4,5,1,1,5]
# Output: 2
# 
# 
# Example 2:
# 
# 
# Input: root = [1,4,5,4,4,5]
# Output: 2
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the tree is in the range [0, 10^4].
# -1000 <= Node.val <= 1000
# The depth of the tree will not exceed 1000.
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
    def longestUnivaluePath(self, root: TreeNode) -> int:
        self.max_length = 0
        self.dfs(root)
        return self.max_length - 1 if self.max_length != 0 else 0


    def dfs(self, root):
        if not root:
            return 0

        left = self.dfs(root.left)
        right = self.dfs(root.right)

        left_with_root = left + 1 if root.left and root.val == root.left.val else 1
        right_with_root = right + 1 if root.right and root.val == root.right.val else 1
        with_root = left + right + 1 if root.left and root.right and root.val == root.right.val and root.val == root.left.val else 1

        self.max_length = max(
            self.max_length,
            with_root,
            left_with_root,
            right_with_root
        )

        # current root can only select at most one child node
        return max(left_with_root, right_with_root, 1)
# @lc code=end

