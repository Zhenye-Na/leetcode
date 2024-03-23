#
# @lc app=leetcode id=143 lang=python3
#
# [143] Reorder List
#
# https://leetcode.com/problems/reorder-list/description/
#
# algorithms
# Medium (42.58%)
# Likes:    4895
# Dislikes: 190
# Total Accepted:    415K
# Total Submissions: 908.2K
# Testcase Example:  '[1,2,3,4]'
#
# You are given the head of a singly linked-list. The list can be represented
# as:
# 
# 
# L0 → L1 → … → Ln - 1 → Ln
# 
# 
# Reorder the list to be on the following form:
# 
# 
# L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
# 
# 
# You may not modify the values in the list's nodes. Only nodes themselves may
# be changed.
# 
# 
# Example 1:
# 
# 
# Input: head = [1,2,3,4]
# Output: [1,4,2,3]
# 
# 
# Example 2:
# 
# 
# Input: head = [1,2,3,4,5]
# Output: [1,5,2,4,3]
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the list is in the range [1, 5 * 10^4].
# 1 <= Node.val <= 1000
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
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return head

        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        stack = []
        right = slow
        while right:
            stack.append(right)
            right = right.next

        left = head
        while left != slow and stack:
            tmp = left.next
            node = stack.pop()
            left.next = node
            node.next = tmp
            left = tmp

        if len(stack) != 0:
            node = stack.pop()
            left.next = node
            node.next = None

        else:
            left.next = None

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow, fast = head, head
        prev_slow = None
        while fast and fast.next:
            fast = fast.next.next
            prev_slow = slow
            slow = slow.next

        if slow == fast:
            return

        # middle node is slow
        prev_slow.next = None

        # reverse the right half
        right = self._reverse_linked_list(slow)
        left = head

        head = self._merge_linked_lists(left, right)

    def _merge_linked_lists(self, l1, l2):
        dummy = ListNode()
        current = dummy

        while l1 is not None and l2 is not None:
            # Attach node from the first list
            current.next = l1
            l1 = l1.next
            current = current.next

            # Attach node from the second list
            current.next = l2
            l2 = l2.next
            current = current.next

        # Attach remaining nodes from list 1 if any
        if l1 is not None:
            current.next = l1

        # Attach remaining nodes from list 2 if any
        if l2 is not None:
            current.next = l2

        return dummy.next


    def _reverse_linked_list(self, head):
        prev_node, curr = None, head

        while curr:
            next_node = curr.next
            curr.next = prev_node
            prev_node = curr
            curr = next_node

        return prev_node
# @lc code=end

