#
# @lc app=leetcode id=304 lang=python3
#
# [304] Range Sum Query 2D - Immutable
#
# https://leetcode.com/problems/range-sum-query-2d-immutable/description/
#
# algorithms
# Medium (40.30%)
# Likes:    1413
# Dislikes: 207
# Total Accepted:    145.5K
# Total Submissions: 357.9K
# Testcase Example:  '["NumMatrix","sumRegion","sumRegion","sumRegion"]\n' +
# '[[[[3,0,1,4,2],[5,6,3,2,1],[1,2,0,1,5],[4,1,0,1,7],[1,0,3,0,5]]],[2,1,4,3],[1,1,2,2],[1,2,2,4]]'
#
# Given a 2D matrix matrix, find the sum of the elements inside the rectangle
# defined by its upper left corner (row1, col1) and lower right corner (row2,
# col2).
# 
# Implement the NumMatrix class:
# 
# 
# NumMatrix(int[][] matrix) initializes the object with the integer matrix
# matrix.
# int sumRegion(int row1, int col1, int row2, int col2) returns the sum of the
# elements of the matrix array inside the rectangle defined by its upper left
# corner (row1, col1) and lower right corner (row2, col2).
# 
# 
# 
# Example 1:
# 
# 
# Input
# ["NumMatrix", "sumRegion", "sumRegion", "sumRegion"]
# [[[[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0,
# 3, 0, 5]]], [2, 1, 4, 3], [1, 1, 2, 2], [1, 2, 2, 4]]
# Output
# [null, 8, 11, 12]
# 
# Explanation
# NumMatrix numMatrix = new NumMatrix([[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2,
# 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]);
# numMatrix.sumRegion(2, 1, 4, 3); // return 8 (i.e sum of the red rectangele).
# numMatrix.sumRegion(1, 1, 2, 2); // return 11 (i.e sum of the green
# rectangele).
# numMatrix.sumRegion(1, 2, 2, 4); // return 12 (i.e sum of the blue
# rectangele).
# 
# 
# 
# Constraints:
# 
# 
# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 200
# -10^5 <= matrix[i][j] <= 10^5
# 0 <= row1 <= row2 < m
# 0 <= col1 <= col2 < n
# At most 10^4 calls will be made to sumRegion.
# 
# 
#

# @lc code=start

# Dynamic Programming
#   O(mn) to preprocess
#   O(1) to query
#   https://www.youtube.com/watch?v=MSNSqU3BnXk&ab_channel=HuaHua
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        if not matrix or len(matrix) == 0 or len(matrix[0]) == 0:
            return
        row, col = len(matrix), len(matrix[0])
        self.prefix_matrix = [[0 for _ in range(col + 1)] for _ in range(row + 1)]
        for i in range(1, len(self.prefix_matrix)):
            for j in range(1, len(self.prefix_matrix[0])):
                self.prefix_matrix[i][j] = matrix[i - 1][j - 1] \
                                   + self.prefix_matrix[i - 1][j] \
                                   + self.prefix_matrix[i][j - 1] \
                                   - self.prefix_matrix[i - 1][j - 1]


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.prefix_matrix[row2 + 1][col2 + 1] \
             - self.prefix_matrix[row2 + 1][col1] \
             - self.prefix_matrix[row1][col2 + 1] \
             + self.prefix_matrix[row1][col1]



# Prefix Sum Matrix
# Pre-process prefix sum for each row
# Time Complexity:
#   O(row2 - row1): for loop in sumRegion method
#   O(mn): contruct prefix matrix
#   Overall O(mn)

class NumMatrix_PrefixSum:

    def __init__(self, matrix: List[List[int]]):
        row, col = len(matrix), len(matrix[0])
        self.prefix_matrix = [[0 for _ in range(col + 1)] for _ in range(row)]
        for i in range(row):
            prefix_sum = 0
            for j in range(col):
                prefix_sum += matrix[i][j]
                self.prefix_matrix[i][j + 1] = prefix_sum


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row_range = [i for i in range(row1, row2 + 1)]
        running_sum = 0
        for row in row_range:
            left_sum = self.prefix_matrix[row][col1] if col1 >= 0 else 0
            running_sum += self.prefix_matrix[row][col2 + 1] - left_sum

        return running_sum

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
# @lc code=end

