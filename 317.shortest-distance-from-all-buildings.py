# [317] Shortest Distance from All Buildings
#
# Description
#
# You want to build a house on an empty land which reaches all
# buildings in the shortest amount of distance. You can only
# move up, down, left and right.
#
# You are given a 2D grid of values 0, 1 or 2, where:
#
# Each 0 marks an empty land which you can pass by freely.
# Each 1 marks a building which you cannot pass through.
# Each 2 marks an obstacle which you cannot pass through.
#
# Example
#
# Example 1
#
# Input: [[1,0,2,0,1],[0,0,0,0,0],[0,0,1,0,0]]
# Output: 7
# Explanation:
# In this example, there are three buildings at (0,0), (0,4), (2,2),
# and an obstacle at (0,2).
#
# 1 - 0 - 2 - 0 - 1
# |   |   |   |   |
# 0 - 0 - 0 - 0 - 0
# |   |   |   |   |
# 0 - 0 - 1 - 0 - 0
#
# The point (1,2) is an ideal empty land to build a house, as the
# total travel distance of 3+3+1=7 is minimal. So return 7.
#
# Example 2
#
# Input: [[1,0],[0,0]]
# Output: 1
# In this example, there is one buildings at (0,0).
#
# 1 - 0
# |   |
# 0 - 0
#
# The point (1,0) or (0,1) is an ideal empty land to build a house,
# as the total travel distance of 1 is minimal. So return 1.
#
from collections import deque, defaultdict

import sys
class Solution:
    """
    @param grid: the 2D grid
    @return: the shortest distance
    """
    def __init__(self):
        self.min_dist = defaultdict(int)
        self.reachable_count = defaultdict(int)

        self.directions = [[0,1],[1,0],[0,-1],[-1,0]]

        self.obstacle = 2
        self.building = 1
        self.empty = 0

    def shortestDistance(self, grid):
        # write your code here
        if not grid or len(grid) == 0 or len(grid[0]) == 0:
            return 0

        m, n = len(grid), len(grid[0])
        buildings = []
        for i in range(m):
            for j in range(n):
                if grid[i][j] == self.building:
                    buildings.append((i, j))

        for building in buildings:
            queue = deque([building])
            distance = 0
            visited = set([building])

            while queue:
                size = len(queue)
                for _ in range(size):
                    x, y = queue.popleft()
                    if grid[x][y] != self.building:
                        self.min_dist[(x, y)] += distance
                        self.reachable_count[(x, y)] += 1
                    for i in range(4):
                        next_x, next_y = x + self.directions[i][0], y + self.directions[i][1]

                        if self._is_valid(next_x, next_y, m, n, visited, grid):
                            queue.append((next_x, next_y))
                            visited.add((next_x, next_y))
                distance += 1

        min_distance = sys.maxsize
        for cordinate in self.reachable_count:
            if self.reachable_count[cordinate] == len(buildings):
                min_distance = min(min_distance, self.min_dist[cordinate])

        return min_distance

    def _is_valid(self, x, y, m, n, visited, grid):
        return 0 <= x < m and 0 <= y < n and (x, y) not in visited and grid[x][y] == self.empty

