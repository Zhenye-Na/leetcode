#
# @lc app=leetcode id=108 lang=python3
#
# [108] Convert Sorted Array to Binary Search Tree
#
# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/description/
#
# algorithms
# Easy (60.07%)
# Likes:    3685
# Dislikes: 269
# Total Accepted:    518.1K
# Total Submissions: 851.2K
# Testcase Example:  '[-10,-3,0,5,9]'
#
# Given an integer array nums where the elements are sorted in ascending order,
# convert it to a height-balanced binary search tree.
# 
# A height-balanced binary tree is a binary tree in which the depth of the two
# subtrees of every node never differs by more than one.
# 
# 
# Example 1:
# 
# 
# Input: nums = [-10,-3,0,5,9]
# Output: [0,-3,9,-10,null,5]
# Explanation: [0,-10,5,null,-3,null,9] is also accepted:
# 
# 
# 
# Example 2:
# 
# 
# Input: nums = [1,3]
# Output: [3,1]
# Explanation: [1,3] and [3,1] are both a height-balanced BSTs.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 10^4
# -10^4 <= nums[i] <= 10^4
# nums is sorted in a strictly increasing order.
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
class Solution_WithHelper:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        return self.create_bst(nums)


    def create_bst(self, nums):
        if not nums or len(nums) == 0:
            return None

        mid = len(nums) // 2
        root = TreeNode(nums[mid])

        left = self.create_bst(nums[:mid])
        right  = self.create_bst(nums[mid + 1:])

        root.left = left
        root.right = right

        return root


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums or len(nums) == 0:
            return None
        
        if len(nums) == 1:
            return TreeNode(nums[0])
        
        n = len(nums)
        root = TreeNode(nums[n // 2])
        left = self.sortedArrayToBST(nums[: n// 2])
        right = self.sortedArrayToBST(nums[n // 2 + 1:])
        
        root.left = left
        root.right = right
        return root
# @lc code=end

