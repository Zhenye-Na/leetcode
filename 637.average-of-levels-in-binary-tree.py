#
# @lc app=leetcode id=637 lang=python3
#
# [637] Average of Levels in Binary Tree
#
# https://leetcode.com/problems/average-of-levels-in-binary-tree/description/
#
# algorithms
# Easy (64.59%)
# Likes:    1926
# Dislikes: 201
# Total Accepted:    187.7K
# Total Submissions: 284.1K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# Given the root of a binary tree, return the average value of the nodes on
# each level in the form of an array. Answers within 10^-5 of the actual answer
# will be accepted.
# 
# Example 1:
# 
# 
# Input: root = [3,9,20,null,15,7]
# Output: [3.00000,14.50000,11.00000]
# Explanation: The average value of nodes on level 0 is 3, on level 1 is 14.5,
# and on level 2 is 11.
# Hence return [3, 14.5, 11].
# 
# 
# Example 2:
# 
# 
# Input: root = [3,9,20,15,7]
# Output: [3.00000,14.50000,11.00000]
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the tree is in the range [1, 10^4].
# -2^31 <= Node.val <= 2^31 - 1
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
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        if not root:
            return [0]

        queue = deque([root])
        res = []
        while queue:
            size = len(queue)
            level_total = 0
            for _ in range(size):
                node = queue.popleft()
                level_total += node.val

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            res.append(level_total / size)

        return res
# @lc code=end

