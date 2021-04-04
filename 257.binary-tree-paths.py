#
# @lc app=leetcode id=257 lang=python3
#
# [257] Binary Tree Paths
#
# https://leetcode.com/problems/binary-tree-paths/description/
#
# algorithms
# Easy (53.28%)
# Likes:    2482
# Dislikes: 129
# Total Accepted:    386.8K
# Total Submissions: 716.4K
# Testcase Example:  '[1,2,3,null,5]'
#
# Given the root of a binary tree, return all root-to-leaf paths in any order.
# 
# A leaf is a node with no children.
# 
# 
# Example 1:
# 
# 
# Input: root = [1,2,3,null,5]
# Output: ["1->2->5","1->3"]
# 
# 
# Example 2:
# 
# 
# Input: root = [1]
# Output: ["1"]
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the tree is in the range [1, 100].
# -100 <= Node.val <= 100
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
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        self.paths = []
        self.dfs(root, [])
        return self.paths

    def dfs(self, root, curr):
        # exit for dfs
        if root.left is None and root.right is None:
            curr_path = "->".join(curr[:] + [str(root.val)])
            self.paths.append(curr_path)
            return

        # dfs main logic
        if root.left:
            self.dfs(root.left, curr + [str(root.val)])
        if root.right:
            self.dfs(root.right, curr + [str(root.val)])
# @lc code=end

