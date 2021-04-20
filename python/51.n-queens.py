#
# @lc app=leetcode id=51 lang=python3
#
# [51] N-Queens
#
# https://leetcode.com/problems/n-queens/description/
#
# algorithms
# Hard (49.22%)
# Likes:    2729
# Dislikes: 98
# Total Accepted:    244.4K
# Total Submissions: 490.3K
# Testcase Example:  '4'
#
# The n-queens puzzle is the problem of placing n queens on an n x n chessboard
# such that no two queens attack each other.
# 
# Given an integer n, return all distinct solutions to the n-queens puzzle.
# 
# Each solution contains a distinct board configuration of the n-queens'
# placement, where 'Q' and '.' both indicate a queen and an empty space,
# respectively.
# 
# 
# Example 1:
# 
# 
# Input: n = 4
# Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
# Explanation: There exist two distinct solutions to the 4-queens puzzle as
# shown above
# 
# 
# Example 2:
# 
# 
# Input: n = 1
# Output: [["Q"]]
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
    def solveNQueens(self, n: int) -> List[List[str]]:
        if not n or n < 0:
            return [[]]


        self.n = n
        solutions = []
        self._dfs(0, [], solutions)

        res = []
        for solution in solutions:
            res.append(self._create_chessboard(solution))

        return res

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


    def _create_chessboard(self, solution):
        # solution is an array, [2,0,3,1], each value
        # represent column should be Q
        board = []
        for i in range(len(solution)):
            tmp = ["." for _ in range(len(solution))]
            tmp[solution[i]] = 'Q'
            board.append("".join(tmp))

        return board
# @lc code=end

