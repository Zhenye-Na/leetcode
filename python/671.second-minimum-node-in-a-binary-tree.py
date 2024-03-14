#
# @lc app=leetcode id=671 lang=python3
#
# [671] Second Minimum Node In a Binary Tree
#
# https://leetcode.com/problems/second-minimum-node-in-a-binary-tree/description/
#
# algorithms
# Easy (44.25%)
# Likes:    1809
# Dislikes: 1858
# Total Accepted:    187.5K
# Total Submissions: 421.8K
# Testcase Example:  '[2,2,5,null,null,5,7]'
#
# Given a non-empty special binary tree consisting of nodes with the
# non-negative value, where each node in this tree has exactly two or zero
# sub-node. If the node has two sub-nodes, then this node's value is the
# smaller value among its two sub-nodes. More formally, the property root.val =
# min(root.left.val, root.right.val) always holds.
# 
# Given such a binary tree, you need to output the second minimum value in the
# set made of all the nodes' value in the whole tree.
# 
# If no such second minimum value exists, output -1 instead.
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: root = [2,2,5,null,null,5,7]
# Output: 5
# Explanation: The smallest value is 2, the second smallest value is 5.
# 
# 
# Example 2:
# 
# 
# Input: root = [2,2,2]
# Output: -1
# Explanation: The smallest value is 2, but there isn't any second smallest
# value.
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the tree is in the range [1, 25].
# 1 <= Node.val <= 2^31 - 1
# root.val == min(root.left.val, root.right.val) for each internal node of the
# tree.
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
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        if not root:
            return -1

        root = self.replace_min(root, root.val)
        return self.find_min(root) if self.find_min(root) != float('inf') else -1

    def replace_min(self, root, value):
        if not root:
            return root

        if root.val == value:
            root.val = float('inf')
        
        self.replace_min(root.left, value)
        self.replace_min(root.right, value)
        return root

    def find_min(self, root):

        if not root:
            return float('inf')

        left = self.find_min(root.left)
        right = self.find_min(root.right)

        return min(left, root.val, right)
# @lc code=end

