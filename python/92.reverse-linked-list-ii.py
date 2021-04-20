#
# @lc app=leetcode id=92 lang=python3
#
# [92] Reverse Linked List II
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if not head or n < m or m < 1:
            return head

        dummy = ListNode(0)
        dummy.next = head
        head = dummy

        count = 1
        prev, first = head, head.next
        while head.next and count < m:
            prev  = first
            first = first.next

            count += 1

        # first -> the m_th node in the LinkedList
        newLast  = first
        newFirst = prev

        switch = 0
        while switch <= n - m:
            tmp = first.next
            first.next = prev
            prev  = first
            first = tmp

            switch += 1

        newLast.next  = first
        newFirst.next = prev

        return dummy.next


