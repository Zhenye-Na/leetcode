#
# @lc app=leetcode id=867 lang=python3
#
# [867] Transpose Matrix
#
# https://leetcode.com/problems/transpose-matrix/description/
#
# algorithms
# Easy (62.16%)
# Likes:    607
# Dislikes: 328
# Total Accepted:    95.4K
# Total Submissions: 153.9K
# Testcase Example:  '[[1,2,3],[4,5,6],[7,8,9]]'
#
# Given a 2D integer array matrix, return the transpose of matrix.
# 
# The transpose of a matrix is the matrix flipped over its main diagonal,
# switching the matrix's row and column indices.
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [[1,4,7],[2,5,8],[3,6,9]]
# 
# 
# Example 2:
# 
# 
# Input: matrix = [[1,2,3],[4,5,6]]
# Output: [[1,4],[2,5],[3,6]]
# 
# 
# 
# Constraints:
# 
# 
# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 1000
# 1 <= m * n <= 10^5
# -10^9 <= matrix[i][j] <= 10^9
# 
# 
#

# @lc code=start
class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        transpose = []
        for i in range(len(matrix[0])):
            row = []
            for j in range(len(matrix)):
                row.append(matrix[j][i])
            transpose.append(row)
        return transpose
# @lc code=end

