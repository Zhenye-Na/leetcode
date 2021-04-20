#
# @lc app=leetcode id=227 lang=python3
#
# [227] Basic Calculator II
#
# https://leetcode.com/problems/basic-calculator-ii/description/
#
# algorithms
# Medium (38.39%)
# Likes:    2268
# Dislikes: 355
# Total Accepted:    261K
# Total Submissions: 673.6K
# Testcase Example:  '"3+2*2"'
#
# Given a string s which represents an expression, evaluate this expression and
# return its value. 
# 
# The integer division should truncate toward zero.
# 
# 
# Example 1:
# Input: s = "3+2*2"
# Output: 7
# Example 2:
# Input: s = " 3/2 "
# Output: 1
# Example 3:
# Input: s = " 3+5 / 2 "
# Output: 5
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 3 * 10^5
# s consists of integers and operators ('+', '-', '*', '/') separated by some
# number of spaces.
# s represents a valid expression.
# All the integers in the expression are non-negative integers in the range [0,
# 2^31 - 1].
# The answer is guaranteed to fit in a 32-bit integer.
# 
# 
#

# @lc code=start
class Solution:

    def calculate(self, s: str) -> int:
        i = 0
        stack = []
        res = 0
        sign = "+"
        curr = 0
        while i < len(s):
            if s[i].isdigit():
                curr = int(s[i])
                i += 1
                while i < len(s) and s[i].isdigit():
                    curr = curr * 10 + int(s[i])
                    i += 1
                i -= 1

            if (not s[i].isdigit() and s[i] != " ") or i == len(s) - 1:
                if sign == "+":
                    stack.append(curr)
                elif sign == "-":
                    stack.append(-curr)
                elif sign == "*":
                    stack.append(stack.pop() * curr)
                elif sign == "/":
                    stack.append(int(stack.pop() / curr))

                # update sign and curr number
                sign = s[i]
                curr = 0

            i += 1

        for num in stack:
            res += num

        return res
# @lc code=end

