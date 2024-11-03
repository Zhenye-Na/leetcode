#
# @lc app=leetcode id=796 lang=python3
#
# [796] Rotate String
#
# https://leetcode.com/problems/rotate-string/description/
#
# algorithms
# Easy (59.58%)
# Likes:    3917
# Dislikes: 238
# Total Accepted:    428.1K
# Total Submissions: 702.7K
# Testcase Example:  '"abcde"\n"cdeab"'
#
# Given two strings s and goal, return true if and only if s can become goal
# after some number of shifts on s.
#
# A shift on s consists of moving the leftmost character of s to the rightmost
# position.
#
#
# For example, if s = "abcde", then it will be "bcdea" after one shift.
#
#
#
# Example 1:
# Input: s = "abcde", goal = "cdeab"
# Output: true
# Example 2:
# Input: s = "abcde", goal = "abced"
# Output: false
#
#
# Constraints:
#
#
# 1 <= s.length, goal.length <= 100
# s and goal consist of lowercase English letters.
#
#
#


# @lc code=start
from collections import deque


class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        lst_s = [char for char in s]
        deque_s = deque(lst_s)

        for _ in range(len(deque_s)):
            deque_s.append(deque_s.popleft())
            if "".join(deque_s) == goal:
                return True

        return False


# @lc code=end
