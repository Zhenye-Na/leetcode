#
# @lc app=leetcode id=329 lang=python3
#
# [329] Longest Increasing Path in a Matrix
#
# https://leetcode.com/problems/longest-increasing-path-in-a-matrix/description/
#
# algorithms
# Hard (44.55%)
# Likes:    2858
# Dislikes: 52
# Total Accepted:    200.4K
# Total Submissions: 442.8K
# Testcase Example:  '[[9,9,4],[6,6,8],[2,1,1]]'
#
# Given an m x n integers matrix, return the length of the longest increasing
# path in matrix.
# 
# From each cell, you can either move in four directions: left, right, up, or
# down. You may not move diagonally or move outside the boundary (i.e.,
# wrap-around is not allowed).
# 
# 
# Example 1:
# 
# 
# Input: matrix = [[9,9,4],[6,6,8],[2,1,1]]
# Output: 4
# Explanation: The longest increasing path is [1, 2, 6, 9].
# 
# 
# Example 2:
# 
# 
# Input: matrix = [[3,4,5],[3,2,6],[2,2,1]]
# Output: 4
# Explanation: The longest increasing path is [3, 4, 5, 6]. Moving diagonally
# is not allowed.
# 
# 
# Example 3:
# 
# 
# Input: matrix = [[1]]
# Output: 1
# 
# 
# 
# Constraints:
# 
# 
# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 200
# 0 <= matrix[i][j] <= 2^31 - 1
# 
# 
#

# @lc code=start
class Solution:

    def __init__(self):
        self.memo = {}
        self.dx = [0, 0, 1, -1]
        self.dy = [1, -1, 0, 0]


    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        length = 0

        for i in range(m):
            for j in range(n):
                length = max(length, self.dfs(i, j, matrix))

        return length


    def dfs(self, x, y, matrix):
        if (x, y) in self.memo:
            return self.memo[(x, y)]

        curr_length = 1
        next_length = 0
        for i in range(4):
            next_x, next_y = x + self.dx[i], y + self.dy[i]
            if self.inbound(next_x, next_y, matrix) and matrix[next_x][next_y] > matrix[x][y]:
                next_length = max(next_length, self.dfs(next_x, next_y, matrix))

        self.memo[(x, y)] = curr_length + next_length

        return self.memo[(x, y)]


    def inbound(self, x, y, matrix):
        return 0 <= x < len(matrix) and 0 <= y < len(matrix[0])
# @lc code=end

