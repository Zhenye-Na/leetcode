#
# @lc app=leetcode id=82 lang=python3
#
# [82] Remove Duplicates from Sorted List II
#
# https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/description/
#
# algorithms
# Medium (39.04%)
# Likes:    2704
# Dislikes: 122
# Total Accepted:    317.3K
# Total Submissions: 807.9K
# Testcase Example:  '[1,2,3,3,4,4,5]'
#
# Given the head of a sorted linked list, delete all nodes that have duplicate
# numbers, leaving only distinct numbers from the original list. Return the
# linked list sorted as well.
# 
# 
# Example 1:
# 
# 
# Input: head = [1,2,3,3,4,4,5]
# Output: [1,2,5]
# 
# 
# Example 2:
# 
# 
# Input: head = [1,1,1,2,3]
# Output: [2,3]
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the list is in the range [0, 300].
# -100 <= Node.val <= 100
# The list is guaranteed to be sorted in ascending order.
# 
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Solution 1
#   In-place with set
#   Time Complexity: O(n)
#   Space Complexity: O(n)

class Solution1:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head or head.next is None:
            return head

        tmp = head
        counter = {}
        while tmp is not None:
            counter[tmp.val] = counter.get(tmp.val, 0) + 1
            tmp = tmp.next

        dummy = ListNode(-1)
        dummy.next = head
        tmp = head
        head = dummy
        while tmp is not None:
            if counter.get(tmp.val) > 1:
                tmp = tmp.next
            else:
                head.next = tmp
                tmp = tmp.next
                head = head.next

        head.next = None
        return dummy.next


# Solution 2
#   In-place with several pointers
#   Time Complexity: O(n)
#   Space Complexity: O(1)
class Solution2:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head or head.next is None:
            return head

        if head and head.next is None:
            return head

        # list with at least two nodes
        dummy = ListNode(-1)
        prev = ListNode(-1)
        dummy.next = head
        curr = dummy

        while head:
            print(head.val)
            if prev.val != head.val and ( (head.next and head.val != head.next.val) or head.next is None ):
                # ListNode `head` has different value from prev node and next node
                # value is unique
                curr.next = head
                curr = curr.next

            # update two pointers
            prev = head
            head = head.next

        if head:
            head.next = None

        return dummy.next


# @lc code=end

