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



from collections import deque

class Solution_BFS:
    def isSymmetric(self, root: TreeNode) -> bool:
        depth = self.get_depth(root)
        queue = deque([root])
        curr_depth = 0

        while queue and curr_depth < depth:
            size = len(queue)
            level = []
            for _ in range(size):
                node = queue.popleft()
                if node is None:
                    level.append(".")
                else:
                    level.append(str(node.val))
                    queue.append(node.left)
                    queue.append(node.right)

            if level != level[::-1]:
                return False

            curr_depth += 1

        return True


    def get_depth(self, root):
        if not root:
            return 0
        
        left = self.get_depth(root.left)
        right = self.get_depth(root.right)
        
        return max(left, right) + 1
# @lc code=end

