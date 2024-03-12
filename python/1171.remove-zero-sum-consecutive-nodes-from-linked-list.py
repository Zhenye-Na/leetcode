#
# @lc app=leetcode id=1171 lang=python3
#
# [1171] Remove Zero Sum Consecutive Nodes from Linked List
#
# https://leetcode.com/problems/remove-zero-sum-consecutive-nodes-from-linked-list/description/
#
# algorithms
# Medium (43.31%)
# Likes:    2288
# Dislikes: 115
# Total Accepted:    61.5K
# Total Submissions: 136.3K
# Testcase Example:  '[1,2,-3,3,1]'
#
# Given the head of a linked list, we repeatedly delete consecutive sequences
# of nodes that sum to 0 until there are no such sequences.
# 
# After doing so, return the head of the final linked list.  You may return any
# such answer.
# 
# 
# (Note that in the examples below, all sequences are serializations of
# ListNode objects.)
# 
# Example 1:
# 
# 
# Input: head = [1,2,-3,3,1]
# Output: [3,1]
# Note: The answer [1,2,1] would also be accepted.
# 
# 
# Example 2:
# 
# 
# Input: head = [1,2,3,-3,4]
# Output: [1,2,4]
# 
# 
# Example 3:
# 
# 
# Input: head = [1,2,3,-3,-2]
# Output: [1]
# 
# 
# 
# Constraints:
# 
# 
# The given linked list will contain between 1 and 1000 nodes.
# Each node in the linked list has -1000 <= node.val <= 1000.
# 
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from collections import defaultdict

class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prefix_sum = 0
        seen = defaultdict(ListNode)
        dummy = ListNode(0)
        dummy.next = head
        curr = dummy

        while curr:
            prefix_sum += curr.val
            seen[prefix_sum] = curr
            curr = curr.next

        prefix_sum = 0
        curr = dummy

        while curr:
            prefix_sum += curr.val
            curr.next = seen[prefix_sum].next
            curr = curr.next

        return dummy.next
# @lc code=end

