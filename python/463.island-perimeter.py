#
# @lc app=leetcode id=463 lang=python3
#
# [463] Island Perimeter
#
# https://leetcode.com/problems/island-perimeter/description/
#
# algorithms
# Easy (67.33%)
# Likes:    3392
# Dislikes: 205
# Total Accepted:    304.3K
# Total Submissions: 449.5K
# Testcase Example:  '[[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]'
#
# You are given row x col grid representing a map where grid[i][j] = 1
# represents land and grid[i][j] = 0 represents water.
# 
# Grid cells are connected horizontally/vertically (not diagonally). The grid
# is completely surrounded by water, and there is exactly one island (i.e., one
# or more connected land cells).
# 
# The island doesn't have "lakes", meaning the water inside isn't connected to
# the water around the island. One cell is a square with side length 1. The
# grid is rectangular, width and height don't exceed 100. Determine the
# perimeter of the island.
# 
# 
# Example 1:
# 
# 
# Input: grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
# Output: 16
# Explanation: The perimeter is the 16 yellow stripes in the image above.
# 
# 
# Example 2:
# 
# 
# Input: grid = [[1]]
# Output: 4
# 
# 
# Example 3:
# 
# 
# Input: grid = [[1,0]]
# Output: 4
# 
# 
# 
# Constraints:
# 
# 
# row == grid.length
# col == grid[i].length
# 1 <= row, col <= 100
# grid[i][j] is 0 or 1.
# There is exactly one island in grid.
# 
# 
#

# @lc code=start
from collections import deque

class Solution:
    def __init__(self):
        self.n = 0
        self.m = 0
        self.LAND = 1
        self.WATER = 0
    
        #       up, down, right, left
        self.dx = [0, 0, 1, -1]
        self.dy = [1, -1, 0, 0]


    def islandPerimeter(self, grid: List[List[int]]) -> int:
        if not grid or len(grid) == 0 or len(grid[0]) == 0:
            return 0
        
        self.n, self.m = len(grid), len(grid[0])
        
        x, y = 0, 0
        for i in range(self.n):
            for j in range(self.m):
                if grid[i][j] == self.LAND:
                    return self.bfs(grid, i, j)


    def bfs(self, grid, x, y):
        queue = deque([(x, y)])
        self.seen = set([(x, y)])
        
        res = 0
        while queue:
            x, y = queue.popleft()
            adj = 0
            for d in range(4):
                next_x, next_y = x + self.dx[d], y + self.dy[d]
                if self.is_valid(next_x, next_y, grid):
                    adj += 1
                    if (next_x, next_y) not in self.seen:
                        self.seen.add((next_x, next_y))
                        queue.append((next_x, next_y))
                
            res += 4 - adj


        return res
    def is_valid(self, x, y, grid):
        return 0 <= x < self.n and 0 <= y < self.m and grid[x][y] == self.LAND
# @lc code=end

