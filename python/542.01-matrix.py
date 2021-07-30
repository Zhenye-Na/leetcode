#
# @lc app=leetcode id=542 lang=python3
#
# [542] 01 Matrix
#
# https://leetcode.com/problems/01-matrix/description/
#
# algorithms
# Medium (41.79%)
# Likes:    2906
# Dislikes: 143
# Total Accepted:    154.7K
# Total Submissions: 362.3K
# Testcase Example:  '[[0,0,0],[0,1,0],[0,0,0]]'
#
# Given an m x n binary matrix matrix, return the distance of the nearest 0 for
# each cell.
# 
# The distance between two adjacent cells is 1.
# 
# 
# Example 1:
# 
# 
# Input: matrix = [[0,0,0],[0,1,0],[0,0,0]]
# Output: [[0,0,0],[0,1,0],[0,0,0]]
# 
# 
# Example 2:
# 
# 
# Input: matrix = [[0,0,0],[0,1,0],[1,1,1]]
# Output: [[0,0,0],[0,1,0],[1,2,1]]
# 
# 
# 
# Constraints:
# 
# 
# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 10^4
# 1 <= m * n <= 10^4
# matrix[i][j] is either 0 or 1.
# There is at least one 0 in matrix.
# 
# 
#

# @lc code=start
import sys

from collections import deque

class Solution:

    def __init__(self):
        self.dx = [1, -1, 0, 0]
        self.dy = [0, 0, 1, -1]
    
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:

        if not matrix or len(matrix) == 0 or len(matrix[0]) == 0:
            return matrix

        n, m = len(matrix), len(matrix[0])
        dist = [[0 for _ in range(m)] for _ in range(n)]
        queue = deque([])

        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    dist[i][j] = 0
                    queue.append([i, j])
                else:
                    dist[i][j] = sys.maxsize
        
        while queue:
            x, y = queue.popleft()
            for d in range(4):
                next_x, next_y = x + self.dx[d], y + self.dy[d]
                if self.isValid(next_x, next_y, matrix):
                    if (dist[next_x][next_y] > dist[x][y] + 1):
                        dist[next_x][next_y] = dist[x][y] + 1
                        queue.append([next_x, next_y])

        return dist


    def isValid(self, x, y, matrix):
        return 0 <= x < len(matrix) and 0 <= y < len(matrix[0])

# @lc code=end

