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
from collections import defaultdict, deque
from typing import Optional


class Solution_DFS:
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
            node.val = total - self.value[parent.right] - self.value[node]
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


class Solution_BFS:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root

        level_sum, original_values = self.calculateLevelSumAndStoreOriginalValues(root)
        self.updateNodeValues(root, level_sum, original_values)

        return root

    def calculateLevelSumAndStoreOriginalValues(self, root: TreeNode):
        """Performs the first BFS to calculate level sums and store the original values of the nodes."""
        level_sum = defaultdict(int)
        original_values = {}  # To store original values of nodes
        queue = deque([(root, 0)])  # (node, level)

        while queue:
            size = len(queue)
            running_total = 0

            for _ in range(size):
                node, level = queue.popleft()
                running_total += node.val
                original_values[node] = node.val  # Store original node value

                if node.left:
                    queue.append((node.left, level + 1))
                if node.right:
                    queue.append((node.right, level + 1))

            level_sum[level] = running_total  # Store sum for the current level

        return level_sum, original_values

    def updateNodeValues(
        self, root: TreeNode, level_sum: defaultdict, original_values: dict
    ):
        """Performs the second BFS to update node values using level sums and original values."""
        queue = deque([(root, None)])  # (node, parent)
        curr_level = 0

        while queue:
            size = len(queue)
            for _ in range(size):
                node, parent = queue.popleft()

                if not parent:
                    node.val = 0  # Root gets a value of 0
                else:
                    self.updateSingleNodeValue(
                        node, parent, level_sum, original_values, curr_level
                    )

                if node.left:
                    queue.append((node.left, node))
                if node.right:
                    queue.append((node.right, node))

            curr_level += 1

    def updateSingleNodeValue(
        self,
        node: TreeNode,
        parent: TreeNode,
        level_sum: defaultdict,
        original_values: dict,
        level: int,
    ):
        """Updates the value of a single node based on its parent and level information."""
        if node == parent.left and parent.right:
            node.val = (
                level_sum[level] - original_values[parent.right] - original_values[node]
            )
        elif node == parent.right and parent.left:
            node.val = (
                level_sum[level] - original_values[parent.left] - original_values[node]
            )
        else:
            node.val = level_sum[level] - original_values[node]


# @lc code=end
