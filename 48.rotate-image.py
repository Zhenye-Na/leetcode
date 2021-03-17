#
# @lc app=leetcode id=48 lang=python3
#
# [48] Rotate Image
#
# https://leetcode.com/problems/rotate-image/description/
#
# algorithms
# Medium (59.50%)
# Likes:    4486
# Dislikes: 326
# Total Accepted:    541.2K
# Total Submissions: 899.5K
# Testcase Example:  '[[1,2,3],[4,5,6],[7,8,9]]'
#
# You are given an n x n 2D matrix representing an image, rotate the image by
# 90 degrees (clockwise).
# 
# You have to rotate the image in-place, which means you have to modify the
# input 2D matrix directly. DO NOT allocate another 2D matrix and do the
# rotation.
# 
# 
# Example 1:
# 
# 
# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [[7,4,1],[8,5,2],[9,6,3]]
# 
# 
# Example 2:
# 
# 
# Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
# Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
# 
# 
# Example 3:
# 
# 
# Input: matrix = [[1]]
# Output: [[1]]
# 
# 
# Example 4:
# 
# 
# Input: matrix = [[1,2],[3,4]]
# Output: [[3,1],[4,2]]
# 
# 
# 
# Constraints:
# 
# 
# matrix.length == n
# matrix[i].length == n
# 1 <= n <= 20
# -1000 <= matrix[i][j] <= 1000
# 
# 
#

# @lc code=start
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)

        # transpose the matrix
        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for i in range(n):
            left, right = 0, n - 1
            while left <= right:
                matrix[i][left], matrix[i][right] = matrix[i][right], matrix[i][left]
                left += 1
                right -= 1


class Solution_Second:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if not matrix or len(matrix) == 0 or len(matrix[0]) == 0:
            return

        m, n = len(matrix), len(matrix[0])
        tmp = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                tmp[j][n - 1 - i] = matrix[i][j]

        for i in range(m):
            for j in range(n):
                matrix[i][j] = tmp[i][j]
# @lc code=end

