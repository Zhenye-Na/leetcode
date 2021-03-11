#
# @lc app=leetcode id=1091 lang=python3
#
# [1091] Shortest Path in Binary Matrix
#
# https://leetcode.com/problems/shortest-path-in-binary-matrix/description/
#
# algorithms
# Medium (39.00%)
# Likes:    1096
# Dislikes: 74
# Total Accepted:    79.2K
# Total Submissions: 197.8K
# Testcase Example:  '[[0,1],[1,0]]'
#
# Given an n x n binary matrix grid, return the length of the shortest clear
# path in the matrix. If there is no clear path, return -1.
# 
# A clear path in a binary matrix is a path from the top-left cell (i.e., (0,
# 0)) to the bottom-right cell (i.e., (n - 1, n - 1)) such that:
# 
# 
# All the visited cells of the path are 0.
# All the adjacent cells of the path are 8-directionally connected (i.e., they
# are different and they share an edge or a corner).
# 
# 
# The length of a clear path is the number of visited cells of this path.
# 
# 
# Example 1:
# 
# 
# Input: grid = [[0,1],[1,0]]
# Output: 2
# 
# 
# Example 2:
# 
# 
# Input: grid = [[0,0,0],[1,1,0],[1,1,0]]
# Output: 4
# 
# 
# Example 3:
# 
# 
# Input: grid = [[1,0,0],[1,1,0],[1,1,0]]
# Output: -1
# 
# 
# 
# Constraints:
# 
# 
# n == grid.length
# n == grid[i].length
# 1 <= n <= 100
# grid[i][j] is 0 or 1
# 
# 
#

# @lc code=start
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
# @lc code=end

