#
# @lc app=leetcode id=101 lang=python3
#
# [101] Symmetric Tree
#
# https://leetcode.com/problems/symmetric-tree/description/
#
# algorithms
# Easy (47.93%)
# Likes:    5774
# Dislikes: 154
# Total Accepted:    845.4K
# Total Submissions: 1.8M
# Testcase Example:  '[1,2,2,3,4,4,3]'
#
# Given the root of a binary tree, check whether it is a mirror of itself
# (i.e., symmetric around its center).
# 
# 
# Example 1:
# 
# 
# Input: root = [1,2,2,3,4,4,3]
# Output: true
# 
# 
# Example 2:
# 
# 
# Input: root = [1,2,2,null,3,null,3]
# Output: false
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the tree is in the range [1, 1000].
# -100 <= Node.val <= 100
# 
# 
# 
# Follow up: Could you solve it both recursively and iteratively?
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution_DFS:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        return self._dfs(root.left, root.right)


    def _dfs(self, left_root, right_root):
        if not left_root and not right_root:
            return True

        if not left_root and right_root:
            return False

        if left_root and not right_root:
            return False

        if left_root and right_root and left_root.val != right_root.val:
            return False

        # pass the validation, check for the next level
        return self._dfs(left_root.left, right_root.right) and \
               self._dfs(left_root.right, right_root.left)



class Solution_BFS:
    def isSymmetric(self, root: TreeNode) -> bool:
        # Iteratively
        queue = deque([root])
        while queue:
            is_sym, end_flag = self._check_symmetric(list(queue)):
            if not is_sym:
                return False
            if end_flag:
                break
            size = len(queue)
            for _ in range(size):
                node = queue.popleft()
                if node:
                    queue.append(node.left)
                    queue.append(node.right)
                else:
                    queue.append(None)
                    queue.append(None)

        return True


    def _check_symmetric(self, node_lst):
        end_flag = True
        for node in node_list:
            if node is not None:
                end_flag = False
                break

        left, right = 0, len(node_lst) - 1
        while left <= right:
            if node_lst[left] is None and node_lst[right] is not None:
                return False, end_flag

            if node_lst[left] is not None and node_lst[right] is None:
                return False, end_flag

            if node_lst[left] is not None and \
                node_lst[right] is not None and \
                node_lst[left].val != node_lst[right].val:
                return False, end_flag

            left += 1
            right -= 1
        return True, end_flag
# @lc code=end

