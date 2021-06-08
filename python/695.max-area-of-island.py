#
# @lc app=leetcode id=695 lang=python3
#
# [695] Max Area of Island
#
# https://leetcode.com/problems/max-area-of-island/description/
#
# algorithms
# Medium (64.42%)
# Likes:    2794
# Dislikes: 94
# Total Accepted:    215.6K
# Total Submissions: 332.7K
# Testcase Example:  '[[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]]'
#
# Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's
# (representing land) connected 4-directionally (horizontal or vertical.) You
# may assume all four edges of the grid are surrounded by water.
# 
# Find the maximum area of an island in the given 2D array. (If there is no
# island, the maximum area is 0.)
# 
# Example 1:
# 
# 
# [[0,0,1,0,0,0,0,1,0,0,0,0,0],
# ⁠[0,0,0,0,0,0,0,1,1,1,0,0,0],
# ⁠[0,1,1,0,1,0,0,0,0,0,0,0,0],
# ⁠[0,1,0,0,1,1,0,0,1,0,1,0,0],
# ⁠[0,1,0,0,1,1,0,0,1,1,1,0,0],
# ⁠[0,0,0,0,0,0,0,0,0,0,1,0,0],
# ⁠[0,0,0,0,0,0,0,1,1,1,0,0,0],
# ⁠[0,0,0,0,0,0,0,1,1,0,0,0,0]]
# 
# Given the above grid, return 6. Note the answer is not 11, because the island
# must be connected 4-directionally.
# 
# Example 2:
# 
# 
# [[0,0,0,0,0,0,0,0]]
# Given the above grid, return 0.
# 
# Note: The length of each dimension in the given grid does not exceed 50.
# 
#

# @lc code=start
from collections import deque

class Solution:
    
    def __init__(self):
        self.dx = [1, -1, 0, 0]
        self.dy = [0, 0, -1, 1]
        self.max_area = 0

        self.ISLAND = 1
        self.EMPTY = 0

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid or len(grid) == 0 or len(grid[0]) == 0:
            return self.max_area

        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == self.ISLAND:
                    self.max_area = max(
                        self.max_area,
                        self.bfs(i, j, grid)
                    )
        
        return self.max_area


    def bfs(self, x, y, grid):
        queue = deque([(x, y)])
        curr_area = 1
        while queue:
            print(queue)
            x, y = queue.popleft()
            grid[x][y] == self.EMPTY
            for d in range(4):
                next_x, next_y = x + self.dx[d], y + self.dy[d]
                if 0 <= next_x < len(grid) and 0 <= next_y < len(grid[0]) and grid[next_x][next_y] == self.ISLAND:
                    curr_area += 1
                    queue.append((next_x, next_y))

        return curr_area
# @lc code=end

