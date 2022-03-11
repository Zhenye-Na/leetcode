#
# @lc app=leetcode id=61 lang=python3
#
# [61] Rotate List
#
# https://leetcode.com/problems/rotate-list/description/
#
# algorithms
# Medium (32.51%)
# Likes:    4380
# Dislikes: 1250
# Total Accepted:    502.2K
# Total Submissions: 1.5M
# Testcase Example:  '[1,2,3,4,5]\n2'
#
# Given the head of a linked list, rotate the list to the right by k places.
# 
# 
# Example 1:
# 
# 
# Input: head = [1,2,3,4,5], k = 2
# Output: [4,5,1,2,3]
# 
# 
# Example 2:
# 
# 
# Input: head = [0,1,2], k = 4
# Output: [2,0,1]
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the list is in the range [0, 500].
# -100 <= Node.val <= 100
# 0 <= k <= 2 * 10^9
# 
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head

        length = self.get_length(head)
        k = k % length
        
        if k == 0:
            return head

        dummy = ListNode(0)
        dummy.next = head
        pointer = dummy
        for _ in range(length - k):
            pointer = pointer.next

        new_head = pointer.next
        new_end = pointer
        while new_end.next:
            new_end = new_end.next

        pointer.next = None
        new_end.next = dummy.next
        
        return new_head

    def get_length(self, head):
        length = 0
        while head:
            head = head.next
            length += 1

        return length
# @lc code=end

