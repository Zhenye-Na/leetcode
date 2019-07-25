#
# @lc app=leetcode id=79 lang=python3
#
# [79] Word Search
#


class Solution:
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board or len(board) == 0 or len(board[0]) == 0:
            return False

        self.m, self.n = len(board), len(board[0])
        self.length = len(word)
        self.contains = False

        startChar = word[0]
        for i in range(self.m):
            for j in range(self.n):
                if board[i][j] == startChar:
                    self.dfs(i, j, board, word, 1, set([]))
                    if self.contains:
                        break

        return self.contains

    def dfs(self, x, y, board, word, idx, history):
        if idx == self.length:
            self.contains = True
            return

        history.add((x, y))
        for i in range(4):
            new_x, new_y = x + self.dx[i], y + self.dy[i]
            if self.isValid(new_x, new_y, board, word, idx, history):
                if not self.contains:
                    self.dfs(new_x, new_y, board, word,
                             idx + 1, history.copy())

    def isValid(self, x, y, board, word, idx, history):
        return 0 <= x < self.m and 0 <= y < self.n and board[x][y] == word[idx] and (x, y) not in history
