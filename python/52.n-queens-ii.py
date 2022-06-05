#
# @lc app=leetcode id=52 lang=python3
#
# [52] N-Queens II
#
# https://leetcode.com/problems/n-queens-ii/description/
#
# algorithms
# Hard (59.78%)
# Likes:    765
# Dislikes: 179
# Total Accepted:    156.9K
# Total Submissions: 260.1K
# Testcase Example:  '4'
#
# The n-queens puzzle is the problem of placing n queens on an n x n chessboard
# such that no two queens attack each other.
# 
# Given an integer n, return the number of distinct solutions to the n-queens
# puzzle.
# 
# 
# Example 1:
# 
# 
# Input: n = 4
# Output: 2
# Explanation: There are two distinct solutions to the 4-queens puzzle as
# shown.
# 
# 
# Example 2:
# 
# 
# Input: n = 1
# Output: 1
# 
# 
# 
# Constraints:
# 
# 
# 1 <= n <= 9
# 
# 
#

# @lc code=start
class Solution:
    def totalNQueens(self, n: int) -> int:
        if not n or n < 0:
            return [[]]

        self.n = n
        solutions = []
        self._dfs(0, [], solutions)

        return len(solutions)

    def _dfs(self, row_index, curr, res):
        if len(curr) == self.n:
            res.append(curr[:])
            return
        if row_index >= self.n:
            return

        for col in range(self.n):
            if len(curr) == 0 or self.check_valid(row_index, col, curr):
                curr.append(col)
                self._dfs(row_index + 1, curr, res)
                curr.pop()

    def check_valid(self, x2, y2, curr):
        for x1, y1 in enumerate(curr):
            if x1 == x2 or y1 == y2:
                return False
            if x1 + y1 == x2 + y2:
                return False
            if x1 - y1 == x2 - y2:
                return False
        return True
# @lc code=end

