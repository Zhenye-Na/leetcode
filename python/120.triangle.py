#
# @lc app=leetcode id=120 lang=python3
#
# [120] Triangle
#
# https://leetcode.com/problems/triangle/description/
#
# algorithms
# Medium (45.55%)
# Likes:    3040
# Dislikes: 316
# Total Accepted:    310K
# Total Submissions: 661.7K
# Testcase Example:  '[[2],[3,4],[6,5,7],[4,1,8,3]]'
#
# Given a triangle array, return the minimum path sum from top to bottom.
# 
# For each step, you may move to an adjacent number of the row below. More
# formally, if you are on index i on the current row, you may move to either
# index i or index i + 1 on the next row.
# 
# 
# Example 1:
# 
# 
# Input: triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
# Output: 11
# Explanation: The triangle looks like:
# ⁠  2
# ⁠ 3 4
# ⁠6 5 7
# 4 1 8 3
# The minimum path sum from top to bottom is 2 + 3 + 5 + 1 = 11 (underlined
# above).
# 
# 
# Example 2:
# 
# 
# Input: triangle = [[-10]]
# Output: -10
# 
# 
# 
# Constraints:
# 
# 
# 1 <= triangle.length <= 200
# triangle[0].length == 1
# triangle[i].length == triangle[i - 1].length + 1
# -10^4 <= triangle[i][j] <= 10^4
# 
# 
# 
# Follow up: Could you do this using only O(n) extra space, where n is the
# total number of rows in the triangle?
#

# @lc code=start
# Time O(n^2)
# Space O(n)
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if not triangle or len(triangle) == 0:
            return 0

        n = len(triangle)

        # dp initialization
        f = [[0 for _ in range(n)] for _ in range(2)]
        f[0][0] = triangle[0][0]

        for i in range(1, n):
            for j in range(i + 1):
                if j == 0:
                    f[i % 2][j] = f[(i - 1) % 2][0] + triangle[i][0]
                elif j == i:
                    f[i % 2][j] = f[(i - 1) % 2][j - 1] + triangle[i][j]
                else:
                    f[i % 2][j] = triangle[i][j] + min(
                        f[(i - 1) % 2][j],
                        f[(i - 1) % 2][j - 1]
                    )

        return min(f[(n - 1) % 2])


# Time O(n^2)
# Space O(n^2)
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if not triangle or len(triangle) == 0:
            return 0

        n = len(triangle)

        # dp initialization
        f = [[0 for _ in range(n)] for _ in range(n)]
        f[0][0] = triangle[0][0]

        for i in range(1, n):
            f[i][0] = f[i - 1][0] + triangle[i][0]
            f[i][i] = f[i - 1][i - 1] + triangle[i][i]

        for i in range(1, n):
            for j in range(1, i):
                f[i][j] = triangle[i][j] + min(
                    f[i - 1][j],
                    f[i - 1][j - 1]
                )

        return min(f[-1])
# @lc code=end

