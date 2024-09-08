#
# @lc app=leetcode id=725 lang=python3
#
# [725] Split Linked List in Parts
#
# https://leetcode.com/problems/split-linked-list-in-parts/description/
#
# algorithms
# Medium (53.74%)
# Likes:    2798
# Dislikes: 255
# Total Accepted:    129.2K
# Total Submissions: 218.9K
# Testcase Example:  '[1,2,3]\n5'
#
# Given the head of a singly linked list and an integer k, split the linked
# list into k consecutive linked list parts.
#
# The length of each part should be as equal as possible: no two parts should
# have a size differing by more than one. This may lead to some parts being
# null.
#
# The parts should be in the order of occurrence in the input list, and parts
# occurring earlier should always have a size greater than or equal to parts
# occurring later.
#
# Return an array of the k parts.
#
#
# Example 1:
#
#
# Input: head = [1,2,3], k = 5
# Output: [[1],[2],[3],[],[]]
# Explanation:
# The first element output[0] has output[0].val = 1, output[0].next = null.
# The last element output[4] is null, but its string representation as a
# ListNode is [].
#
#
# Example 2:
#
#
# Input: head = [1,2,3,4,5,6,7,8,9,10], k = 3
# Output: [[1,2,3,4],[5,6,7],[8,9,10]]
# Explanation:
# The input has been split into consecutive parts with size difference at most
# 1, and earlier parts are a larger size than the later parts.
#
#
#
# Constraints:
#
#
# The number of nodes in the list is in the range [0, 1000].
# 0 <= Node.val <= 1000
# 1 <= k <= 50
#
#
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional


class Solution:
    def splitListToParts(
        self, head: Optional[ListNode], k: int
    ) -> List[Optional[ListNode]]:
        total_len = self._get_length(head)
        quo, rem = divmod(total_len, k)
        arr = [quo for _ in range(k)]
        for i in range(len(arr)):
            if rem == 0:
                break

            arr[i] += 1
            rem -= 1

        res = []
        for target in arr:
            curr, next_head = self._split_list(head, target)
            res.append(curr)
            head = next_head

        return res

    def _split_list(self, head, target_len):
        # return 2 things, 1\ current split 2\ next split head
        split_head = head
        prev_node = None
        curr_len = 0
        while head and curr_len < target_len:
            prev_node = head
            head = head.next
            curr_len += 1

        if not head:
            return split_head, None
        else:
            prev_node.next = None
            return split_head, head

    def _get_length(self, head):
        length = 0
        while head:
            head = head.next
            length += 1

        return length


# @lc code=end
