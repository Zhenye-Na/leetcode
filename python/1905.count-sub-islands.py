#
# @lc app=leetcode id=1905 lang=python3
#
# [1905] Count Sub Islands
#
# https://leetcode.com/problems/count-sub-islands/description/
#
# algorithms
# Medium (67.49%)
# Likes:    2158
# Dislikes: 68
# Total Accepted:    111.9K
# Total Submissions: 162.5K
# Testcase Example:  '[[1,1,1,0,0],[0,1,1,1,1],[0,0,0,0,0],[1,0,0,0,0],[1,1,0,1,1]]\n' +
#   '[[1,1,1,0,0],[0,0,1,1,1],[0,1,0,0,0],[1,0,1,1,0],[0,1,0,1,0]]'
#
# You are given two m x n binary matrices grid1 and grid2 containing only 0's
# (representing water) and 1's (representing land). An island is a group of 1's
# connected 4-directionally (horizontal or vertical). Any cells outside of the
# grid are considered water cells.
#
# An island in grid2 is considered a sub-island if there is an island in grid1
# that contains all the cells that make up this island in grid2.
#
# Return the number of islands in grid2 that are considered sub-islands.
#
#
# Example 1:
#
#
# Input: grid1 = [[1,1,1,0,0],[0,1,1,1,1],[0,0,0,0,0],[1,0,0,0,0],[1,1,0,1,1]],
# grid2 = [[1,1,1,0,0],[0,0,1,1,1],[0,1,0,0,0],[1,0,1,1,0],[0,1,0,1,0]]
# Output: 3
# Explanation: In the picture above, the grid on the left is grid1 and the grid
# on the right is grid2.
# The 1s colored red in grid2 are those considered to be part of a sub-island.
# There are three sub-islands.
#
#
# Example 2:
#
#
# Input: grid1 = [[1,0,1,0,1],[1,1,1,1,1],[0,0,0,0,0],[1,1,1,1,1],[1,0,1,0,1]],
# grid2 = [[0,0,0,0,0],[1,1,1,1,1],[0,1,0,1,0],[0,1,0,1,0],[1,0,0,0,1]]
# Output: 2
# Explanation: In the picture above, the grid on the left is grid1 and the grid
# on the right is grid2.
# The 1s colored red in grid2 are those considered to be part of a sub-island.
# There are two sub-islands.
#
#
#
# Constraints:
#
#
# m == grid1.length == grid2.length
# n == grid1[i].length == grid2[i].length
# 1 <= m, n <= 500
# grid1[i][j] and grid2[i][j] are either 0 or 1.
#
#
#

# @lc code=start
from typing import List
from collections import deque


class Solution:
    def __init__(self):
        self.ISLAND = 1
        self.WATER = 0

        self.dx = [1, -1, 0, 0]
        self.dy = [0, 0, 1, -1]

    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        res = 0
        n, m = len(grid2), len(grid2[0])

        for i in range(n):
            for j in range(m):
                if grid2[i][j] == self.ISLAND:
                    if self._bfs(i, j, grid1, grid2):
                        res += 1

        return res

    def _bfs(self, x, y, grid1, grid2):
        is_sub_island = True
        queue = deque([(x, y)])

        grid2[x][y] = self.WATER

        while queue:
            curr_x, curr_y = queue.popleft()

            if grid1[curr_x][curr_y] == self.WATER:
                is_sub_island = False

            for d in range(4):
                next_x, next_y = curr_x + self.dx[d], curr_y + self.dy[d]

                if self._validate_next(next_x, next_y, grid2):
                    grid2[next_x][next_y] = self.WATER
                    queue.append((next_x, next_y))

        return is_sub_island

    def _validate_next(self, x, y, grid):
        return (
            0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == self.ISLAND
        )


# @lc code=end
