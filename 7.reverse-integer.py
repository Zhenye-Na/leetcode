#
# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
#
# https://leetcode.com/problems/reverse-integer/description/
#
# algorithms
# Easy (25.87%)
# Likes:    4384
# Dislikes: 6769
# Total Accepted:    1.4M
# Total Submissions: 5.5M
# Testcase Example:  '123'
#
# Given a signed 32-bit integer x, return x with its digits reversed. If
# reversing x causes the value to go outside the signed 32-bit integer range
# [-2^31, 2^31 - 1], then return 0.
# 
# Assume the environment does not allow you to store 64-bit integers (signed or
# unsigned).
# 
# 
# Example 1:
# Input: x = 123
# Output: 321
# Example 2:
# Input: x = -123
# Output: -321
# Example 3:
# Input: x = 120
# Output: 21
# Example 4:
# Input: x = 0
# Output: 0
# 
# 
# Constraints:
# 
# 
# -2^31 <= x <= 2^31 - 1
# 
# 
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        x = str(x)
        length = len(x)
        if length == 1:
            return int(x)

        minus_sign = False
        if x[0] == "-":
            minus_sign = True
            x = x[1:]
        
        x = x[::-1]
        i = 0
        while i < len(x):
            if x[i] == "0":
                i += 1
            else:
                break
        x = x[i:]

        if minus_sign:
            x = "-" + x

        return int(x) if int(x) >= - pow(2, 31) and int(x) <= pow(2, 31) - 1 else 0

# @lc code=end

