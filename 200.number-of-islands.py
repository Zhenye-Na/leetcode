#
# @lc app=leetcode id=200 lang=python3
#
# [200] Number of Islands
#
# https://leetcode.com/problems/number-of-islands/description/
#
# algorithms
# Medium (48.74%)
# Likes:    7796
# Dislikes: 238
# Total Accepted:    975.8K
# Total Submissions: 2M
# Testcase Example:  '[["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]'
#
# Given an m x n 2d grid map of '1's (land) and '0's (water), return the number
# of islands.
# 
# An island is surrounded by water and is formed by connecting adjacent lands
# horizontally or vertically. You may assume all four edges of the grid are all
# surrounded by water.
# 
# 
# Example 1:
# 
# 
# Input: grid = [
# ⁠ ["1","1","1","1","0"],
# ⁠ ["1","1","0","1","0"],
# ⁠ ["1","1","0","0","0"],
# ⁠ ["0","0","0","0","0"]
# ]
# Output: 1
# 
# 
# Example 2:
# 
# 
# Input: grid = [
# ⁠ ["1","1","0","0","0"],
# ⁠ ["1","1","0","0","0"],
# ⁠ ["0","0","1","0","0"],
# ⁠ ["0","0","0","1","1"]
# ]
# Output: 3
# 
# 
# 
# Constraints:
# 
# 
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 300
# grid[i][j] is '0' or '1'.
# 
# 
#

# @lc code=start
from collections import deque

class Solution:
    def __init__(self):
        self.directions = [[0,1],[1,0],[0,-1],[-1,0]]

    def numIslands(self, grid: List[List[str]]) -> int:
        self.m, self.n = len(grid), len(grid[0])
        self.grid = grid
        self.seen = set([])

        island = 0
        for i in range(self.m):
            for j in range(self.n):
                if self.grid[i][j] == "1":
                    self._bfs(i, j)
                    island += 1

        return island

    def _bfs(self, i, j):
        queue = deque([(i, j)])
        self.seen.add((i, j))
        while queue:
            x, y = queue.popleft()
            for d in self.directions:
                new_x, new_y = x + d[0], y + d[1]
                if self._valid(new_x, new_y):
                    queue.append((new_x, new_y))
                    self.seen.add((new_x, new_y))
                    self.grid[new_x][new_y] = "0"

    def _valid(self, x, y):
        return 0 <= x < self.m and 0 <= y < self.n and (x, y) not in self.seen and self.grid[x][y] == "1"

# @lc code=end

