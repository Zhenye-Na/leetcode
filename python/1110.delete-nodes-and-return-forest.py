#
# @lc app=leetcode id=1110 lang=python3
#
# [1110] Delete Nodes And Return Forest
#
# https://leetcode.com/problems/delete-nodes-and-return-forest/description/
#
# algorithms
# Medium (69.18%)
# Likes:    4128
# Dislikes: 121
# Total Accepted:    256.3K
# Total Submissions: 365.3K
# Testcase Example:  '[1,2,3,4,5,6,7]\n[3,5]'
#
# Given the root of a binary tree, each node in the tree has a distinct value.
#
# After deleting all nodes with a value in to_delete, we are left with a forest
# (a disjoint union of trees).
#
# Return the roots of the trees in the remaining forest. You may return the
# result in any order.
#
#
# Example 1:
#
#
# Input: root = [1,2,3,4,5,6,7], to_delete = [3,5]
# Output: [[1,2,null,4],[6],[7]]
#
#
# Example 2:
#
#
# Input: root = [1,2,4,null,3], to_delete = [3]
# Output: [[1,2,4]]
#
#
#
# Constraints:
#
#
# The number of nodes in the given tree is at most 1000.
# Each node has a distinct value between 1 and 1000.
# to_delete.length <= 1000
# to_delete contains distinct values between 1 and 1000.
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
        self.forest = []
        self.to_delete_set = set()

    def delNodes(
        self, root: Optional[TreeNode], to_delete: List[int]
    ) -> List[TreeNode]:
        self.to_delete_set = set(to_delete)
        self.dfs(root, True)
        return self.forest

    def dfs(self, node: Optional[TreeNode], is_root: bool) -> Optional[TreeNode]:
        if not node:
            return None

        is_deleted = node.val in self.to_delete_set

        if is_root and not is_deleted:
            self.forest.append(node)

        node.left = self.dfs(node.left, is_deleted)
        node.right = self.dfs(node.right, is_deleted)

        return None if is_deleted else node


# @lc code=end
