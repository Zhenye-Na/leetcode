#
# @lc app=leetcode id=63 lang=python3
#
# [63] Unique Paths II
#
# https://leetcode.com/problems/unique-paths-ii/description/
#
# algorithms
# Medium (35.16%)
# Likes:    2590
# Dislikes: 289
# Total Accepted:    359.9K
# Total Submissions: 1M
# Testcase Example:  '[[0,0,0],[0,1,0],[0,0,0]]'
#
# A robot is located at the top-left corner of a m x n grid (marked 'Start' in
# the diagram below).
# 
# The robot can only move either down or right at any point in time. The robot
# is trying to reach the bottom-right corner of the grid (marked 'Finish' in
# the diagram below).
# 
# Now consider if some obstacles are added to the grids. How many unique paths
# would there be?
# 
# An obstacle and space is marked as 1 and 0 respectively in the grid.
# 
# 
# Example 1:
# 
# 
# Input: obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
# Output: 2
# Explanation: There is one obstacle in the middle of the 3x3 grid above.
# There are two ways to reach the bottom-right corner:
# 1. Right -> Right -> Down -> Down
# 2. Down -> Down -> Right -> Right
# 
# 
# Example 2:
# 
# 
# Input: obstacleGrid = [[0,1],[0,0]]
# Output: 1
# 
# 
# 
# Constraints:
# 
# 
# m == obstacleGrid.length
# n == obstacleGrid[i].length
# 1 <= m, n <= 100
# obstacleGrid[i][j] is 0 or 1.
# 
# 
#

# @lc code=start
class Solution:
    def __init__(self):
        self.empty = 0
        self.block = 1

    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        if not grid or len(grid) == 0 or len(grid[0]) == 0:
            return 0

        m, n = len(grid), len(grid[0])
        f = [[0 for _ in range(n)] for _ in range(m)]
        f[0][0] = 1 if grid[0][0] == self.empty else 0

        for i in range(1, m):
            f[i][0] = 1 if f[i - 1][0] and grid[i][0] == self.empty else 0

        for j in range(1, n):
            f[0][j] = 1 if f[0][j - 1] and grid[0][j] == self.empty else 0

        for i in range(1, m):
            for j in range(1, n):
                f[i][j] = f[i][j - 1] + f[i - 1][j] if grid[i][j] == self.empty else 0

        return f[-1][-1]
# @lc code=end

