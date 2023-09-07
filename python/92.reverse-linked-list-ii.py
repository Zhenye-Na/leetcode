#
# @lc app=leetcode id=92 lang=python3
#
# [92] Reverse Linked List II
#
# https://leetcode.com/problems/reverse-linked-list-ii/description/
#
# algorithms
# Medium (41.18%)
# Likes:    3889
# Dislikes: 203
# Total Accepted:    362.8K
# Total Submissions: 879.6K
# Testcase Example:  '[1,2,3,4,5]\n2\n4'
#
# Given the head of a singly linked list and two integers left and right where
# left <= right, reverse the nodes of the list from position left to position
# right, and return the reversed list.
# 
# 
# Example 1:
# 
# 
# Input: head = [1,2,3,4,5], left = 2, right = 4
# Output: [1,4,3,2,5]
# 
# 
# Example 2:
# 
# 
# Input: head = [5], left = 1, right = 1
# Output: [5]
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the list is n.
# 1 <= n <= 500
# -500 <= Node.val <= 500
# 1 <= left <= right <= n
# 
# 
# 
# Follow up: Could you do it in one pass?
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        if not head or not head.next:
            return head

        dummy = ListNode(0)
        dummy.next = head
        head = dummy

        left_minus, left_node = head, head.next
        for _ in range(left - 1):
            left_node = left_node.next
            left_minus = left_minus.next

        right_node, right_plus = head, head.next
        for _ in range(right):
            right_node = right_node.next
            right_plus = right_plus.next   

        new_start, new_end = self.reverse(left_node, right_plus)
        left_minus.next = new_start
        new_end.next = right_plus

        return head.next



    def reverse(self, start, end):
        """
        n0 -> n1 -> n2, ..... nN  nN+1
              start               end
        
        =>                           curr
        n0 -> n1 <-  n2 ..... nN ->  nN+ 1
        """
        prev = None
        stop, curr = start, start
        while curr != end:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp

        return prev, stop

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        left_node, right_node = None, None
        left_left_node, right_right_node = None, None

        i = 1
        cursor = head
        while i < left:
            left_left_node = cursor
            cursor = cursor.next
            i += 1

        left_node = cursor

        prev_node, next_node = None, None
        while i <= right:

            next_node = cursor.next
            cursor.next = prev_node
            prev_node = cursor
            cursor = next_node

            i += 1

        right_node = prev_node
        right_right_node = cursor

        # stitch 3 pices together
        if left_left_node:
            left_left_node.next = right_node
        left_node.next = right_right_node

        return head if left_left_node else right_node
# @lc code=end

