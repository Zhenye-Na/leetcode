#
# @lc app=leetcode id=897 lang=python3
#
# [897] Increasing Order Search Tree
#
# https://leetcode.com/problems/increasing-order-search-tree/description/
#
# algorithms
# Easy (75.15%)
# Likes:    2707
# Dislikes: 611
# Total Accepted:    185.2K
# Total Submissions: 239.9K
# Testcase Example:  '[5,3,6,2,4,null,8,1,null,null,null,7,9]'
#
# Given the root of a binary search tree, rearrange the tree in in-order so
# that the leftmost node in the tree is now the root of the tree, and every
# node has no left child and only one right child.
# 
# 
# Example 1:
# 
# 
# Input: root = [5,3,6,2,4,null,8,1,null,null,null,7,9]
# Output: [1,null,2,null,3,null,4,null,5,null,6,null,7,null,8,null,9]
# 
# 
# Example 2:
# 
# 
# Input: root = [5,1,7]
# Output: [1,null,5,null,7]
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the given tree will be in the range [1, 100].
# 0 <= Node.val <= 1000
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
    def increasingBST(self, root: TreeNode) -> TreeNode:
        
        dummy = TreeNode(-1)
        if not root:
            return dummy.right

        result = dummy
        # find the leftmost node
        stack = []
        while root:
            stack.append(root)
            root = root.left

        while stack:
            node = stack.pop()
            result.right = TreeNode(node.val)
            result = result.right

            if node.right:
                node = node.right
                while node:
                    stack.append(node)
                    node = node.left

        return dummy.right
# @lc code=end

