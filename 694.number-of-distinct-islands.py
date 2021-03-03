# 694. Number of Distinct Islands
#
# Description
#
# Given a non-empty 2D array grid of 0's and 1's,
#
# an island is a group of 1's (representing land)
# connected 4-directionally (horizontal or vertical).
#
# You may assume all four edges of the grid are surrounded by water.
#
# Count the number of distinct islands. An island is considered to be the
# same as another if and only if one island has the same shape as another
# island (and not rotated or reflected).
#
# Notice that:

# ```
# 11
# 1
# ```

# and

# ```
#  1
# 11
# ```

# are considered `different` island, because we do not consider reflection / rotation.

# The length of each dimension in the given grid does not exceed 50.

# Example

# Example 1:

# Input: 
#   [
#     [1,1,0,0,1],
#     [1,0,0,0,0],
#     [1,1,0,0,1],
#     [0,1,0,1,1]
#   ]
# Output: 3

# Explanation:
#   11   1    1
#   1        11   
#   11
#    1


# Example 2:

# Input:
#   [
#     [1,1,0,0,0],
#     [1,1,0,0,0],
#     [0,0,0,1,1],
#     [0,0,0,1,1]
#   ]
# Output: 1
# 11
# 11

from collections import deque

class Solution:
    """
    @param grid: a list of lists of integers
    @return: return an integer, denote the number of distinct islands
    """
    def __init__(self):
        self.directions = [[0,1],[1,0],[0,-1],[-1,0]]


    def numberofDistinctIslands(self, grid):
        # write your code here
        self.m, self.n = len(grid), len(grid[0])
        self.grid = grid
        self.seen = set([])
        self.shapes = set([])

        self.island = 0
        for i in range(self.m):
            for j in range(self.n):
                if self.grid[i][j] == 1:
                    self._bfs(i, j)

        return self.island


    def _bfs(self, i, j):
        queue = deque([(i, j)])
        self.seen.add((i, j))
        
        islands = []
        while queue:
            x, y = queue.popleft()
            islands.append([x, y])
            for d in self.directions:
                new_x, new_y = x + d[0], y + d[1]
                if self._valid(new_x, new_y):
                    queue.append((new_x, new_y))
                    self.seen.add((new_x, new_y))
                    self.grid[new_x][new_y] = 0

        # hash island shape
        min_x, min_y = self.m, self.n
        for island in islands:
            min_x = min(min_x, island[0])
            min_y = min(min_y, island[1])

        for i in range(len(islands)):
            islands[i][0] -= min_x
            islands[i][1] -= min_y

        islands.sort()
        islands = tuple(tuple(island) for island in islands)

        if islands not in self.shapes:
            self.island += 1
            self.shapes.add(islands)


    def _valid(self, x, y):
        return 0 <= x < self.m and 0 <= y < self.n and (x, y) not in self.seen and self.grid[x][y] == 1


# Time Complexity:
#   Worst case: O(mn)
# Space Complexity:
#   Worst case: O(mn)


# DFS Solution:
#  record the direction in each recursive call
#  https://www.youtube.com/watch?v=c1ZxUOHlulo&list=PLtQWXpf5JNGJagakc_kBtOH5-gd8btjEW&index=3&ab_channel=MichaelMuinos