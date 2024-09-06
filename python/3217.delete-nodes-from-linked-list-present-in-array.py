# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional


class Solution:
    def modifiedList(
        self, nums: List[int], head: Optional[ListNode]
    ) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head

        nums = set(nums)
        prev_node = dummy
        while head:

            if head.val not in nums:
                prev_node = head
                head = head.next
                continue

            tmp = head.next
            prev_node.next = tmp
            head = tmp

        return dummy.next
