#
# @lc app=leetcode id=129 lang=python3
#
# [129] Sum Root to Leaf Numbers
#
# https://leetcode.com/problems/sum-root-to-leaf-numbers/description/
#
# algorithms
# Medium (50.66%)
# Likes:    2199
# Dislikes: 58
# Total Accepted:    324.2K
# Total Submissions: 632.4K
# Testcase Example:  '[1,2,3]'
#
# You are given the root of a binary tree containing digits from 0 to 9 only.
# 
# Each root-to-leaf path in the tree represents a number.
# 
# 
# For example, the root-to-leaf path 1 -> 2 -> 3 represents the number 123.
# 
# 
# Return the total sum of all root-to-leaf numbers.
# 
# A leaf node is a node with no children.
# 
# 
# Example 1:
# 
# 
# Input: root = [1,2,3]
# Output: 25
# Explanation:
# The root-to-leaf path 1->2 represents the number 12.
# The root-to-leaf path 1->3 represents the number 13.
# Therefore, sum = 12 + 13 = 25.
# 
# 
# Example 2:
# 
# 
# Input: root = [4,9,0,5,1]
# Output: 1026
# Explanation:
# The root-to-leaf path 4->9->5 represents the number 495.
# The root-to-leaf path 4->9->1 represents the number 491.
# The root-to-leaf path 4->0 represents the number 40.
# Therefore, sum = 495 + 491 + 40 = 1026.
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the tree is in the range [1, 1000].
# 0 <= Node.val <= 9
# The depth of the tree will not exceed 10.
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
    def sumNumbers(self, root: TreeNode) -> int:
        self.paths = []
        self.get_all_paths(root, 0)
        return sum(self.paths)


    def get_all_paths(self, root, curr):
        if root.left is None and root.right is None:
            self.paths.append(curr * 10 + root.val)
            return

        if root.left:
            self.get_all_paths(root.left, curr * 10  + root.val)
        
        if root.right:
            self.get_all_paths(root.right, curr * 10 + root.val)
# @lc code=end

