# [298] Binary Tree Longest Consecutive Sequence

# Description

# Given a binary tree, find the length of the longest consecutive sequence path.

# The path refers to any sequence of nodes from some starting node to any node in
# the tree along the parent-child connections. The longest consecutive path need
# to be from parent to child (cannot be the reverse).

# Example


# Example 1:

# Input:
#    1
#     \
#      3
#     / \
#    2   4
#         \
#          5
# Output:3
# Explanation:
# Longest consecutive sequence path is 3-4-5, so return 3.


# Example 2:

# Input:
#    2
#     \
#      3
#     / 
#    2    
#   / 
#  1
# Output:2
# Explanation:
# Longest consecutive sequence path is 2-3,not 3-2-1, so return 2.


"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the root of binary tree
    @return: the length of the longest consecutive sequence path
    """
    def __init__(self):
        self.max_len = 0

    def longestConsecutive(self, root):
        # write your code here
        self.dfs(root)
        return self.max_len

    def dfs(self, root):
        if not root:
            return 0

        left = self.dfs(root.left)
        right = self.dfs(root.right)

        curr_length = 1
        if root.left and root.val + 1 == root.left.val:
            curr_length = max(curr_length, left + 1)
        if root.right and root.val + 1 == root.right.val:
            curr_length = max(curr_length, right + 1)

        self.max_len = max(
            self.max_len,
            curr_length
        )

        return curr_length



