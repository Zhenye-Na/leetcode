#
# @lc app=leetcode id=241 lang=python3
#
# [241] Different Ways to Add Parentheses
#
# https://leetcode.com/problems/different-ways-to-add-parentheses/description/
#
# algorithms
# Medium (57.07%)
# Likes:    2133
# Dislikes: 114
# Total Accepted:    120.4K
# Total Submissions: 209.3K
# Testcase Example:  '"2-1-1"'
#
# Given a string expression of numbers and operators, return all possible
# results from computing all the different possible ways to group numbers and
# operators. You may return the answer in any order.
# 
# 
# Example 1:
# 
# 
# Input: expression = "2-1-1"
# Output: [0,2]
# Explanation:
# ((2-1)-1) = 0 
# (2-(1-1)) = 2
# 
# 
# Example 2:
# 
# 
# Input: expression = "2*3-4*5"
# Output: [-34,-14,-10,-10,10]
# Explanation:
# (2*(3-(4*5))) = -34 
# ((2*3)-(4*5)) = -14 
# ((2*(3-4))*5) = -10 
# (2*((3-4)*5)) = -10 
# (((2*3)-4)*5) = 10
# 
# 
# 
# Constraints:
# 
# 
# 1 <= expression.length <= 20
# expression consists of digits and the operator '+', '-', and '*'.
# 
# 
#

# @lc code=start
# DFS with Memoization
#   Runtime: 28 ms
#   Memory Usage: 14.4 MB
from collections import defaultdict

class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        self.memo = defaultdict(list)
        return self.dfs(expression)


    def dfs(self, expression):
        if expression in self.memo:
            return self.memo[expression]

        if "+" not in expression and "-" not in expression and "*" not in expression:
            return [int(expression)]

        res = []

        for i in range(len(expression)):
            if expression[i] in ["*", "-", "+"]:
                left = self.dfs(expression[:i])
                self.memo[expression[:i]] = left
                right = self.dfs(expression[i + 1:])
                self.memo[expression[i + 1:]] = right
                token = expression[i]

                if token == "*":
                    for left_num in left:
                        for right_num in right:
                            res.append(left_num * right_num)
                elif token == "+":
                    for left_num in left:
                        for right_num in right:
                            res.append(left_num + right_num)
                elif token == "-":
                    for left_num in left:
                        for right_num in right:
                            res.append(left_num - right_num)

        self.memo[expression] = res
        return res




# DFS (Divide and Conquer)
#   Runtime: 36 ms
#   Memory Usage: 14.4 MB
class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        return self.dfs(expression)


    def dfs(self, expression):
        if "+" not in expression and "-" not in expression and "*" not in expression:
            return [int(expression)]

        res = []

        for i in range(len(expression)):
            if expression[i] in ["*", "-", "+"]:
                left = self.dfs(expression[:i])
                right = self.dfs(expression[i + 1:])
                token = expression[i]

                if token == "*":
                    for left_num in left:
                        for right_num in right:
                            res.append(left_num * right_num)
                elif token == "+":
                    for left_num in left:
                        for right_num in right:
                            res.append(left_num + right_num)
                elif token == "-":
                    for left_num in left:
                        for right_num in right:
                            res.append(left_num - right_num)

        return res
# @lc code=end

