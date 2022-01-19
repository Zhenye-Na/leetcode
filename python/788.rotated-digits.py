#
# @lc app=leetcode id=788 lang=python3
#
# [788] Rotated Digits
#
# https://leetcode.com/problems/rotated-digits/description/
#
# algorithms
# Medium (57.37%)
# Likes:    543
# Dislikes: 1676
# Total Accepted:    80.2K
# Total Submissions: 140K
# Testcase Example:  '10'
#
# An integer x is a good if after rotating each digit individually by 180
# degrees, we get a valid number that is different from x. Each digit must be
# rotated - we cannot choose to leave it alone.
# 
# A number is valid if each digit remains a digit after rotation. For
# example:
# 
# 
# 0, 1, and 8 rotate to themselves,
# 2 and 5 rotate to each other (in this case they are rotated in a different
# direction, in other words, 2 or 5 gets mirrored),
# 6 and 9 rotate to each other, and
# the rest of the numbers do not rotate to any other number and become
# invalid.
# 
# 
# Given an integer n, return the number of good integers in the range [1,
# n].
# 
# 
# Example 1:
# 
# 
# Input: n = 10
# Output: 4
# Explanation: There are four good numbers in the range [1, 10] : 2, 5, 6, 9.
# Note that 1 and 10 are not good numbers, since they remain unchanged after
# rotating.
# 
# 
# Example 2:
# 
# 
# Input: n = 1
# Output: 0
# 
# 
# Example 3:
# 
# 
# Input: n = 2
# Output: 1
# 
# 
# 
# Constraints:
# 
# 
# 1 <= n <= 10^4
# 
# 
#

# @lc code=start
class Solution:
    def __init__(self):
        self.rotates = [0, 1, 5,'-', '-', 2, 9, '-', 8, 6]

    def rotatedDigits(self, n: int) -> int:
        count = 0
        for i in range(n + 1):
            if self._is_good_number(i):
                count += 1

        return count

    def _is_good_number(self, num):
        num_s = str(num)
        same_digit = 0
        for char in num_s:
            if '-' == self.rotates[int(char)]:
                return False
            elif int(char) == self.rotates[int(char)]:
                same_digit += 1

        return same_digit != len(num_s)
# @lc code=end

