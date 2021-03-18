#
# @lc app=leetcode id=150 lang=python3
#
# [150] Evaluate Reverse Polish Notation
#
# https://leetcode.com/problems/evaluate-reverse-polish-notation/description/
#
# algorithms
# Medium (37.66%)
# Likes:    1470
# Dislikes: 513
# Total Accepted:    271.9K
# Total Submissions: 715.9K
# Testcase Example:  '["2","1","+","3","*"]'
#
# Evaluate the value of an arithmetic expression in Reverse Polish Notation.
# 
# Valid operators are +, -, *, and /. Each operand may be an integer or another
# expression.
# 
# Note that division between two integers should truncate toward zero.
# 
# It is guaranteed that the given RPN expression is always valid. That means
# the expression would always evaluate to a result, and there will not be any
# division by zero operation.
# 
# 
# Example 1:
# 
# 
# Input: tokens = ["2","1","+","3","*"]
# Output: 9
# Explanation: ((2 + 1) * 3) = 9
# 
# 
# Example 2:
# 
# 
# Input: tokens = ["4","13","5","/","+"]
# Output: 6
# Explanation: (4 + (13 / 5)) = 6
# 
# 
# Example 3:
# 
# 
# Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
# Output: 22
# Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
# = ((10 * (6 / (12 * -11))) + 17) + 5
# = ((10 * (6 / -132)) + 17) + 5
# = ((10 * 0) + 17) + 5
# = (0 + 17) + 5
# = 17 + 5
# = 22
# 
# 
# 
# Constraints:
# 
# 
# 1 <= tokens.length <= 10^4
# tokens[i] is either an operator: "+", "-", "*", or "/", or an integer in the
# range [-200, 200].
# 
# 
#

# @lc code=start
class Solution:
    def __init__(self):
        self.operands = ["+", "-", "*", "/"]

    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for idx, token in enumerate(tokens):
            if token not in self.operands:
                stack.append(token)
            else:
                right = stack.pop()
                left = stack.pop()
                tmp_res = int(eval(left + token + right))   # make sure eval() is used safely
                stack.append(str(tmp_res))

        return int(stack[-1])
# @lc code=end

