#
# @lc app=leetcode id=1448 lang=python3
#
# [1448] Count Good Nodes in Binary Tree
#
# https://leetcode.com/problems/count-good-nodes-in-binary-tree/description/
#
# algorithms
# Medium (72.08%)
# Likes:    1462
# Dislikes: 52
# Total Accepted:    102.9K
# Total Submissions: 141.1K
# Testcase Example:  '[3,1,4,3,null,1,5]'
#
# Given a binary tree root, a node X in the tree is named good if in the path
# from root to X there are no nodes with a value greater than X.
# 
# Return the number of good nodes in the binary tree.
# 
# 
# Example 1:
# 
# 
# 
# 
# Input: root = [3,1,4,3,null,1,5]
# Output: 4
# Explanation: Nodes in blue are good.
# Root Node (3) is always a good node.
# Node 4 -> (3,4) is the maximum value in the path starting from the root.
# Node 5 -> (3,4,5) is the maximum value in the path
# Node 3 -> (3,1,3) is the maximum value in the path.
# 
# Example 2:
# 
# 
# 
# 
# Input: root = [3,3,null,4,2]
# Output: 3
# Explanation: Node 2 -> (3, 3, 2) is not good, because "3" is higher than it.
# 
# Example 3:
# 
# 
# Input: root = [1]
# Output: 1
# Explanation: Root is considered as good.
# 
# 
# Constraints:
# 
# 
# The number of nodes in the binary tree is in the range [1, 10^5].
# Each node's value is between [-10^4, 10^4].
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
    def goodNodes(self, root: TreeNode) -> int:
        self.count = 0
        if not root:
            return self.count
        self.count += 1
        self.dfs(root, root.val)
        return self.count


    def dfs(self, root, curr_max):
        if root.left:
            self.dfs(root.left, max(curr_max, root.left.val))
            if curr_max <= root.left.val:
                self.count += 1

        if root.right:
            self.dfs(root.right, max(curr_max, root.right.val))
            if curr_max <= root.right.val:
                self.count += 1
# @lc code=end

