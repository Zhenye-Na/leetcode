#
# @lc app=leetcode id=79 lang=python3
#
# [79] Word Search
#
# https://leetcode.com/problems/word-search/description/
#
# algorithms
# Medium (36.63%)
# Likes:    5343
# Dislikes: 236
# Total Accepted:    627.6K
# Total Submissions: 1.7M
# Testcase Example:  '[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]\n"ABCCED"'
#
# Given an m x n grid of characters board and a string word, return true if
# word exists in the grid.
# 
# The word can be constructed from letters of sequentially adjacent cells,
# where adjacent cells are horizontally or vertically neighboring. The same
# letter cell may not be used more than once.
# 
# Note: There will be some test cases with a board or a word larger than
# constraints to test if your solution is using pruning.
# 
# 
# Example 1:
# 
# 
# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word
# = "ABCCED"
# Output: true
# 
# 
# Example 2:
# 
# 
# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word
# = "SEE"
# Output: true
# 
# 
# Example 3:
# 
# 
# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word
# = "ABCB"
# Output: false
# 
# 
# 
# Constraints:
# 
# 
# m == board.length
# n = board[i].length
# 1 <= m, n <= 6
# 1 <= word.length <= 15
# board and word consists of only lowercase and uppercase English letters.
# 
# 
#

# @lc code=start
class Solution:

    def __init__(self):
        self.dx = [1, -1, 0, 0]
        self.dy = [0, 0, 1, -1]

        self.seen = set([])

    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board or not word or len(board) == 0 or len(board[0]) == 0:
            return False

        self.m, self.n = len(board), len(board[0])
        start_points = []
        for i in range(self.m):
            for j in range(self.n):
                if board[i][j] == word[0]:
                    start_points.append((i, j))

        if not start_points:
            return False

        for x, y in start_points:
            self.seen = set([(x, y)])
            if self._dfs(x, y, word, 1, board):
                return True

        return False


    def _dfs(self, x, y, word, start_index, board):
        if start_index >= len(word):
            return True

        for i in range(4):
            next_x, next_y = x + self.dx[i], y + self.dy[i]
            if self._check(next_x, next_y, board, word[start_index]):
                self.seen.add((next_x, next_y))
                if self._dfs(next_x, next_y, word, start_index + 1, board):
                    return True
                self.seen.remove((next_x, next_y))

        return False


    def _check(self, x, y, board, target):
        return 0 <= x < self.m and 0 <= y < self.n and board[x][y] == target and (x, y) not in self.seen
# @lc code=end

