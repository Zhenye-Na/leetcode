#
# @lc app=leetcode id=1302 lang=python3
#
# [1302] Deepest Leaves Sum
#
# https://leetcode.com/problems/deepest-leaves-sum/description/
#
# algorithms
# Medium (84.10%)
# Likes:    1224
# Dislikes: 56
# Total Accepted:    97.2K
# Total Submissions: 114K
# Testcase Example:  '[1,2,3,4,5,null,6,7,null,null,null,null,8]'
#
# Given the root of a binary tree, return the sum of values of its deepest
# leaves.
# 
# Example 1:
# 
# 
# Input: root = [1,2,3,4,5,null,6,7,null,null,null,null,8]
# Output: 15
# 
# 
# Example 2:
# 
# 
# Input: root = [6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]
# Output: 19
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the tree is in the range [1, 10^4].
# 1 <= Node.val <= 100
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
from collections import deque

class Solution:

    def deepestLeavesSum(self, root: TreeNode) -> int:
        depth = self.get_depth(root)

        queue = deque([root])
        res = 0
        curr_depth = 1

        while queue:
            size = len(queue)
            for _ in range(size):
                node = queue.popleft()
                if curr_depth == depth:
                    res += node.val

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)  

            curr_depth += 1

        return res


    def get_depth(self, root):
        if not root:
            return 0

        left = self.get_depth(root.left)
        right = self.get_depth(root.right)

        return max(left, right) + 1
# @lc code=end

