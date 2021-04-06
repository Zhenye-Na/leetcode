#
# @lc app=leetcode id=54 lang=python3
#
# [54] Spiral Matrix
#
# https://leetcode.com/problems/spiral-matrix/description/
#
# algorithms
# Medium (31.73%)
# Likes:    1438
# Dislikes: 458
# Total Accepted:    277.1K
# Total Submissions: 873K
# Testcase Example:  '[[1,2,3],[4,5,6],[7,8,9]]'
#
# Given a matrix of m x n elements (m rows, n columns), return all elements of
# the matrix in spiral order.
# 
# Example 1:
# 
# 
# Input:
# [
# ⁠[ 1, 2, 3 ],
# ⁠[ 4, 5, 6 ],
# ⁠[ 7, 8, 9 ]
# ]
# Output: [1,2,3,6,9,8,7,4,5]
# 
# 
# Example 2:
# 
# Input:
# [
# ⁠ [1, 2, 3, 4],
# ⁠ [5, 6, 7, 8],
# ⁠ [9,10,11,12]
# ]
# Output: [1,2,3,4,8,12,11,10,9,5,6,7]
# 
#

# @lc code=start
class Solution:
    def __init__(self):
        self.directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]

    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or len(matrix) == 0 or len(matrix[0]) == 0:
            return []

        seen = set([])
        res = []
        batch = 0
        m, n = len(matrix), len(matrix[0])
        i, j = 0, 0
        for _ in range(m * n):
            res.append(matrix[i][j])
            seen.add((i, j))
            next_i, next_j = i + self.directions[batch % 4][0], j + self.directions[batch % 4][1]

            if not self._is_valid(next_i, next_j, m, n, seen):
                batch += 1
                next_i, next_j = i + self.directions[batch % 4][0], j + self.directions[batch % 4][1]

            i, j = next_i, next_j

        return res

    def _is_valid(self, x, y, m, n, seen):
        return 0 <= x < m and 0 <= y < n and (x, y) not in seen
# @lc code=end

