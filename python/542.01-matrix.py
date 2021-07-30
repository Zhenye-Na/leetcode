#
# @lc app=leetcode id=542 lang=python3
#
# [542] 01 Matrix
#
# https://leetcode.com/problems/01-matrix/description/
#
# algorithms
# Medium (41.79%)
# Likes:    2906
# Dislikes: 143
# Total Accepted:    154.7K
# Total Submissions: 362.3K
# Testcase Example:  '[[0,0,0],[0,1,0],[0,0,0]]'
#
# Given an m x n binary matrix mat, return the distance of the nearest 0 for
# each cell.
# 
# The distance between two adjacent cells is 1.
# 
# 
# Example 1:
# 
# 
# Input: mat = [[0,0,0],[0,1,0],[0,0,0]]
# Output: [[0,0,0],[0,1,0],[0,0,0]]
# 
# 
# Example 2:
# 
# 
# Input: mat = [[0,0,0],[0,1,0],[1,1,1]]
# Output: [[0,0,0],[0,1,0],[1,2,1]]
# 
# 
# 
# Constraints:
# 
# 
# m == mat.length
# n == mat[i].length
# 1 <= m, n <= 10^4
# 1 <= m * n <= 10^4
# mat[i][j] is either 0 or 1.
# There is at least one 0 in mat.
# 
# 
#

# @lc code=start
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        
# @lc code=end

