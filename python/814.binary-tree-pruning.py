#
# @lc app=leetcode id=814 lang=python3
#
# [814] Binary Tree Pruning
#
# https://leetcode.com/problems/binary-tree-pruning/description/
#
# algorithms
# Medium (71.62%)
# Likes:    1882
# Dislikes: 61
# Total Accepted:    114.4K
# Total Submissions: 160K
# Testcase Example:  '[1,null,0,0,1]'
#
# Given the root of a binary tree, return the same tree where every subtree (of
# the given tree) not containing a 1 has been removed.
# 
# A subtree of a node node is node plus every node that is a descendant of
# node.
# 
# 
# Example 1:
# 
# 
# Input: root = [1,null,0,0,1]
# Output: [1,null,0,null,1]
# Explanation: 
# Only the red nodes satisfy the property "every subtree not containing a 1".
# The diagram on the right represents the answer.
# 
# 
# Example 2:
# 
# 
# Input: root = [1,0,1,0,0,0,1]
# Output: [1,null,1,null,1]
# 
# 
# Example 3:
# 
# 
# Input: root = [1,1,0,1,1,0,1,0]
# Output: [1,1,0,1,1,null,1]
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the tree is in the range [1, 200].
# Node.val is either 0 or 1.
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
    def pruneTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return root
        
        res = self.helper(root)
        if res:
            return None
        return root
        
        
    def helper(self, root):
        if not root:
            return True
        
        left = self.helper(root.left)
        right = self.helper(root.right)
    
        if left:
            root.left = None
            
        if right:
            root.right = None
    
        if left and right and root.val == 0:
            return True
    
        return False
# @lc code=end

