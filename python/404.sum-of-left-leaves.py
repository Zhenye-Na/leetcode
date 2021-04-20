#
# @lc app=leetcode id=404 lang=python3
#
# [404] Sum of Left Leaves
#
# https://leetcode.com/problems/sum-of-left-leaves/description/
#
# algorithms
# Easy (52.22%)
# Likes:    1719
# Dislikes: 165
# Total Accepted:    236.2K
# Total Submissions: 451.8K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# Find the sum of all left leaves in a given binary tree.
# 
# Example:
# 
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
# 
# There are two left leaves in the binary tree, with values 9 and 15
# respectively. Return 24.
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
class Solution_Queue:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if not root:
            return 0
        queue = deque([root])
        res = 0
        while queue:
            node = queue.popleft()
            if node.left is not None:
                if self._is_leaf(node.left):
                    res += node.left.val
                else:
                    queue.append(node.left)

            if node.right:
                queue.append(node.right)

        return res

    def _is_leaf(self, node):
        return node.left is None and node.right is None


class Solution_Recursive:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if not root:
            return 0

        res = 0
        if root.left:
            if self._is_leaf(root.left):
                res += root.left.val
            else:
                res += self.sumOfLeftLeaves(root.left)

        res += self.sumOfLeftLeaves(root.right)

        return res

    def _is_leaf(self, node):
        return node.left is None and node.right is None


# @lc code=end

