#
# @lc app=leetcode id=65 lang=python3
#
# [65] Valid Number
#
# https://leetcode.com/problems/valid-number/description/
#
# algorithms
# Hard (15.76%)
# Likes:    875
# Dislikes: 5503
# Total Accepted:    195.5K
# Total Submissions: 1.2M
# Testcase Example:  '"0"'
#
# A valid number can be split up into these components (in order):
# 
# 
# A decimal number or an integer.
# (Optional) An 'e' or 'E', followed by an integer.
# 
# 
# A decimal number can be split up into these components (in order):
# 
# 
# (Optional) A sign character (either '+' or '-').
# One of the following formats:
# 
# At least one digit, followed by a dot '.'.
# At least one digit, followed by a dot '.', followed by at least one
# digit.
# A dot '.', followed by at least one digit.
# 
# 
# 
# 
# An integer can be split up into these components (in order):
# 
# 
# (Optional) A sign character (either '+' or '-').
# At least one digit.
# 
# 
# For example, all the following are valid numbers: ["2", "0089", "-0.1",
# "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7", "+6e-1", "53.5e93",
# "-123.456e789"], while the following are not valid numbers: ["abc", "1a",
# "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53"].
# 
# Given a string s, return true if s is a valid number.
# 
# 
# Example 1:
# 
# 
# Input: s = "0"
# Output: true
# 
# 
# Example 2:
# 
# 
# Input: s = "e"
# Output: false
# 
# 
# Example 3:
# 
# 
# Input: s = "."
# Output: false
# 
# 
# Example 4:
# 
# 
# Input: s = ".1"
# Output: true
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 20
# s consists of only English letters (both uppercase and lowercase), digits
# (0-9), plus '+', minus '-', or dot '.'.
# 
# 
#

# @lc code=start
class Solution:
    def isNumber(self, s: str) -> bool:
        #  "(___)?[+-]?(\d*453)?(\.\d)?(\d*)41231(e[+-]?\d+1312)?(____)?"
        pattern = r'^\s*[+-]?(\d+\.?|\.\d)\d*((e[+-]?|E[+-]?)\d+)?\s*$'
        return re.match(pattern, s)

# @lc code=end


# References
#   https://www.youtube.com/watch?v=6TcCGyybs0g&ab_channel=RenZhang
#   Solution 1: Regular Expression
#   Solution 2: Finite State Machine

