#
# @lc app=leetcode id=1963 lang=python3
#
# [1963] Minimum Number of Swaps to Make the String Balanced
#
# https://leetcode.com/problems/minimum-number-of-swaps-to-make-the-string-balanced/description/
#
# algorithms
# Medium (70.19%)
# Likes:    1984
# Dislikes: 96
# Total Accepted:    111.6K
# Total Submissions: 149.4K
# Testcase Example:  '"][]["'
#
# You are given a 0-indexed string s of even length n. The string consists of
# exactly n / 2 opening brackets '[' and n / 2 closing brackets ']'.
#
# A string is called balanced if and only if:
#
#
# It is the empty string, or
# It can be written as AB, where both A and B are balanced strings, or
# It can be written as [C], where C is a balanced string.
#
#
# You may swap the brackets at any two indices any number of times.
#
# Return the minimum number of swaps to make s balanced.
#
#
# Example 1:
#
#
# Input: s = "][]["
# Output: 1
# Explanation: You can make the string balanced by swapping index 0 with index
# 3.
# The resulting string is "[[]]".
#
#
# Example 2:
#
#
# Input: s = "]]][[["
# Output: 2
# Explanation: You can do the following to make the string balanced:
# - Swap index 0 with index 4. s = "[]][][".
# - Swap index 1 with index 5. s = "[[][]]".
# The resulting string is "[[][]]".
#
#
# Example 3:
#
#
# Input: s = "[]"
# Output: 0
# Explanation: The string is already balanced.
#
#
#
# Constraints:
#
#
# n == s.length
# 2 <= n <= 10^6
# n is even.
# s[i] is either '[' or ']'.
# The number of opening brackets '[' equals n / 2, and the number of closing
# brackets ']' equals n / 2.
#
#
#


# @lc code=start
class Solution:
    def minSwaps(self, s: str) -> int:
        if len(s) == 2:
            return 0 if s == "[]" else 1

        left, right = 0, len(s) - 1
        left_open_bracket = 0
        left_close_bracket = 0
        right_open_bracket = 0
        right_close_bracket = 0

        res = 0
        while left < right:
            while left < right and (
                left_open_bracket > left_close_bracket or s[left] == "["
            ):
                left_open_bracket += 1 if s[left] == "[" else 0
                left_close_bracket += 1 if s[left] == "]" else 0
                left += 1

            while left < right and (
                right_close_bracket > right_open_bracket or s[right] == "]"
            ):
                right_open_bracket += 1 if s[right] == "[" else 0
                right_close_bracket += 1 if s[right] == "]" else 0
                right -= 1

            if left < right:
                res += 1
                left += 1
                right -= 1
                left_open_bracket += 1
                right_close_bracket += 1

        return res


# @lc code=end
