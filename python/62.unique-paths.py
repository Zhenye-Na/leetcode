#
# @lc app=leetcode id=62 lang=python3
#
# [62] Unique Paths
#
# https://leetcode.com/problems/unique-paths/description/
#
# algorithms
# Medium (55.72%)
# Likes:    4791
# Dislikes: 240
# Total Accepted:    617.4K
# Total Submissions: 1.1M
# Testcase Example:  '3\n7'
#
# A robot is located at the top-left corner of a m x n grid (marked 'Start' in
# the diagram below).
# 
# The robot can only move either down or right at any point in time. The robot
# is trying to reach the bottom-right corner of the grid (marked 'Finish' in
# the diagram below).
# 
# How many possible unique paths are there?
# 
# 
# Example 1:
# 
# 
# Input: m = 3, n = 7
# Output: 28
# 
# 
# Example 2:
# 
# 
# Input: m = 3, n = 2
# Output: 3
# Explanation:
# From the top-left corner, there are a total of 3 ways to reach the
# bottom-right corner:
# 1. Right -> Down -> Down
# 2. Down -> Down -> Right
# 3. Down -> Right -> Down
# 
# 
# Example 3:
# 
# 
# Input: m = 7, n = 3
# Output: 28
# 
# 
# Example 4:
# 
# 
# Input: m = 3, n = 3
# Output: 6
# 
# 
# 
# Constraints:
# 
# 
# 1 <= m, n <= 100
# It's guaranteed that the answer will be less than or equal to 2 * 10^9.
# 
# 
#

# @lc code=start
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 0 or n == 0:
            return 1

        # dp initialization
        # f[i][j] represents # of possible unique paths from (0,0) to (i,j)
        f = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            f[i][0] = 1

        for j in range(n):
            f[0][j] = 1

        f[0][0] = 1

        for i in range(1, m):
            for j in range(1, n):
                f[i][j] = f[i - 1][j] + f[i][j - 1]

        return f[-1][-1]
# @lc code=end

