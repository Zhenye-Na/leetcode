#
# @lc app=leetcode id=25 lang=python3
#
# [25] Reverse Nodes in k-Group
#
# https://leetcode.com/problems/reverse-nodes-in-k-group/description/
#
# algorithms
# Hard (46.35%)
# Likes:    4377
# Dislikes: 423
# Total Accepted:    383.3K
# Total Submissions: 813.3K
# Testcase Example:  '[1,2,3,4,5]\n2'
#
# Given a linked list, reverse the nodes of a linked list k at a time and
# return its modified list.
# 
# k is a positive integer and is less than or equal to the length of the linked
# list. If the number of nodes is not a multiple of k then left-out nodes, in
# the end, should remain as it is.
# 
# You may not alter the values in the list's nodes, only nodes themselves may
# be changed.
# 
# 
# Example 1:
# 
# 
# Input: head = [1,2,3,4,5], k = 2
# Output: [2,1,4,3,5]
# 
# 
# Example 2:
# 
# 
# Input: head = [1,2,3,4,5], k = 3
# Output: [3,2,1,4,5]
# 
# 
# Example 3:
# 
# 
# Input: head = [1,2,3,4,5], k = 1
# Output: [1,2,3,4,5]
# 
# 
# Example 4:
# 
# 
# Input: head = [1], k = 1
# Output: [1]
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the list is in the range sz.
# 1 <= sz <= 5000
# 0 <= Node.val <= 1000
# 1 <= k <= sz
# 
# 
# 
# Follow-up: Can you solve the problem in O(1) extra memory space?
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return head

        dummy = ListNode(0, head)
        head = dummy

        while head:
            head = self._reverseK(head, k)

        return dummy.next

    def _reverseK(self, node, k):
        n1, nk = node.next, node
        for _ in range(k):
            nk = nk.next
            if nk is None:
                return nk

        nk_next = nk.next

        # reverse
        prev, curt = None, n1
        while curt != nk_next:
            tmp = curt.next
            curt.next = prev
            prev = curt
            curt = tmp

        # connect
        node.next = nk
        n1.next = nk_next

        return n1

# @lc code=end

