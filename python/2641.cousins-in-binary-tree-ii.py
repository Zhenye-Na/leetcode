#
# @lc app=leetcode id=2641 lang=python3
#
# [2641] Cousins in Binary Tree II
#
# https://leetcode.com/problems/cousins-in-binary-tree-ii/description/
#
# algorithms
# Medium (67.61%)
# Likes:    473
# Dislikes: 7
# Total Accepted:    15.1K
# Total Submissions: 22.3K
# Testcase Example:  '[5,4,9,1,10,null,7]'
#
# Given the root of a binary tree, replace the value of each node in the tree
# with the sum of all its cousins' values.
# 
# Two nodes of a binary tree are cousins if they have the same depth with
# different parents.
# 
# Return the root of the modified tree.
# 
# Note that the depth of a node is the number of edges in the path from the
# root node to it.
# 
# 
# Example 1:
# 
# 
# Input: root = [5,4,9,1,10,null,7]
# Output: [0,0,0,7,7,null,11]
# Explanation: The diagram above shows the initial binary tree and the binary
# tree after changing the value of each node.
# - Node with value 5 does not have any cousins so its sum is 0.
# - Node with value 4 does not have any cousins so its sum is 0.
# - Node with value 9 does not have any cousins so its sum is 0.
# - Node with value 1 has a cousin with value 7 so its sum is 7.
# - Node with value 10 has a cousin with value 7 so its sum is 7.
# - Node with value 7 has cousins with values 1 and 10 so its sum is 11.
# 
# 
# Example 2:
# 
# 
# Input: root = [3,1,2]
# Output: [0,0,0]
# Explanation: The diagram above shows the initial binary tree and the binary
# tree after changing the value of each node.
# - Node with value 3 does not have any cousins so its sum is 0.
# - Node with value 1 does not have any cousins so its sum is 0.
# - Node with value 2 does not have any cousins so its sum is 0.
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the tree is in the range [1, 10^5].
# 1 <= Node.val <= 10^4
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
    def __init__(self):
        self.total = defaultdict(int)
        self.value = {}

    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.findTotal(root, 0)
        self.substractSibling(root, None, 0)

        return root

    def substractSibling(self, node, parent, height):
        if not node:
            return

        total = self.total[height]
        if not parent:
            node.val = 0
        elif parent.left == node and parent.right:
            node.val = total - self.value[parent.right]- self.value[node]
        elif parent.right == node and parent.left:
            node.val = total - self.value[parent.left] - self.value[node]
        else:
            node.val = total - self.value[node]

        self.substractSibling(node.left, node, height + 1)
        self.substractSibling(node.right, node, height + 1)

    def findTotal(self, node, height):
        if not node:
            return

        self.total[height] += node.val
        self.value[node] = node.val

        self.findTotal(node.left, height + 1)
        self.findTotal(node.right, height + 1)
# @lc code=end

