#
# @lc app=leetcode id=74 lang=python3
#
# [74] Search a 2D Matrix
#
# https://leetcode.com/problems/search-a-2d-matrix/description/
#
# algorithms
# Medium (37.48%)
# Likes:    2796
# Dislikes: 190
# Total Accepted:    411.8K
# Total Submissions: 1.1M
# Testcase Example:  '[[1,3,5,7],[10,11,16,20],[23,30,34,60]]\n3'
#
# Write an efficient algorithm that searches for a value in an m x n matrix.
# This matrix has the following properties:
# 
# 
# Integers in each row are sorted from left to right.
# The first integer of each row is greater than the last integer of the
# previous row.
# 
# 
# 
# Example 1:
# 
# 
# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
# Output: true
# 
# 
# Example 2:
# 
# 
# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
# Output: false
# 
# 
# 
# Constraints:
# 
# 
# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 100
# -10^4 <= matrix[i][j], target <= 10^4
# 
# 
#

# @lc code=start
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        firstCol = [row[0] for row in matrix]
        row = self._binarySearchRow(firstCol, target)

        return self._binarySearch(matrix[row], target)

    def _binarySearchRow(self, array, target):
        # return the last position where array[idx] <= target
        left, right = 0, len(array) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            if array[mid] <= target:
                left = mid
            else:
                right = mid
        
        if array[right] <= target:
            return right
        if array[left] <= target:
            return left
        return -1


    def _binarySearch(self, array, target):
        # return the first position where array[idx] >= target
        left, right = 0, len(array) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            if array[mid] == target:
                return True
            elif target < array[mid]:
                right = mid
            else:
                left = mid
        
        if array[left] == target or array[right] == target:
            return True
        return False

# @lc code=end

