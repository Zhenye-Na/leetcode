#
# @lc app=leetcode id=234 lang=python3
#
# [234] Palindrome Linked List
#
# https://leetcode.com/problems/palindrome-linked-list/description/
#
# algorithms
# Easy (40.29%)
# Likes:    4998
# Dislikes: 432
# Total Accepted:    609.6K
# Total Submissions: 1.5M
# Testcase Example:  '[1,2,2,1]'
#
# Given the head of a singly linked list, return true if it is a palindrome.
# 
# 
# Example 1:
# 
# 
# Input: head = [1,2,2,1]
# Output: true
# 
# 
# Example 2:
# 
# 
# Input: head = [1,2]
# Output: false
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the list is in the range [1, 10^5].
# 0 <= Node.val <= 9
# 
# 
# 
# Follow up: Could you do it in O(n) time and O(1) space?
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        prev_nodes = {}

        dummy = ListNode(0)
        dummy.next = head

        prev_node = dummy
        ptr = head

        while ptr:
            prev_nodes[ptr] = prev_node
            prev_node = ptr
            ptr = ptr.next

        right, length = head, 1
        while right and right.next:
            right = right.next
            length += 1

        left = head

        times = length // 2
        for _ in range(times):
            if left.val != right.val:
                return False

            left = left.next
            right = prev_nodes[right]

        return True
# @lc code=end

