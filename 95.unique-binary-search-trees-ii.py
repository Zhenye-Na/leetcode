#
# @lc app=leetcode id=95 lang=python3
#
# [95] Unique Binary Search Trees II
#
# https://leetcode.com/problems/unique-binary-search-trees-ii/description/
#
# algorithms
# Medium (42.19%)
# Likes:    2955
# Dislikes: 204
# Total Accepted:    225.6K
# Total Submissions: 525.1K
# Testcase Example:  '3'
#
# Given an integer n, return all the structurally unique BST's (binary search
# trees), which has exactly n nodes of unique values from 1 to n. Return the
# answer in any order.
# 
# 
# Example 1:
# 
# 
# Input: n = 3
# Output:
# [[1,null,2,null,3],[1,null,3,2],[2,1,3],[3,1,null,null,2],[3,2,null,1]]
# 
# 
# Example 2:
# 
# 
# Input: n = 1
# Output: [[1]]
# 
# 
# 
# Constraints:
# 
# 
# 1 <= n <= 8
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

from collections import defaultdict

class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        self.memo = defaultdict(list)
        return self.dfs(1, n)


    def dfs(self, start, end):
        if (start, end) in self.memo:
            return self.memo[(start, end)]

        if start == end:
            self.memo[(start, end)] = TreeNode(start)
            return [self.memo[(start, end)]]

        if start > end:
            return [None]

        res = []
        for root_val in range(start, end + 1):
            left = self.dfs(start, root_val - 1)
            self.memo[(start, root_val - 1)] = left

            right = self.dfs(root_val + 1, end)
            self.memo[(root_val + 1, end)] = right

            for left_subtree in left:
                for right_subtree in right:
                    root = TreeNode(root_val)
                    root.left = left_subtree
                    root.right = right_subtree

                    res.append(root)

        if not res:
            res = [None]

        self.memo[(start, end)] = res
        return res
# @lc code=end

