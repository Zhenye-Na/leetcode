#
# @lc app=leetcode id=328 lang=python3
#
# [328] Odd Even Linked List
#
# https://leetcode.com/problems/odd-even-linked-list/description/
#
# algorithms
# Medium (57.82%)
# Likes:    4249
# Dislikes: 361
# Total Accepted:    455.3K
# Total Submissions: 776.6K
# Testcase Example:  '[1,2,3,4,5]'
#
# Given the head of a singly linked list, group all the nodes with odd indices
# together followed by the nodes with even indices, and return the reordered
# list.
# 
# The first node is considered odd, and the second node is even, and so on.
# 
# Note that the relative order inside both the even and odd groups should
# remain as it was in the input.
# 
# You must solve the problem in O(1) extra space complexity and O(n) time
# complexity.
# 
# 
# Example 1:
# 
# 
# Input: head = [1,2,3,4,5]
# Output: [1,3,5,2,4]
# 
# 
# Example 2:
# 
# 
# Input: head = [2,1,3,5,6,4,7]
# Output: [2,3,6,7,1,5,4]
# 
# 
# 
# Constraints:
# 
# 
# n == number of nodes in the linked list
# 0 <= n <= 10^4
# -10^6 <= Node.val <= 10^6
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
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        
        odd_pointer, even_pointer = head, head.next
        even_head = even_pointer
        
        while even_pointer and even_pointer.next:
            odd_pointer.next = even_pointer.next
            odd_pointer = odd_pointer.next

            even_pointer.next = odd_pointer.next
            even_pointer = even_pointer.next
            
        odd_pointer.next = even_head
        return head
# @lc code=end

