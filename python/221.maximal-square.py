#
# @lc app=leetcode id=221 lang=python3
#
# [221] Maximal Square
#
# https://leetcode.com/problems/maximal-square/description/
#
# algorithms
# Medium (38.86%)
# Likes:    4304
# Dislikes: 105
# Total Accepted:    341.6K
# Total Submissions: 868K
# Testcase Example:  '[["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]'
#
# Given an m x n binary matrix filled with 0's and 1's, find the largest square
# containing only 1's and return its area.
# 
# 
# Example 1:
# 
# 
# Input: matrix =
# [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
# Output: 4
# 
# 
# Example 2:
# 
# 
# Input: matrix = [["0","1"],["1","0"]]
# Output: 1
# 
# 
# Example 3:
# 
# 
# Input: matrix = [["0"]]
# Output: 0
# 
# 
# 
# Constraints:
# 
# 
# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 300
# matrix[i][j] is '0' or '1'.
# 
# 
#

# @lc code=start
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix or len(matrix) == 0 or len(matrix[0]) == 0:
            return 0

        m, n = len(matrix), len(matrix[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]

        max_area = 0
        for i in range(m):
            for j in range(n):
                dp[i][j] = 0 if matrix[i][j] == '0' else 1
                if dp[i][j] == 0:
                    continue

                if i == 0 or j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = min(
                        dp[i - 1][j - 1],
                        dp[i][j - 1],
                        dp[i - 1][j]
                    ) + 1

                max_area = max(max_area, dp[i][j] * dp[i][j])

        return max_area

# @lc code=end

