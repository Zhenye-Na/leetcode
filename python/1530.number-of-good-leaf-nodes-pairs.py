#
# @lc app=leetcode id=1530 lang=python3
#
# [1530] Number of Good Leaf Nodes Pairs
#
# https://leetcode.com/problems/number-of-good-leaf-nodes-pairs/description/
#
# algorithms
# Medium (61.49%)
# Likes:    1907
# Dislikes: 64
# Total Accepted:    64.6K
# Total Submissions: 97.3K
# Testcase Example:  '[1,2,3,null,4]\n3'
#
# You are given the root of a binary tree and an integer distance. A pair of
# two different leaf nodes of a binary tree is said to be good if the length of
# the shortest path between them is less than or equal to distance.
#
# Return the number of good leaf node pairs in the tree.
#
#
# Example 1:
#
#
# Input: root = [1,2,3,null,4], distance = 3
# Output: 1
# Explanation: The leaf nodes of the tree are 3 and 4 and the length of the
# shortest path between them is 3. This is the only good pair.
#
#
# Example 2:
#
#
# Input: root = [1,2,3,4,5,6,7], distance = 3
# Output: 2
# Explanation: The good pairs are [4,5] and [6,7] with shortest path = 2. The
# pair [4,6] is not good because the length of ther shortest path between them
# is 4.
#
#
# Example 3:
#
#
# Input: root = [7,1,4,6,null,5,3,null,null,null,null,null,2], distance = 3
# Output: 1
# Explanation: The only good pair is [2,5].
#
#
#
# Constraints:
#
#
# The number of nodes in the tree is in the range [1, 2^10].
# 1 <= Node.val <= 100
# 1 <= distance <= 10
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
    def __init__(self):
        self.res = 0

    def countPairs(self, root: TreeNode, distance: int) -> int:
        self.dfs(root, distance)
        return self.res

    def dfs(self, node: TreeNode, distance: int) -> list:
        if not node:
            return []

        if not node.left and not node.right:
            return [1]

        left_distances = self.dfs(node.left, distance)
        right_distances = self.dfs(node.right, distance)

        for ld in left_distances:
            for rd in right_distances:
                if ld + rd <= distance:
                    self.res += 1

        return [d + 1 for d in left_distances + right_distances]


# @lc code=end
