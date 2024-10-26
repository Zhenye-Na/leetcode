#
# @lc app=leetcode id=2458 lang=python3
#
# [2458] Height of Binary Tree After Subtree Removal Queries
#
# https://leetcode.com/problems/height-of-binary-tree-after-subtree-removal-queries/description/
#
# algorithms
# Hard (41.37%)
# Likes:    931
# Dislikes: 22
# Total Accepted:    33.7K
# Total Submissions: 77.4K
# Testcase Example:  '[1,3,4,2,null,6,5,null,null,null,null,null,7]\n[4]'
#
# You are given the root of a binary tree with n nodes. Each node is assigned a
# unique value from 1 to n. You are also given an array queries of size m.
#
# You have to perform m independent queries on the tree where in the i^th query
# you do the following:
#
#
# Remove the subtree rooted at the node with the value queries[i] from the
# tree. It is guaranteed that queries[i] will not be equal to the value of the
# root.
#
#
# Return an array answer of size m where answer[i] is the height of the tree
# after performing the i^th query.
#
# Note:
#
#
# The queries are independent, so the tree returns to its initial state after
# each query.
# The height of a tree is the number of edges in the longest simple path from
# the root to some node in the tree.
#
#
#
# Example 1:
#
#
# Input: root = [1,3,4,2,null,6,5,null,null,null,null,null,7], queries = [4]
# Output: [2]
# Explanation: The diagram above shows the tree after removing the subtree
# rooted at node with value 4.
# The height of the tree is 2 (The path 1 -> 3 -> 2).
#
#
# Example 2:
#
#
# Input: root = [5,8,9,2,1,3,7,4,6], queries = [3,2,4,8]
# Output: [3,2,3,2]
# Explanation: We have the following queries:
# - Removing the subtree rooted at node with value 3. The height of the tree
# becomes 3 (The path 5 -> 8 -> 2 -> 4).
# - Removing the subtree rooted at node with value 2. The height of the tree
# becomes 2 (The path 5 -> 8 -> 1).
# - Removing the subtree rooted at node with value 4. The height of the tree
# becomes 3 (The path 5 -> 8 -> 2 -> 6).
# - Removing the subtree rooted at node with value 8. The height of the tree
# becomes 2 (The path 5 -> 9 -> 3).
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
# m == queries.length
# 1 <= m <= min(n, 10^4)
# 1 <= queries[i] <= n
# queries[i] != root.val
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
from typing import List, Optional


class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        # Dictionary to store height of each node
        height = {}
        # Dictionary to store max height possible when each node is removed
        height_without_node = defaultdict(int)

        # First calculate the height of each node
        self.calculate_height(root, height)

        # Compute maximum heights possible when each node is removed
        self.compute_max_heights(root, height, height_without_node, 0, 0)

        # Return results for each query
        return [height_without_node[q] for q in queries]

    def calculate_height(self, node: Optional[TreeNode], height: dict) -> int:
        if not node:
            return 0

        left_h = self.calculate_height(node.left, height)
        right_h = self.calculate_height(node.right, height)
        height[node] = max(left_h, right_h) + 1

        return height[node]

    def compute_max_heights(
        self,
        node: Optional[TreeNode],
        height: dict,
        height_without_node: dict,
        depth: int,
        max_height: int,
    ) -> None:
        if not node:
            return

        # Store the maximum height possible without current node
        height_without_node[node.val] = max_height

        # Process left child
        if node.left:
            # Max height is either from ancestor path or current depth + right subtree
            right_height = height.get(node.right, 0) if node.right else 0
            new_max = max(depth + right_height, max_height)
            self.compute_max_heights(
                node.left, height, height_without_node, depth + 1, new_max
            )

        # Process right child
        if node.right:
            # Max height is either from ancestor path or current depth + left subtree
            left_height = height.get(node.left, 0) if node.left else 0
            new_max = max(depth + left_height, max_height)
            self.compute_max_heights(
                node.right, height, height_without_node, depth + 1, new_max
            )


# @lc code=end
