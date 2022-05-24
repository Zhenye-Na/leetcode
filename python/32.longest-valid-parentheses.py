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
class Solution_Stack:
    def longestValidParentheses(self, s: str) -> int:
        if not s or len(s) == 0:
            return 0

        stack = []
        length = 0

        for i, char in enumerate(s):
            if char == "(":
                stack.append(i)

            else:
                if stack and s[stack[-1]] == "(":
                    stack.pop()
                    length = max(length, i - (stack[-1] if stack else -1))
                else:
                    stack.append(i)

        return length


class Solution_DP:
    def longestValidParentheses(self, s: str) -> int:

        # f[i] represents the length of the longest valid (well-formed) parentheses substring ending with s[i]
        s = "#" + s
        f = [0 for _ in range(len(s))]
        f[0] = 0

        for i in range(1, len(s)):
            if s[i] == "(":
                f[i] = 0
            else:
                # s[i] = ")"
                if s[i - 1] == "(":
                    f[i] = f[i - 2] + 2 if i >= 2 else 2
                else:

                    # eg: (())
                    if i - f[i - 1] - 1 >= 0 and s[i - f[i - 1] - 1] == "(":

                        f[i] = f[i - 1] + 2

                        # plus length before, eg   () (())
                        #                                i
                        if i - f[i - 1] - 2 >= 0:
                            f[i] += f[i - f[i - 1] - 2] if s[i - f[i - 1] - 2] == ")" else 0

        return max(f)
# @lc code=end

