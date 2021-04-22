#
# @lc app=leetcode id=589 lang=python3
#
# [589] N-ary Tree Preorder Traversal
#
# https://leetcode.com/problems/n-ary-tree-preorder-traversal/description/
#
# algorithms
# Easy (73.16%)
# Likes:    986
# Dislikes: 64
# Total Accepted:    155.3K
# Total Submissions: 209.5K
# Testcase Example:  '[1,null,3,2,4,null,5,6]'
#
# Given the root of an n-ary tree, return the preorder traversal of its nodes'
# values.
# 
# Nary-Tree input serialization is represented in their level order traversal.
# Each group of children is separated by the null value (See examples)
# 
# 
# Example 1:
# 
# 
# 
# 
# Input: root = [1,null,3,2,4,null,5,6]
# Output: [1,3,5,6,2,4]
# 
# 
# Example 2:
# 
# 
# 
# 
# Input: root =
# [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
# Output: [1,2,3,6,7,11,14,4,8,12,5,9,13,10]
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the tree is in the range [0, 10^4].
# 0 <= Node.val <= 10^4
# The height of the n-ary tree is less than or equal to 1000.
# 
# 
# 
# Follow up: Recursive solution is trivial, could you do it iteratively?
# 
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        
        if not root.children:
            return [root.val]
        
        children_nodes = []
        for child in root.children:
            children_nodes.extend(self.preorder(child))
        
        return [root.val] + children_nodes
# @lc code=end

