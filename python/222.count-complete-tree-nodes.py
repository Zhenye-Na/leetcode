#
# @lc app=leetcode id=222 lang=python3
#
# [222] Count Complete Tree Nodes
#
# https://leetcode.com/problems/count-complete-tree-nodes/description/
#
# algorithms
# Medium (51.07%)
# Likes:    7942
# Dislikes: 437
# Total Accepted:    586.3K
# Total Submissions: 945.2K
# Testcase Example:  '[1,2,3,4,5,6]'
#
# Given the root of a complete binary tree, return the number of the nodes in
# the tree.
# 
# According to Wikipedia, every level, except possibly the last, is completely
# filled in a complete binary tree, and all nodes in the last level are as far
# left as possible. It can have between 1 and 2^h nodes inclusive at the last
# level h.
# 
# Design an algorithm that runs in less than O(n) time complexity.
# 
# 
# Example 1:
# 
# 
# Input: root = [1,2,3,4,5,6]
# Output: 6
# 
# 
# Example 2:
# 
# 
# Input: root = []
# Output: 0
# 
# 
# Example 3:
# 
# 
# Input: root = [1]
# Output: 1
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the tree is in the range [0, 5 * 10^4].
# 0 <= Node.val <= 5 * 10^4
# The tree is guaranteed to be complete.
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
class Solution_DivideAndConquer:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        return 1 + self.countNodes(root.left) + self.countNodes(root.right)


class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        l = self.getHeight(root.left)
        r = self.getHeight(root.right)

        if l == r:
            return 2 ** (l - 1) + self.countNodes(root.right)
        else:
            return 2 ** (r - 1) + self.countNodes(root.left)

    def getHeight(self, root):
        h = 1
        node = root
        while node:
            h += 1
            node = node.left

        return h
# @lc code=end

