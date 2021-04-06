#
# @lc app=leetcode id=224 lang=python3
#
# [224] Basic Calculator
#
# https://leetcode.com/problems/basic-calculator/description/
#
# algorithms
# Hard (38.04%)
# Likes:    2126
# Dislikes: 176
# Total Accepted:    203.8K
# Total Submissions: 532.8K
# Testcase Example:  '"1 + 1"'
#
# Given a string s representing an expression, implement a basic calculator to
# evaluate it.
# 
# 
# Example 1:
# 
# 
# Input: s = "1 + 1"
# Output: 2
# 
# 
# Example 2:
# 
# 
# Input: s = " 2-1 + 2 "
# Output: 3
# 
# 
# Example 3:
# 
# 
# Input: s = "(1+(4+5+2)-3)+(6+8)"
# Output: 23
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 3 * 10^5
# s consists of digits, '+', '-', '(', ')', and ' '.
# s represents a valid expression.
# 
# 
#

# @lc code=start
class Solution:
    def calculate(self, s: str) -> int:
        i = 0
        res = 0
        sign = 1
        stack = []

        while i < len(s):
            if s[i].isdigit():
                curr = int(s[i])
                i += 1
                while i < len(s) and s[i].isdigit():
                    curr = curr * 10 + int(s[i])
                    i += 1

                res += curr * sign
                i -= 1

            elif s[i] == "+":
                sign = 1
            elif s[i] == "-":
                sign = -1

            elif s[i] == "(":
                stack.append(res)
                stack.append(sign)
                res = 0
                sign = 1

            elif s[i] == ")":
                res = stack.pop() * res
                res += stack.pop()

            i += 1

        return res
# @lc code=end

