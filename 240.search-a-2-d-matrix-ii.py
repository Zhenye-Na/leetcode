#
# @lc app=leetcode id=240 lang=python3
#
# [240] Search a 2D Matrix II
#
# https://leetcode.com/problems/search-a-2d-matrix-ii/description/
#
# algorithms
# Medium (41.66%)
# Likes:    1941
# Dislikes: 57
# Total Accepted:    218.3K
# Total Submissions: 523.9K
# Testcase Example:  '[[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]\n5'
#
# Write an efficient algorithm that searches for a value in an m x n matrix.
# This matrix has the following properties:
# 
# 
# Integers in each row are sorted in ascending from left to right.
# Integers in each column are sorted in ascending from top to bottom.
# 
# 
# Example:
# 
# Consider the following matrix:
# 
# 
# [
# ⁠ [1,   4,  7, 11, 15],
# ⁠ [2,   5,  8, 12, 19],
# ⁠ [3,   6,  9, 16, 22],
# ⁠ [10, 13, 14, 17, 24],
# ⁠ [18, 21, 23, 26, 30]
# ]
# 
# 
# Given target = 5, return true.
# 
# Given target = 20, return false.
# 
#

# @lc code=start
class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or len(matrix) == 0 or len(matrix[0]) == 0:
            return False

        res = False
        for row in matrix:
            if row[0] <= target:
                res = self.binarySearch(row, target)
                if res:
                    return res
            else:
                break
        return res

    def binarySearch(self, arr, target):
        lo, hi = 0, len(arr) - 1
        while lo + 1 < hi:
            mid = lo + (hi - lo) // 2
            if target == arr[mid]:
                return True
            elif target > arr[mid]:
                lo = mid
            else:
                hi = mid

        if arr[lo] == target or arr[hi] == target:
            return True
        return False

# @lc code=end

