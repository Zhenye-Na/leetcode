#
# @lc app=leetcode id=105 lang=python3
#
# [105] Construct Binary Tree from Preorder and Inorder Traversal
#
# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/
#
# algorithms
# Medium (51.38%)
# Likes:    4990
# Dislikes: 128
# Total Accepted:    480K
# Total Submissions: 916.3K
# Testcase Example:  '[3,9,20,15,7]\n[9,3,15,20,7]'
#
# Given two integer arrays preorder and inorder where preorder is the preorder
# traversal of a binary tree and inorder is the inorder traversal of the same
# tree, construct and return the binary tree.
# 
# 
# Example 1:
# 
# 
# Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
# Output: [3,9,20,null,null,15,7]
# 
# 
# Example 2:
# 
# 
# Input: preorder = [-1], inorder = [-1]
# Output: [-1]
# 
# 
# 
# Constraints:
# 
# 
# 1 <= preorder.length <= 3000
# inorder.length == preorder.length
# -3000 <= preorder[i], inorder[i] <= 3000
# preorder and inorder consist of unique values.
# Each value of inorder also appears in preorder.
# preorder is guaranteed to be the preorder traversal of the tree.
# inorder is guaranteed to be the inorder traversal of the tree.
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
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        return self.constructTree(0, 0, len(inorder) - 1, preorder, inorder)


    def constructTree(self, pre_start, in_start, in_end, preorder, inorder):
        # exit
        if pre_start > len(preorder) or in_start > in_end:
            return None

        root = TreeNode(preorder[pre_start])
        in_index = inorder.index(preorder[pre_start])

        root.left = self.constructTree(pre_start + 1, in_start, in_index - 1, preorder, inorder)
        root.right = self.constructTree(pre_start + (in_index - in_start) + 1, in_index + 1, in_end, preorder, inorder)

        return root
# @lc code=end

