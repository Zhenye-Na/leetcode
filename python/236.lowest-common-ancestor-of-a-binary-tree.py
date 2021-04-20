#
# @lc app=leetcode id=236 lang=python3
#
# [236] Lowest Common Ancestor of a Binary Tree
#
# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/description/
#
# algorithms
# Medium (48.27%)
# Likes:    5369
# Dislikes: 201
# Total Accepted:    618.5K
# Total Submissions: 1.3M
# Testcase Example:  '[3,5,1,6,2,0,8,null,null,7,4]\n5\n1'
#
# Given a binary tree, find the lowest common ancestor (LCA) of two given nodes
# in the tree.
# 
# According to the definition of LCA on Wikipedia: “The lowest common ancestor
# is defined between two nodes p and q as the lowest node in T that has both p
# and q as descendants (where we allow a node to be a descendant of
# itself).”
# 
# 
# Example 1:
# 
# 
# Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
# Output: 3
# Explanation: The LCA of nodes 5 and 1 is 3.
# 
# 
# Example 2:
# 
# 
# Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
# Output: 5
# Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant
# of itself according to the LCA definition.
# 
# 
# Example 3:
# 
# 
# Input: root = [1,2], p = 1, q = 2
# Output: 1
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the tree is in the range [2, 10^5].
# -10^9 <= Node.val <= 10^9
# All Node.val are unique.
# p != q
# p and q will exist in the tree.
# 
# 
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        return self._find(root, p, q)


    def _find(self, root, p, q):
        if root is None or root == p or root == q:
            return root

        left_node = self._find(root.left, p, q)
        right_node = self._find(root.right, p, q)

        if right_node and not left_node:
            return right_node

        if left_node and not right_node:
            return left_node

        if left_node and right_node:
            return root

        return None
# @lc code=end

