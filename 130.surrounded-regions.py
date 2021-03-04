#
# @lc app=leetcode id=130 lang=python3
#
# [130] Surrounded Regions
#
# https://leetcode.com/problems/surrounded-regions/description/
#
# algorithms
# Medium (29.21%)
# Likes:    2538
# Dislikes: 750
# Total Accepted:    285.6K
# Total Submissions: 969.9K
# Testcase Example:  '[["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]'
#
# Given an m x n matrix board containing 'X' and 'O', capture all regions
# surrounded by 'X'.
# 
# A region is captured by flipping all 'O's into 'X's in that surrounded
# region.
# 
# 
# Example 1:
# 
# 
# Input: board =
# [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
# Output:
# [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
# Explanation: Surrounded regions should not be on the border, which means that
# any 'O' on the border of the board are not flipped to 'X'. Any 'O' that is
# not on the border and it is not connected to an 'O' on the border will be
# flipped to 'X'. Two cells are connected if they are adjacent cells connected
# horizontally or vertically.
# 
# 
# Example 2:
# 
# 
# Input: board = [["X"]]
# Output: [["X"]]
# 
# 
# 
# Constraints:
# 
# 
# m == board.length
# n == board[i].length
# 1 <= m, n <= 200
# board[i][j] is 'X' or 'O'.
# 
# 
#

# @lc code=start

from collections import deque
class Solution:
    def __init__(self):
        self.directions = [[0,1],[1,0],[0,-1],[-1,0]]


    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        queue = deque([])
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                if board[i][j] == "O" and (i == 0 or i == m - 1 or j == 0 or j == n - 1):
                    queue.append((i, j))

        while queue:
            x, y = queue.popleft()
            if 0 <= x < m and 0 <= y < n and board[x][y] == "O":
                board[x][y] = "Y"
                for d in self.directions:
                    next_x, next_y = x + d[0], y + d[1]
                    queue.append((next_x, next_y))

        for i in range(m):
            for j in range(n):
                if board[i][j] == "O":
                    board[i][j] = "X"
                if board[i][j] == "Y":
                    board[i][j] = "O"


# @lc code=end

