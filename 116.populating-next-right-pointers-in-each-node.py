#
# @lc app=leetcode id=116 lang=python3
#
# [116] Populating Next Right Pointers in Each Node
#
# https://leetcode.com/problems/populating-next-right-pointers-in-each-node/description/
#
# algorithms
# Medium (48.63%)
# Likes:    3219
# Dislikes: 163
# Total Accepted:    475.2K
# Total Submissions: 959.3K
# Testcase Example:  '[1,2,3,4,5,6,7]'
#
# You are given a perfect binary tree where all leaves are on the same level,
# and every parent has two children. The binary tree has the following
# definition:
# 
# 
# struct Node {
# ⁠ int val;
# ⁠ Node *left;
# ⁠ Node *right;
# ⁠ Node *next;
# }
# 
# 
# Populate each next pointer to point to its next right node. If there is no
# next right node, the next pointer should be set to NULL.
# 
# Initially, all next pointers are set to NULL.
# 
# 
# 
# Follow up:
# 
# 
# You may only use constant extra space.
# Recursive approach is fine, you may assume implicit stack space does not
# count as extra space for this problem.
# 
# 
# 
# Example 1:
# 
# 
# 
# 
# Input: root = [1,2,3,4,5,6,7]
# Output: [1,#,2,3,#,4,5,6,7,#]
# Explanation: Given the above perfect binary tree (Figure A), your function
# should populate each next pointer to point to its next right node, just like
# in Figure B. The serialized output is in level order as connected by the next
# pointers, with '#' signifying the end of each level.
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the given tree is less than 4096.
# -1000 <= node.val <= 1000
# 
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        self._connect(root)
        return root
        
        
    def _connect(self, root):
        if not root or not root.left:
            return

        root.left.next = root.right
        
        if root.next:
            root.right.next = root.next.left
        
        self._connect(root.left)
        self._connect(root.right)

        return




from collections import deque

class Solution_BFS:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root

        queue = deque([root])

        while queue:
            size = len(queue)
            prev_node = None
            level = []

            for _ in range(size):

                node = queue.popleft()
                if prev_node is not None:
                    prev_node.next = node
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                prev_node = node

        return root
# @lc code=end

