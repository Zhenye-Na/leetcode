#
# @lc app=leetcode id=94 lang=python3
#
# [94] Binary Tree Inorder Traversal
#
# https://leetcode.com/problems/binary-tree-inorder-traversal/description/
#
# algorithms
# Medium (65.53%)
# Likes:    4402
# Dislikes: 193
# Total Accepted:    934.2K
# Total Submissions: 1.4M
# Testcase Example:  '[1,null,2,3]'
#
# Given the root of a binary tree, return the inorder traversal of its nodes'
# values.
# 
# 
# Example 1:
# 
# 
# Input: root = [1,null,2,3]
# Output: [1,3,2]
# 
# 
# Example 2:
# 
# 
# Input: root = []
# Output: []
# 
# 
# Example 3:
# 
# 
# Input: root = [1]
# Output: [1]
# 
# 
# Example 4:
# 
# 
# Input: root = [1,2]
# Output: [2,1]
# 
# 
# Example 5:
# 
# 
# Input: root = [1,null,2]
# Output: [1,2]
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the tree is in the range [0, 100].
# -100 <= Node.val <= 100
# 
# 
# 
# 
# Follow up:
# 
# Recursive solution is trivial, could you do it iteratively?
# 
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
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        result = []
        if not root:
            return result

        # find the leftmost node
        stack = []
        while root:
            stack.append(root)
            root = root.left

        while stack:
            node = stack.pop()
            result.append(node.val)

            if node.right:
                node = node.right
                while node:
                    stack.append(node)
                    node = node.left

        return result
# @lc code=end

