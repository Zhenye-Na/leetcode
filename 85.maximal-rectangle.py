#
# @lc app=leetcode id=85 lang=python3
#
# [85] Maximal Rectangle
#
# https://leetcode.com/problems/maximal-rectangle/description/
#
# algorithms
# Hard (39.27%)
# Likes:    3989
# Dislikes: 86
# Total Accepted:    219.9K
# Total Submissions: 555.6K
# Testcase Example:  '[["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]'
#
# Given a rows x cols binary matrix filled with 0's and 1's, find the largest
# rectangle containing only 1's and return its area.
# 
# 
# Example 1:
# 
# 
# Input: matrix =
# [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
# Output: 6
# Explanation: The maximal rectangle is shown in the above picture.
# 
# 
# Example 2:
# 
# 
# Input: matrix = []
# Output: 0
# 
# 
# Example 3:
# 
# 
# Input: matrix = [["0"]]
# Output: 0
# 
# 
# Example 4:
# 
# 
# Input: matrix = [["1"]]
# Output: 1
# 
# 
# Example 5:
# 
# 
# Input: matrix = [["0","0"]]
# Output: 0
# 
# 
# 
# Constraints:
# 
# 
# rows == matrix.length
# cols == matrix[i].length
# 0 <= row, cols <= 200
# matrix[i][j] is '0' or '1'.
# 
# 
#

# @lc code=start
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or len(matrix) == 0 or len(matrix[0]) == 0:
            return 0

        m, n = len(matrix), len(matrix[0])
        curr_height = [0 for _ in range(n)]
        max_area = 0
        for row in matrix:
            for idx, val in enumerate(row):
                curr_height[idx] = curr_height[idx] + 1 if val == "1" else 0

            curr_max = self._find_max(curr_height)
            max_area = max(max_area, curr_max)

        return max_area


    def _find_max(self, heights):
        levels = heights[:] + [-1]
        mono_stack = []
        level_max = 0

        for idx, height in enumerate(levels):
            while mono_stack and levels[mono_stack[-1]] >= height:
                curr_height = levels[mono_stack.pop()]
                left_idx = mono_stack[-1] if mono_stack else -1
                curr_width = idx - left_idx - 1

                level_max = max(level_max, curr_width * curr_height)

            mono_stack.append(idx)

        return level_max
# @lc code=end

