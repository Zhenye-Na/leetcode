#
# @lc app=leetcode id=994 lang=python3
#
# [994] Rotting Oranges
#
# https://leetcode.com/problems/rotting-oranges/description/
#
# algorithms
# Medium (53.52%)
# Likes:    13007
# Dislikes: 408
# Total Accepted:    947.2K
# Total Submissions: 1.7M
# Testcase Example:  '[[2,1,1],[1,1,0],[0,1,1]]'
#
# You are given an m x n grid where each cell can have one of three
# values:
#
#
# 0 representing an empty cell,
# 1 representing a fresh orange, or
# 2 representing a rotten orange.
#
#
# Every minute, any fresh orange that is 4-directionally adjacent to a rotten
# orange becomes rotten.
#
# Return the minimum number of minutes that must elapse until no cell has a
# fresh orange. If this is impossible, return -1.
#
#
# Example 1:
#
#
# Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
# Output: 4
#
#
# Example 2:
#
#
# Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
# Output: -1
# Explanation: The orange in the bottom left corner (row 2, column 0) is never
# rotten, because rotting only happens 4-directionally.
#
#
# Example 3:
#
#
# Input: grid = [[0,2]]
# Output: 0
# Explanation: Since there are already no fresh oranges at minute 0, the answer
# is just 0.
#
#
#
# Constraints:
#
#
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 10
# grid[i][j] is 0, 1, or 2.
#
#
#

# @lc code=start
from collections import deque
import sys
from typing import List


class Solution:

    def __init__(self):
        self.EMPTY = 0
        self.ORANGE = 1
        self.ROTTEN = 2

        self.dx = [-1, 1, 0, 0]
        self.dy = [0, 0, 1, -1]

    def orangesRotting(self, grid: List[List[int]]) -> int:

        if not grid or len(grid) == 0 or len(grid[0]) == 0:
            return -1

        self.n, self.m = len(grid), len(grid[0])
        time = [[sys.maxsize for _ in range(self.m)] for _ in range(self.n)]
        visited = set()

        queue = deque([])
        for i in range(self.n):
            for j in range(self.m):
                if grid[i][j] == self.ROTTEN:
                    queue.append((i, j))
                    time[i][j] = 0
                    visited.add((i, j))

        curr_time = 0
        while queue:
            size = len(queue)
            for _ in range(size):
                curr_x, curr_y = queue.popleft()
                for d in range(4):
                    next_x, next_y = curr_x + self.dx[d], curr_y + self.dy[d]
                    if (
                        self._is_valid(next_x, next_y, grid)
                        and (next_x, next_y) not in visited
                    ):
                        queue.append((next_x, next_y))
                        visited.add((next_x, next_y))
                        time[next_x][next_y] = time[curr_x][curr_y] + 1
            curr_time += 1

        res = 0
        for i in range(self.n):
            for j in range(self.m):
                if grid[i][j] == self.ORANGE:
                    res = max(res, time[i][j])

        return res if res != sys.maxsize else -1

    def _is_valid(self, next_x, next_y, grid):
        return (
            0 <= next_x < self.n
            and 0 <= next_y < self.m
            and grid[next_x][next_y] == self.ORANGE
        )


# @lc code=end
