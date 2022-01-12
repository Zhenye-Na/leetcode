#
# @lc app=leetcode id=701 lang=python3
#
# [701] Insert into a Binary Search Tree
#
# https://leetcode.com/problems/insert-into-a-binary-search-tree/description/
#
# algorithms
# Medium (75.85%)
# Likes:    1487
# Dislikes: 96
# Total Accepted:    175.1K
# Total Submissions: 232.4K
# Testcase Example:  '[4,2,7,1,3]\n5'
#
# You are given the root node of a binary search tree (BST) and a value to
# insert into the tree. Return the root node of the BST after the insertion. It
# is guaranteed that the new value does not exist in the original BST.
# 
# Notice that there may exist multiple valid ways for the insertion, as long as
# the tree remains a BST after insertion. You can return any of them.
# 
# 
# Example 1:
# 
# 
# Input: root = [4,2,7,1,3], val = 5
# Output: [4,2,7,1,3,5]
# Explanation: Another accepted tree is:
# 
# 
# 
# Example 2:
# 
# 
# Input: root = [40,20,60,10,30,50,70], val = 25
# Output: [40,20,60,10,30,50,70,null,null,25]
# 
# 
# Example 3:
# 
# 
# Input: root = [4,2,7,1,3,null,null,null,null,null,null], val = 5
# Output: [4,2,7,1,3,5]
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the tree will be in the range [0, 10^4].
# -10^8 <= Node.val <= 10^8
# All the values Node.val are unique.
# -10^8 <= val <= 10^8
# It's guaranteed that val does not exist in the original BST.
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

# Runtime: 120 ms, faster than 99.77% of Python3 online submissions for Insert into a Binary Search Tree.
# Memory Usage: 16.9 MB, less than 21.89% of Python3 online submissions for Insert into a Binary Search Tree.

class Solution:
    def insertIntoBST_Iterative(self, root: TreeNode, val: int) -> TreeNode:
        if root is None:
            return TreeNode(val)

        node = root
        flag = 0
        while node:   
            if val < node.val:
                if node.left:
                    node = node.left
                else:
                    break
            else:
                if node.right:
                    node = node.right
                else:
                    flag = 1
                    break

        if flag:
            node.right = TreeNode(val)
        else:
            node.left = TreeNode(val)

        return root


    def insertIntoBST_Recursive_1(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)

        if val >= root.val:
            root.right = self.insertIntoBST(root.right, val)

        if val < root.val:
            root.left = self.insertIntoBST(root.left, val)

        return root

    def insertIntoBST_Recursive_2(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        self._insert(root, val)
        return root


    def _insert(self, root, val):
        if val >= root.val:
            if root.right:
                return self._insert(root.right, val)
            else:
                root.right = TreeNode(val)
        
        if val < root.val:
            if root.left:
                return self._insert(root.left, val)
            else:
                root.left = TreeNode(val)
# @lc code=end

