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
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or len(matrix) == 0 or len(matrix[0]) == 0:
            return []

        history = [[False] * len(matrix[0]) for _ in range(len(matrix))]
        x, y = 0, 0

        directions = {
            0: [0, 1],
            1: [1, 0],
            2: [0, -1],
            3: [-1, 0],
        }

        r, c = len(matrix), len(matrix[0])
        res = []
        d = 0
        for _ in range(r * c):
            res.append(matrix[x][y])
            history[x][y] = True

            nx = x + directions[d][0]
            ny = y + directions[d][1]

            if not ( 0 <= nx < r and 0 <= ny < c and not history[nx][ny] ):
                d = (d + 1) % 4

                nx = x + directions[d][0]
                ny = y + directions[d][1]

            x, y = nx, ny

        return res
# @lc code=end

