#
# @lc app=leetcode id=110 lang=python3
#
# [110] Balanced Binary Tree
#
# https://leetcode.com/problems/balanced-binary-tree/description/
#
# algorithms
# Easy (44.61%)
# Likes:    3301
# Dislikes: 217
# Total Accepted:    550.2K
# Total Submissions: 1.2M
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# Given a binary tree, determine if it is height-balanced.
# 
# For this problem, a height-balanced binary tree is defined as:
# 
# 
# a binary tree in which the left and right subtrees of every node differ in
# height by no more than 1.
# 
# 
# 
# Example 1:
# 
# 
# Input: root = [3,9,20,null,null,15,7]
# Output: true
# 
# 
# Example 2:
# 
# 
# Input: root = [1,2,2,3,3,null,null,4,4]
# Output: false
# 
# 
# Example 3:
# 
# 
# Input: root = []
# Output: true
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the tree is in the range [0, 5000].
# -10^4 <= Node.val <= 10^4
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
    def isBalanced(self, root: TreeNode) -> bool:
        is_balance, _ = self._check(root)
        return is_balance


    def _check(self, root):
        """
        @params: root
        @return: is_balance, subtree_height
        """
        if not root:
            return True, 0

        if root.left:
            is_balance_left, left_height = self._check(root.left)
        else:
            is_balance_left, left_height = True, 0

        if root.right:
            is_balance_right, right_height = self._check(root.right)
        else:
            is_balance_right, right_height = True, 0

        # is either subtree is not balanced
        if not is_balance_left or not is_balance_right:
            return False, 0

        # if height diff is greater than 1
        if abs(left_height - right_height) > 1:
            return False, 0

        return True, max(left_height, right_height) + 1
# @lc code=end

