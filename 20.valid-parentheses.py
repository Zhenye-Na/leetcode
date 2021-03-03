#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#
# https://leetcode.com/problems/valid-parentheses/description/
#
# algorithms
# Easy (39.76%)
# Likes:    6909
# Dislikes: 286
# Total Accepted:    1.3M
# Total Submissions: 3.3M
# Testcase Example:  '"()"'
#
# Given a string s containing just the characters '(', ')', '{', '}', '[' and
# ']', determine if the input string is valid.
# 
# An input string is valid if:
# 
# 
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# 
# 
# 
# Example 1:
# 
# 
# Input: s = "()"
# Output: true
# 
# 
# Example 2:
# 
# 
# Input: s = "()[]{}"
# Output: true
# 
# 
# Example 3:
# 
# 
# Input: s = "(]"
# Output: false
# 
# 
# Example 4:
# 
# 
# Input: s = "([)]"
# Output: false
# 
# 
# Example 5:
# 
# 
# Input: s = "{[]}"
# Output: true
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 10^4
# s consists of parentheses only '()[]{}'.
# 
# 
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        if not s or len(s) == 0:
            return True

        stack = []
        for i in range(len(s)):
            if s[i] == '(' or s[i] == '[' or s[i] == '{':
                stack.append(s[i])
            else:
                if len(stack) == 0:
                    return False

                if ( s[i] == ')' and stack[-1] != '(' ) or ( s[i] == ']' and stack[-1] != '[' ) or ( s[i] == '}' and stack[-1] != '{' ):
                    return False

                stack.pop()

        return len(stack) == 0


# @lc code=end

