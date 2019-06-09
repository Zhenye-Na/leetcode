#
# @lc app=leetcode id=86 lang=python3
#
# [86] Partition List
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        if not head:
            return head

        small, large = ListNode(0), ListNode(0)

        s, l = small, large
        p = head
        while p:
            if p.val >= x:
                l.next = p
                l = l.next
            else:
                s.next = p
                s = s.next
            p = p.next

        l.next = None
        s.next = large.next

        return small.next

