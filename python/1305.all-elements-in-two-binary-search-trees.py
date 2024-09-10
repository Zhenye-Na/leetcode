#
# @lc app=leetcode id=1305 lang=python3
#
# [1305] All Elements in Two Binary Search Trees
#
# https://leetcode.com/problems/all-elements-in-two-binary-search-trees/description/
#
# algorithms
# Medium (79.84%)
# Likes:    3074
# Dislikes: 94
# Total Accepted:    223.5K
# Total Submissions: 279.9K
# Testcase Example:  '[2,1,4]\n[1,0,3]'
#
# Given two binary search trees root1 and root2, return a list containing all
# the integers from both trees sorted in ascending order.
#
#
# Example 1:
#
#
# Input: root1 = [2,1,4], root2 = [1,0,3]
# Output: [0,1,1,2,3,4]
#
#
# Example 2:
#
#
# Input: root1 = [1,null,8], root2 = [8,1]
# Output: [1,1,8,8]
#
#
#
# Constraints:
#
#
# The number of nodes in each tree is in the range [0, 5000].
# -10^5 <= Node.val <= 10^5
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
from typing import List


class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        vals1 = self._inorder_traversal(root1)
        vals2 = self._inorder_traversal(root2)

        q1, q2 = deque(vals1), deque(vals2)
        res = []
        while q1 and q2:
            if q1[0] < q2[0]:
                res.append(q1.popleft())
            elif q1[0] == q2[0]:
                res.append(q1.popleft())
                res.append(q2.popleft())
            else:
                res.append(q2.popleft())

        while q1:
            res.append(q1.popleft())

        while q2:
            res.append(q2.popleft())

        return res

    def _inorder_traversal(self, root):
        if not root:
            return []

        return (
            self._inorder_traversal(root.left)
            + [root.val]
            + self._inorder_traversal(root.right)
        )


# @lc code=end
