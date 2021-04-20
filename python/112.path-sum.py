#
# @lc app=leetcode id=112 lang=python3
#
# [112] Path Sum
#
# https://leetcode.com/problems/path-sum/description/
#
# algorithms
# Easy (42.21%)
# Likes:    2919
# Dislikes: 591
# Total Accepted:    590.5K
# Total Submissions: 1.4M
# Testcase Example:  '[5,4,8,11,null,13,4,7,2,null,null,null,1]\n22'
#
# Given the root of a binary tree and an integer targetSum, return true if the
# tree has a root-to-leaf path such that adding up all the values along the
# path equals targetSum.
# 
# A leaf is a node with no children.
# 
# 
# Example 1:
# 
# 
# Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
# Output: true
# 
# 
# Example 2:
# 
# 
# Input: root = [1,2,3], targetSum = 5
# Output: false
# 
# 
# Example 3:
# 
# 
# Input: root = [1,2], targetSum = 0
# Output: false
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the tree is in the range [0, 5000].
# -1000 <= Node.val <= 1000
# -1000 <= targetSum <= 1000
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
    def __init__(self):
        self.res = False

    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        self._dfs(root, targetSum)
        return self.res

    def _dfs(self, root, target):
        if not root:
            return

        if not root.left and not root.right and target == root.val:
            self.res = True
            return

        if root.left:
            self._dfs(root.left, target - root.val)

        if root.right:
            self._dfs(root.right, target - root.val)
# @lc code=end

