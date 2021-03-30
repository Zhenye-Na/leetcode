#
# @lc app=leetcode id=32 lang=python3
#
# [32] Longest Valid Parentheses
#
# https://leetcode.com/problems/longest-valid-parentheses/description/
#
# algorithms
# Hard (29.19%)
# Likes:    4629
# Dislikes: 171
# Total Accepted:    345.7K
# Total Submissions: 1.2M
# Testcase Example:  '"(()"'
#
# Given a string containing just the characters '(' and ')', find the length of
# the longest valid (well-formed) parentheses substring.
# 
# 
# Example 1:
# 
# 
# Input: s = "(()"
# Output: 2
# Explanation: The longest valid parentheses substring is "()".
# 
# 
# Example 2:
# 
# 
# Input: s = ")()())"
# Output: 4
# Explanation: The longest valid parentheses substring is "()()".
# 
# 
# Example 3:
# 
# 
# Input: s = ""
# Output: 0
# 
# 
# 
# Constraints:
# 
# 
# 0 <= s.length <= 3 * 10^4
# s[i] is '(', or ')'.
# 
# 
#

# @lc code=start
class Solution:

    def longestValidParentheses(self, s: str) -> int:
        stack = []
        res = 0

        for i, char in enumerate(s):
            if char == "(":
                stack.append(i)
            else:
                if stack and s[stack[-1]] == '(':
                    stack.pop()
                    res = max(res, i - (stack[-1] if stack else -1))
                else:
                    stack.append(i)

        return res

# @lc code=end

