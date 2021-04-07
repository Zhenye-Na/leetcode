# [285] Inorder Successor in BST

# Description

# Given a binary search tree (See Definition) and a node in it,
# find the in-order successor of that node in the BST.

# If the given node has no in-order successor in the tree, return null.

# It's guaranteed p is one node in the given tree. (You can directly compare the memory address to find p)

# Example

# Example 1:

# Input: {1,#,2}, node with value 1
# Output: 2
# Explanation:
#   1
#    \
#     2

# Example 2:

# Input: {2,1,3}, node with value 1
# Output: 2
# Explanation: 
#     2
#    / \
#   1   3

# Challenge

# O(h), where h is the height of the BST.


"""
Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
"""

class Solution:
    """
    @param: root: The root of the BST.
    @param: p: You need find the successor node of p.
    @return: Successor of p.
    """
    def inorderSuccessor(self, root, p):
        if not root:
            return None

        if p.val >= root.val:
            return self.inorderSuccessor(root.right, p)

        left = self.inorderSuccessor(root.left, p)
        if left:
            return left
        return root



class Solution_Stack:
    """
    @param: root: The root of the BST.
    @param: p: You need find the successor node of p.
    @return: Successor of p.
    """
    def inorderSuccessor(self, root, p):
        # write your code here
        stack = []
        node = root
        while node:
            stack.append(node)
            node = node.left

        found = False
        while stack:
            node = stack.pop()
            if found:
                return node
            if node == p:
                found = True
            if node.right:
                node = node.right
                while node:
                    stack.append(node)
                    node = node.left

        return None

