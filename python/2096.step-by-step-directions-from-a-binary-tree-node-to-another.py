#
# @lc app=leetcode id=2096 lang=python3
#
# [2096] Step-By-Step Directions From a Binary Tree Node to Another
#
# https://leetcode.com/problems/step-by-step-directions-from-a-binary-tree-node-to-another/description/
#
# algorithms
# Medium (48.60%)
# Likes:    2386
# Dislikes: 124
# Total Accepted:    103.4K
# Total Submissions: 209.6K
# Testcase Example:  '[5,1,2,3,null,6,4]\n3\n6'
#
# You are given the root of a binary tree with n nodes. Each node is uniquely
# assigned a value from 1 to n. You are also given an integer startValue
# representing the value of the start node s, and a different integer destValue
# representing the value of the destination node t.
#
# Find the shortest path starting from node s and ending at node t. Generate
# step-by-step directions of such path as a string consisting of only the
# uppercase letters 'L', 'R', and 'U'. Each letter indicates a specific
# direction:
#
#
# 'L' means to go from a node to its left child node.
# 'R' means to go from a node to its right child node.
# 'U' means to go from a node to its parent node.
#
#
# Return the step-by-step directions of the shortest path from node s to node
# t.
#
#
# Example 1:
#
#
# Input: root = [5,1,2,3,null,6,4], startValue = 3, destValue = 6
# Output: "UURL"
# Explanation: The shortest path is: 3 → 1 → 5 → 2 → 6.
#
#
# Example 2:
#
#
# Input: root = [2,1], startValue = 2, destValue = 1
# Output: "L"
# Explanation: The shortest path is: 2 → 1.
#
#
#
# Constraints:
#
#
# The number of nodes in the tree is n.
# 2 <= n <= 10^5
# 1 <= Node.val <= n
# All the values in the tree are unique.
# 1 <= startValue, destValue <= n
# startValue != destValue
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

    def getDirections(
        self, root: Optional[TreeNode], startValue: int, destValue: int
    ) -> str:
        start_path, dest_path = [], []
        self.dfs(root, [], startValue, start_path)
        self.dfs(root, [], destValue, dest_path)

        start, dest = start_path[0], dest_path[0]

        # find LCA
        i = 0
        while i < len(start) and i < len(dest) and start[i] == dest[i]:
            i += 1

        return "U" * (len(start) - i) + dest[i:]

    def dfs(self, node, path, target, paths):
        if not node:
            return

        if node.val == target:
            paths.append("".join(path))

        path.append("L")
        self.dfs(node.left, path, target, paths)
        path.pop()

        path.append("R")
        self.dfs(node.right, path, target, paths)
        path.pop()


# @lc code=end
