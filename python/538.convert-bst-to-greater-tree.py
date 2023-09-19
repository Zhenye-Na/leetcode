#
# @lc app=leetcode id=538 lang=python3
#
# [538] Convert BST to Greater Tree
#
# https://leetcode.com/problems/convert-bst-to-greater-tree/description/
#
# algorithms
# Medium (56.64%)
# Likes:    2561
# Dislikes: 144
# Total Accepted:    163.3K
# Total Submissions: 273.4K
# Testcase Example:  '[4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]'
#
# Given the root of a Binary Search Tree (BST), convert it to a Greater Tree
# such that every key of the original BST is changed to the original key plus
# sum of all keys greater than the original key in BST.
# 
# As a reminder, a binary search tree is a tree that satisfies these
# constraints:
# 
# 
# The left subtree of a node contains only nodes with keys less than the node's
# key.
# The right subtree of a node contains only nodes with keys greater than the
# node's key.
# Both the left and right subtrees must also be binary search trees.
# 
# 
# Note: This question is the same as 1038:
# https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/
# 
# 
# Example 1:
# 
# 
# Input: root = [4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]
# Output: [30,36,21,36,35,26,15,null,null,null,33,null,null,null,8]
# 
# 
# Example 2:
# 
# 
# Input: root = [0,null,1]
# Output: [1,null,1]
# 
# 
# Example 3:
# 
# 
# Input: root = [1,0,2]
# Output: [3,3,2]
# 
# 
# Example 4:
# 
# 
# Input: root = [3,2,4,1]
# Output: [7,9,4,10]
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the tree is in the range [0, 10^4].
# -10^4 <= Node.val <= 10^4
# All the values in the tree are unique.
# root is guaranteed to be a valid binary search tree.
# 
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# DFS with global variable
class Solution:

    def __init__(self):
        self.greater = 0

    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        self.dfs(root)
        return root

    def dfs(self, node):
        if not node:
            return 0

        self.dfs(node.right)

        self.greater += node.val
        node.val = self.greater

        self.dfs(node.left)

        return node


# DFS without global variable
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        self.dfs(root, 0)
        return root

    def dfs(self, node, carry):
        if not node:
            return carry

        carry = self.dfs(node.right, carry)

        carry += node.val
        node.val = carry

        return self.dfs(node.left, carry)

# Stack
class Solution:

    def __init__(self):
        self.greater = 0

    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        stack = []
        node = root
        while node:
            stack.append(node)
            node = node.right

        while stack or node is not None:
            while node:
                stack.append(node)
                node = node.right

            node = stack.pop()

            self.greater += node.val
            node.val = self.greater

            node = node.left

        return root


# Construct a new tree
# Not in-place operation
class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        new_root, _ = self.convert(root, 0)
        return new_root

    def convert(self, root, incre):
        if not root:
            return root, incre

        right, right_max = self.convert(root.right, incre)
        new_root = TreeNode(root.val + right_max)
        left, left_max = self.convert(root.left, new_root.val)

        new_root.left = left
        new_root.right = right

        return new_root, left_max
# @lc code=end

