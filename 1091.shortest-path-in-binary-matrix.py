#
# @lc app=leetcode id=1091 lang=python3
#
# [1091] Shortest Path in Binary Matrix
#

"""
In an N by N square grid, each cell is either empty (0) or blocked (1).

A clear path from top-left to bottom-right has length k if and only if it is composed of cells C_1, C_2, ..., C_k such that:

Adjacent cells C_i and C_{i+1} are connected 8-directionally (ie., they are different and share an edge or corner)
C_1 is at location (0, 0) (ie. has value grid[0][0])
C_k is at location (N-1, N-1) (ie. has value grid[N-1][N-1])
If C_i is located at (r, c), then grid[r][c] is empty (ie. grid[r][c] == 0).
Return the length of the shortest such clear path from top-left to bottom-right.  If such a path does not exist, return -1.


Example 1:

Input: [[0,1],[1,0]]
Output: 2


Example 2:

Input: [[0,0,0],[1,1,0],[1,1,0]]
Output: 4
 

Note:

1 <= grid.length == grid[0].length <= 100
grid[i][j] is 0 or 1
"""

from collections import deque

class Solution(object):
    EMPTY = 0
    BLOCK = 1
    
    DIRECTIONS = [[-1, -1], [-1, 1], [1, -1], [1, 1], [0, 1], [0, -1], [1, 0], [-1, 0]]
    
    def shortestPathBinaryMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or len(grid) == 0 or len(grid[0]) == 0 or grid[0][0] != self.EMPTY or grid[len(grid) - 1][len(grid[0]) - 1] != self.EMPTY:
            return -1

        m, n = len(grid), len(grid[0])
        
        step = 1
        queue = deque([(0, 0)])
        visited = set([(0, 0)])
        while queue:
            step += 1
            size = len(queue)
            for _ in range(size):
                x, y = queue.popleft()
                for d in self.DIRECTIONS:
                    x_, y_ = x + d[0], y + d[1]
                    if self._inBound(x_, y_, m, n, grid, visited):
                        if x_ == m - 1 and y_ == n - 1:
                            return step
                        queue.append((x_, y_))
                        visited.add((x_, y_))
                        
        return -1
            
            
    def _inBound(self, x, y, m, n, grid, visited):
        return 0 <= x < m and  0 <= y < n and grid[x][y] == self.EMPTY and (x, y) not in visited
