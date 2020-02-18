#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if not n or n < 0:
            return []

        self.result = []
        self.dfs(n, n, '', n)
        return self.result

    def dfs(self, left, right, current, n):
        if len(current) == 2 * n:
            self.result.append(current)

        if left > 0:
            self.dfs(left - 1, right, current + '(', n)

        if right > left:
            self.dfs(left, right - 1, current + ')', n)
