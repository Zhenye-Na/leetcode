#
# @lc app=leetcode id=86 lang=python3
#
# [86] Partition List
#
# https://leetcode.com/problems/partition-list/description/
#
# algorithms
# Medium (43.12%)
# Likes:    1981
# Dislikes: 384
# Total Accepted:    256.4K
# Total Submissions: 585.7K
# Testcase Example:  '[1,4,3,2,5,2]\n3'
#
# Given the head of a linked list and a value x, partition it such that all
# nodes less than x come before nodes greater than or equal to x.
# 
# You should preserve the original relative order of the nodes in each of the
# two partitions.
# 
# 
# Example 1:
# 
# 
# Input: head = [1,4,3,2,5,2], x = 3
# Output: [1,2,2,4,3,5]
# 
# 
# Example 2:
# 
# 
# Input: head = [2,1], x = 2
# Output: [1,2]
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the list is in the range [0, 200].
# -100 <= Node.val <= 100
# -200 <= x <= 200
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
    def partition(self, head: ListNode, x: int) -> ListNode:
        if not head:
            return head

        smaller_dummy = ListNode(0)
        greater_dummy = ListNode(0)
        smaller = smaller_dummy
        greater = greater_dummy

        node = head
        while node:
            if node.val < x:
                smaller.next = node
                smaller = smaller.next
            else:
                greater.next = node
                greater = greater.next

            node = node.next

        greater.next = None
        smaller.next = greater_dummy.next
        return smaller_dummy.next
# @lc code=end

