#
# @lc app=leetcode id=741 lang=python3
#
# [741] Cherry Pickup
#
# https://leetcode.com/problems/cherry-pickup/description/
#
# algorithms
# Hard (35.65%)
# Likes:    2605
# Dislikes: 120
# Total Accepted:    53.3K
# Total Submissions: 147K
# Testcase Example:  '[[0,1,-1],[1,0,-1],[1,1,1]]'
#
# You are given an n x n grid representing a field of cherries, each cell is
# one of three possible integers.
# 
# 
# 0 means the cell is empty, so you can pass through,
# 1 means the cell contains a cherry that you can pick up and pass through,
# or
# -1 means the cell contains a thorn that blocks your way.
# 
# 
# Return the maximum number of cherries you can collect by following the rules
# below:
# 
# 
# Starting at the position (0, 0) and reaching (n - 1, n - 1) by moving right
# or down through valid path cells (cells with value 0 or 1).
# After reaching (n - 1, n - 1), returning to (0, 0) by moving left or up
# through valid path cells.
# When passing through a path cell containing a cherry, you pick it up, and the
# cell becomes an empty cell 0.
# If there is no valid path between (0, 0) and (n - 1, n - 1), then no cherries
# can be collected.
# 
# 
# 
# Example 1:
# 
# 
# Input: grid = [[0,1,-1],[1,0,-1],[1,1,1]]
# Output: 5
# Explanation: The player started at (0, 0) and went down, down, right right to
# reach (2, 2).
# 4 cherries were picked up during this single trip, and the matrix becomes
# [[0,1,-1],[0,0,-1],[0,0,0]].
# Then, the player went left, up, up, left to return home, picking up one more
# cherry.
# The total number of cherries picked up is 5, and this is the maximum
# possible.
# 
# 
# Example 2:
# 
# 
# Input: grid = [[1,1,-1],[1,-1,1],[-1,1,1]]
# Output: 0
# 
# 
# 
# Constraints:
# 
# 
# n == grid.length
# n == grid[i].length
# 1 <= n <= 50
# grid[i][j] is -1, 0, or 1.
# grid[0][0] != -1
# grid[n - 1][n - 1] != -1
# 
# 
#

# @lc code=start
import sys

class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        if not grid or len(grid) == 0 or len(grid[0]) == 0:
            return 0

        n = len(grid)

        f = [[[0 for _ in range(n + 1)] for _ in range(n + 1)] for _ in range(n + 1)]
        for i in range(n + 1):
            for j in range(n + 1):
                for k in range(n + 1):
                    f[i][j][k] = -sys.maxsize - 1

        for i in range(1, n + 1):
            for j in range(1, n + 1):
                for k in range(1, n + 1):
                    
                    l = i + j - k
                    if l < 1 or l > n:
                        continue

                    if grid[i - 1][j - 1] == -1 or grid[k - 1][l - 1] == -1:
                        continue

                    if i == 1 and j == 1 and k == 1:
                        f[i][j][k] = grid[0][0]
                        continue

                    f[i][j][k] = max(
                        f[i][j][k],
                        f[i - 1][j][k - 1],
                        f[i - 1][j][k],
                        f[i][j - 1][k - 1],
                        f[i][j - 1][k]
                    )
                    
                    if i == k and j == l:
                        f[i][j][k] += grid[i - 1][j - 1]
                    else:
                        f[i][j][k] += grid[i - 1][j - 1] + grid[k - 1][l - 1]

        return max(0, f[n][n][n])
# @lc code=end

