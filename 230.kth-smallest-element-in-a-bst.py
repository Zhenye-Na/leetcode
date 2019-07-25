#
# @lc app=leetcode id=230 lang=python3
#
# [230] Kth Smallest Element in a BST
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
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
