#
# @lc app=leetcode id=230 lang=python3
#
# [230] Kth Smallest Element in a BST
#
# https://leetcode.com/problems/kth-smallest-element-in-a-bst/description/
#
# algorithms
# Medium (53.80%)
# Likes:    1443
# Dislikes: 46
# Total Accepted:    263.7K
# Total Submissions: 490.2K
# Testcase Example:  '[3,1,4,null,2]\n1'
#
# Given a binary search tree, write a function kthSmallest to find the kth
# smallest element in it.
# 
# Note: 
# You may assume k is always valid, 1 ≤ k ≤ BST's total elements.
# 
# Example 1:
# 
# 
# Input: root = [3,1,4,null,2], k = 1
# ⁠  3
# ⁠ / \
# ⁠1   4
# ⁠ \
#   2
# Output: 1
# 
# Example 2:
# 
# 
# Input: root = [5,3,6,2,4,null,null,1], k = 3
# ⁠      5
# ⁠     / \
# ⁠    3   6
# ⁠   / \
# ⁠  2   4
# ⁠ /
# ⁠1
# Output: 3
# 
# 
# Follow up:
# What if the BST is modified (insert/delete operations) often and you need to
# find the kth smallest frequently? How would you optimize the kthSmallest
# routine?
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
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        stack = []
        curr = root
        while curr:
            stack.append(curr)
            curr = curr.left

        for _ in range(k - 1):
            node = stack.pop()
            if node.right:
                node = node.right
                while node:
                    stack.append(node)
                    node = node.left

        return stack[-1].val


class Solution_QuickSelect:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self.numChildren = {}
        self._count_children(root)
        return self.quick_select_K(root, k)


    def _count_children(self, root):
        if root is None:
            return 0

        left = self._count_children(root.left)
        right = self._count_children(root.right)

        self.numChildren[root] = left + right + 1
        return left + right + 1


    def quick_select_K(self, root, k):
        if root is None:
            return 

        left = 0
        if root.left:
            left = self.numChildren[root.left]

        if left >= k:
            return self.quick_select_K(root.left, k)
        elif left == k - 1:
            return root.val
        else:
            return self.quick_select_K(root.right, k - left - 1)
# @lc code=end

