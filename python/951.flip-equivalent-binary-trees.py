#
# @lc app=leetcode id=951 lang=python3
#
# [951] Flip Equivalent Binary Trees
#
# https://leetcode.com/problems/flip-equivalent-binary-trees/description/
#
# algorithms
# Medium (67.12%)
# Likes:    2328
# Dislikes: 96
# Total Accepted:    156.1K
# Total Submissions: 232.1K
# Testcase Example:  '[1,2,3,4,5,6,null,null,null,7,8]\n[1,3,2,null,6,4,5,null,null,null,null,8,7]'
#
# For a binary tree T, we can define a flip operation as follows: choose any
# node, and swap the left and right child subtrees.
#
# A binary tree X is flip equivalent to a binary tree Y if and only if we can
# make X equal to Y after some number of flip operations.
#
# Given the roots of two binary trees root1 and root2, return true if the two
# trees are flip equivalent or false otherwise.
#
#
# Example 1:
#
#
# Input: root1 = [1,2,3,4,5,6,null,null,null,7,8], root2 =
# [1,3,2,null,6,4,5,null,null,null,null,8,7]
# Output: true
# Explanation: We flipped at nodes with values 1, 3, and 5.
#
#
# Example 2:
#
#
# Input: root1 = [], root2 = []
# Output: true
#
#
# Example 3:
#
#
# Input: root1 = [], root2 = [1]
# Output: false
#
#
#
# Constraints:
#
#
# The number of nodes in each tree is in the range [0, 100].
# Each tree will have unique node values in the range [0, 99].
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
# Definition for a binary tree node.
from typing import Optional


class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:

        return self.check(root1, root2)

    def check(self, node1, node2):

        if not node1 and node2:
            return False

        if node1 and not node2:
            return False

        if not node1 and not node2:
            return True

        if node1.val == node2.val:
            return (
                self.check(node1.left, node2.left)
                and self.check(node1.right, node2.right)
            ) or (
                self.check(node1.left, node2.right)
                and self.check(node1.right, node2.left)
            )

        return False


# @lc code=end
