#
# @lc app=leetcode id=148 lang=python3
#
# [148] Sort List
#
# https://leetcode.com/problems/sort-list/description/
#
# algorithms
# Medium (47.91%)
# Likes:    6220
# Dislikes: 210
# Total Accepted:    443.9K
# Total Submissions: 878.5K
# Testcase Example:  '[4,2,1,3]'
#
# Given the head of a linked list, return the list after sorting it in
# ascending order.
# 
# 
# Example 1:
# 
# 
# Input: head = [4,2,1,3]
# Output: [1,2,3,4]
# 
# 
# Example 2:
# 
# 
# Input: head = [-1,5,3,4,0]
# Output: [-1,0,3,4,5]
# 
# 
# Example 3:
# 
# 
# Input: head = []
# Output: []
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the list is in the range [0, 5 * 10^4].
# -10^5 <= Node.val <= 10^5
# 
# 
# 
# Follow up: Can you sort the linked list in O(n logn) time and O(1) memory
# (i.e. constant space)?
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        slow, fast = head, head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next

        mid = slow.next
        slow.next = None

        list1 = self.sortList(head)
        list2 = self.sortList(mid)
        return self.merge(list1,list2)

    
    def merge(self, list1, list2):
        if not list1:
            return list2
        if not list2:
            return list1

        head = None

        if list1.val < list2.val:
            head  = list1
            list1 = list1.next
        else:
            head  = list2
            list2 = list2.next

        tmp = head

        while list1 and list2:
            if list1.val < list2.val:
                tmp.next = list1
                tmp      = list1
                list1    = list1.next
            else:
                tmp.next = list2
                tmp      = list2
                list2    = list2.next

        if list1:
            tmp.next = list1
        if list2:
            tmp.next = list2

        return head
# @lc code=end

