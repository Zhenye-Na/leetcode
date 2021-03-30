#
# @lc app=leetcode id=173 lang=python3
#
# [173] Binary Search Tree Iterator
#
# https://leetcode.com/problems/binary-search-tree-iterator/description/
#
# algorithms
# Medium (59.75%)
# Likes:    3554
# Dislikes: 315
# Total Accepted:    396.6K
# Total Submissions: 655.6K
# Testcase Example:  '["BSTIterator","next","next","hasNext","next","hasNext","next","hasNext","next","hasNext"]\n' +
#   '[[[7,3,15,null,null,9,20]],[],[],[],[],[],[],[],[],[]]'
#
# Implement the BSTIterator class that represents an iterator over the in-order
# traversal of a binary search tree (BST):
# 
# 
# BSTIterator(TreeNode root) Initializes an object of the BSTIterator class.
# The root of the BST is given as part of the constructor. The pointer should
# be initialized to a non-existent number smaller than any element in the
# BST.
# boolean hasNext() Returns true if there exists a number in the traversal to
# the right of the pointer, otherwise returns false.
# int next() Moves the pointer to the right, then returns the number at the
# pointer.
# 
# 
# Notice that by initializing the pointer to a non-existent smallest number,
# the first call to next() will return the smallest element in the BST.
# 
# You may assume that next() calls will always be valid. That is, there will be
# at least a next number in the in-order traversal when next() is called.
# 
# 
# Example 1:
# 
# 
# Input
# ["BSTIterator", "next", "next", "hasNext", "next", "hasNext", "next",
# "hasNext", "next", "hasNext"]
# [[[7, 3, 15, null, null, 9, 20]], [], [], [], [], [], [], [], [], []]
# Output
# [null, 3, 7, true, 9, true, 15, true, 20, false]
# 
# Explanation
# BSTIterator bSTIterator = new BSTIterator([7, 3, 15, null, null, 9, 20]);
# bSTIterator.next();    // return 3
# bSTIterator.next();    // return 7
# bSTIterator.hasNext(); // return True
# bSTIterator.next();    // return 9
# bSTIterator.hasNext(); // return True
# bSTIterator.next();    // return 15
# bSTIterator.hasNext(); // return True
# bSTIterator.next();    // return 20
# bSTIterator.hasNext(); // return False
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the tree is in the range [1, 10^5].
# 0 <= Node.val <= 10^6
# At most 10^5 calls will be made to hasNext, and next.
# 
# 
# 
# Follow up:
# 
# 
# Could you implement next() and hasNext() to run in average O(1) time and use
# O(h) memory, where h is the height of the tree?
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
class BSTIterator:

    def __init__(self, root: TreeNode):
        self.root = root
        self.next_elem = None

        self.stack = []
        while root is not None:
            self.stack.append(root)
            root = root.left


    def next(self) -> int:
        if self.next_elem is None:
            self.hasNext()

        tmp, self.next_elem = self.next_elem, None
        return tmp


    def hasNext(self) -> bool:
        if self.next_elem is not None:
            return True

        # get next element
        if self.stack:
            node = self.stack.pop()
            self.next_elem = node.val

            # append node.right to stack and go the leftmost of it
            if node.right:
                node = node.right
                while node is not None:
                    self.stack.append(node)
                    node = node.left

            return True

        return False


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
# @lc code=end

