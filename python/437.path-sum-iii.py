#
# @lc app=leetcode id=437 lang=python3
#
# [437] Path Sum III
#
# https://leetcode.com/problems/path-sum-iii/description/
#
# algorithms
# Medium (47.13%)
# Likes:    11080
# Dislikes: 528
# Total Accepted:    610.6K
# Total Submissions: 1.3M
# Testcase Example:  '[10,5,-3,3,2,null,11,3,-2,null,1]\n8'
#
# Given the root of a binary tree and an integer targetSum, return the number
# of paths where the sum of the values along the path equals targetSum.
#
# The path does not need to start or end at the root or a leaf, but it must go
# downwards (i.e., traveling only from parent nodes to child nodes).
#
#
# Example 1:
#
#
# Input: root = [10,5,-3,3,2,null,11,3,-2,null,1], targetSum = 8
# Output: 3
# Explanation: The paths that sum to 8 are shown.
#
#
# Example 2:
#
#
# Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
# Output: 3
#
#
#
# Constraints:
#
#
# The number of nodes in the tree is in the range [0, 1000].
# -10^9 <= Node.val <= 10^9
# -1000 <= targetSum <= 1000
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
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def __init__(self):
        self.res = 0

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.target = targetSum
        self.dfs(root, [targetSum])

        return self.res

    def dfs(self, node, targets):
        if not node:
            return

        for target in targets:
            if node.val == target:
                self.res += 1

        next_targets = targets[:]
        for i in range(len(next_targets)):
            next_targets[i] -= node.val

        next_targets.append(self.target)

        self.dfs(node.left, next_targets)
        self.dfs(node.right, next_targets)


# @lc code=end
