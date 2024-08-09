#
# @lc app=leetcode id=840 lang=python3
#
# [840] Magic Squares In Grid
#
# https://leetcode.com/problems/magic-squares-in-grid/description/
#
# algorithms
# Medium (38.75%)
# Likes:    764
# Dislikes: 1795
# Total Accepted:    126.9K
# Total Submissions: 248.3K
# Testcase Example:  '[[4,3,8,4],[9,5,1,9],[2,7,6,2]]'
#
# A 3 x 3 magic square is a 3 x 3 grid filled with distinct numbers from 1 to 9
# such that each row, column, and both diagonals all have the same sum.
#
# Given a row x col grid of integers, how many 3 x 3 contiguous magic square
# subgrids are there?
#
# Note: while a magic square can only contain numbers from 1 to 9, grid may
# contain numbers up to 15.
#
#
# Example 1:
#
#
# Input: grid = [[4,3,8,4],[9,5,1,9],[2,7,6,2]]
# Output: 1
# Explanation:
# The following subgrid is a 3 x 3 magic square:
#
# while this one is not:
#
# In total, there is only one magic square inside the given grid.
#
#
# Example 2:
#
#
# Input: grid = [[8]]
# Output: 0
#
#
#
# Constraints:
#
#
# row == grid.length
# col == grid[i].length
# 1 <= row, col <= 10
# 0 <= grid[i][j] <= 15
#
#
#


# @lc code=start
from typing import List


class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        i, j = 0, 0
        res = 0

        for i in range(n - 2):
            for j in range(m - 2):
                matrix = self._get_sub_matrix(grid, i, j)
                if self._is_matrix_magic(matrix) and self._is_distinct_matrix(matrix):
                    res += 1

        return res

    def _get_sub_matrix(self, matrix, start_row, start_col):
        return [
            row[start_col : start_col + 3] for row in matrix[start_row : start_row + 3]
        ]

    def _is_matrix_magic(self, matrix):
        transposed_matrix = list(map(list, zip(*matrix)))
        return (
            sum(matrix[0]) == sum(matrix[1]) == sum(matrix[2])
            and sum(transposed_matrix[0])
            == sum(transposed_matrix[1])
            == sum(transposed_matrix[2])
            and matrix[0][0] + matrix[2][2] == matrix[0][2] + matrix[2][0]
        )

    def _is_distinct_matrix(self, matrix):
        all_nums = list(set([num for row in matrix for num in row]))
        all_nums.sort()
        return len(all_nums) == 9 and min(all_nums) == 1 and max(all_nums) == 9


# @lc code=end
