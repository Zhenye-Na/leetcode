#
# @lc app=leetcode id=59 lang=python3
#
# [59] Spiral Matrix II
#
# https://leetcode.com/problems/spiral-matrix-ii/description/
#
# algorithms
# Medium (57.52%)
# Likes:    1559
# Dislikes: 126
# Total Accepted:    243.7K
# Total Submissions: 421K
# Testcase Example:  '3'
#
# Given a positive integer n, generate an n x n matrix filled with elements
# from 1 to n^2 in spiral order.
# 
# 
# Example 1:
# 
# 
# Input: n = 3
# Output: [[1,2,3],[8,9,4],[7,6,5]]
# 
# 
# Example 2:
# 
# 
# Input: n = 1
# Output: [[1]]
# 
# 
# 
# Constraints:
# 
# 
# 1 <= n <= 20
# 
# 
#

# @lc code=start
class Solution:

    def __init__(self):
        self.directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]

    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0 for _ in range(n)] for _ in range(n)]
        seen = set([])
        batch = 0
        x, y = 0, 0

        for num in range(1, n * n + 1):
            matrix[x][y] = num
            seen.add((x, y))

            next_x = x + self.directions[batch % 4][0]
            next_y = y + self.directions[batch % 4][1]

            if not self._is_valid(next_x, next_y, n, seen):
                batch += 1
                next_x = x + self.directions[batch % 4][0]
                next_y = y + self.directions[batch % 4][1]

            x, y = next_x, next_y

        return matrix

    def _is_valid(self, x, y, n, seen):
        return 0 <= x < n and 0 <= y < n and (x, y) not in seen

# @lc code=end

