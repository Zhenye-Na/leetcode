#
# @lc app=leetcode id=1669 lang=python3
#
# [1669] Merge In Between Linked Lists
#
# https://leetcode.com/problems/merge-in-between-linked-lists/description/
#
# algorithms
# Medium (73.04%)
# Likes:    1992
# Dislikes: 218
# Total Accepted:    195.7K
# Total Submissions: 241.2K
# Testcase Example:  '[10,1,13,6,9,5]\n3\n4\n[1000000,1000001,1000002]'
#
# You are given two linked lists: list1 and list2 of sizes n and m
# respectively.
# 
# Remove list1's nodes from the a^th node to the b^th node, and put list2 in
# their place.
# 
# The blue edges and nodes in the following figure indicate the result:
# 
# Build the result list and return its head.
# 
# 
# Example 1:
# 
# 
# Input: list1 = [10,1,13,6,9,5], a = 3, b = 4, list2 =
# [1000000,1000001,1000002]
# Output: [10,1,13,1000000,1000001,1000002,5]
# Explanation: We remove the nodes 3 and 4 and put the entire list2 in their
# place. The blue edges and nodes in the above figure indicate the result.
# 
# 
# Example 2:
# 
# 
# Input: list1 = [0,1,2,3,4,5,6], a = 2, b = 5, list2 =
# [1000000,1000001,1000002,1000003,1000004]
# Output: [0,1,1000000,1000001,1000002,1000003,1000004,6]
# Explanation: The blue edges and nodes in the above figure indicate the
# result.
# 
# 
# 
# Constraints:
# 
# 
# 3 <= list1.length <= 10^4
# 1 <= a <= b < list1.length - 1
# 1 <= list2.length <= 10^4
# 
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        diff = b - a
        head1, head2 = list1, list2

        curr1 = head1
        for _ in range(diff):
            curr1 = curr1.next

        a_node, b_node = head1, curr1
        prev_a = None
        for _ in range(a): 
            prev_a = a_node
            a_node = a_node.next
            b_node = b_node.next
        
        next_b = b_node.next

        curr2 = head2
        while curr2.next:
            curr2 = curr2.next


        prev_a.next = head2
        b_node.next = None
        curr2.next = next_b

        return list1
# @lc code=end

