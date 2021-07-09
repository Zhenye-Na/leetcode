#
# @lc app=leetcode id=378 lang=python3
#
# [378] Kth Smallest Element in a Sorted Matrix
#
# https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/description/
#
# algorithms
# Medium (55.93%)
# Likes:    3375
# Dislikes: 178
# Total Accepted:    244.4K
# Total Submissions: 435K
# Testcase Example:  '[[1,5,9],[10,11,13],[12,13,15]]\n8'
#
# Given an n x n matrix where each of the rows and columns are sorted in
# ascending order, return the k^th smallest element in the matrix.
# 
# Note that it is the k^th smallest element in the sorted order, not the k^th
# distinct element.
# 
# 
# Example 1:
# 
# 
# Input: matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 8
# Output: 13
# Explanation: The elements in the matrix are [1,5,9,10,11,12,13,13,15], and
# the 8^th smallest number is 13
# 
# 
# Example 2:
# 
# 
# Input: matrix = [[-5]], k = 1
# Output: -5
# 
# 
# 
# Constraints:
# 
# 
# n == matrix.length
# n == matrix[i].length
# 1 <= n <= 300
# -10^9 <= matrix[i][j] <= -10^9
# All the rows and columns of matrix are guaranteed to be sorted in
# non-degreasing order.
# 1 <= k <= n^2
# 
# 
#

# @lc code=start
from heapq import heappush, heappop

class Solution:
    dx = [0, 1]
    dy = [1, 0]

    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        if not matrix or len(matrix) == 0 or len(matrix[0]) == 0:
            return 0

        m, n = len(matrix), len(matrix[0])
        heap = [(matrix[0][0], 0, 0)]
        seen = set([(0, 0)])

        for _ in range(k - 1):
            _, x, y = heappop(heap)
            for i in range(2):
                newx, newy = x + self.dx[i], y + self.dy[i]
                if 0 <= newx < m and 0 <= newy < n and (newx, newy) not in seen:
                    heappush(heap, (matrix[newx][newy], newx, newy))
                    seen.add((newx, newy))

        return heap[0][0]
# @lc code=end

