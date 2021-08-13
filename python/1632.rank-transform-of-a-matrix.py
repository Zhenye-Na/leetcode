#
# @lc app=leetcode id=1632 lang=python3
#
# [1632] Rank Transform of a Matrix
#
# https://leetcode.com/problems/rank-transform-of-a-matrix/description/
#
# algorithms
# Hard (32.28%)
# Likes:    406
# Dislikes: 26
# Total Accepted:    11.8K
# Total Submissions: 29.2K
# Testcase Example:  '[[1,2],[3,4]]'
#
# Given an m x n matrix, return a new matrix answer where answer[row][col] is
# the rank of matrix[row][col].
# 
# The rank is an integer that represents how large an element is compared to
# other elements. It is calculated using the following rules:
# 
# 
# The rank is an integer starting from 1.
# If two elements p and q are in the same row or column, then:
# 
# If p < q then rank(p) < rank(q)
# If p == q then rank(p) == rank(q)
# If p > q then rank(p) > rank(q)
# 
# 
# The rank should be as small as possible.
# 
# 
# It is guaranteed that answer is unique under the given rules.
# 
# 
# Example 1:
# 
# 
# Input: matrix = [[1,2],[3,4]]
# Output: [[1,2],[2,3]]
# Explanation:
# The rank of matrix[0][0] is 1 because it is the smallest integer in its row
# and column.
# The rank of matrix[0][1] is 2 because matrix[0][1] > matrix[0][0] and
# matrix[0][0] is rank 1.
# The rank of matrix[1][0] is 2 because matrix[1][0] > matrix[0][0] and
# matrix[0][0] is rank 1.
# The rank of matrix[1][1] is 3 because matrix[1][1] > matrix[0][1],
# matrix[1][1] > matrix[1][0], and both matrix[0][1] and matrix[1][0] are rank
# 2.
# 
# 
# Example 2:
# 
# 
# Input: matrix = [[7,7],[7,7]]
# Output: [[1,1],[1,1]]
# 
# 
# Example 3:
# 
# 
# Input: matrix = [[20,-21,14],[-19,4,19],[22,-47,24],[-19,4,19]]
# Output: [[4,2,3],[1,3,4],[5,1,6],[1,3,4]]
# 
# 
# Example 4:
# 
# 
# Input: matrix = [[7,3,6],[1,4,5],[9,8,2]]
# Output: [[5,1,4],[1,2,3],[6,3,1]]
# 
# 
# 
# Constraints:
# 
# 
# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 500
# -10^9 <= matrix[row][col] <= 10^9
# 
# 
#

# @lc code=start
from heapq import heappush, heappop

import sys

class Solution:
    def matrixRankTransform(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix or len(matrix) == 0 or len(matrix[0]) == 0:
            return matrix

        n , m = len(matrix), len(matrix[0])
        ret = [[0 for _ in range(m)] for _ in range(n)]
        heap = []

        for i in range(n):
            for j in range(m):
                heappush(heap, (matrix[i][j], i, j))

        starter, last_max = 1, -1
        prev = - sys.maxsize - 1
        prev_x, prev_y = -1, -1
        for _ in range(len(heap)):
            value, x, y = heappop(heap)
            print(value, x, y, starter)
            if value == prev:
                ret[x][y] = ret[prev_x][prev_y]
                continue

            print(ret)
            col = [row[y] for row in ret]
            print(ret[x])
            print(col)
            if max(ret[x]) == 0 and max(col) == 0:
                ret[x][y] = 1
            elif max(ret[x]) == starter - 1 or max([ret[r][y] for r in range(n)]) == starter - 1:
                print(">>> if")
                ret[x][y] = starter
            else:
                print(">>> else")
                ret[x][y] = max(
                    max(ret[x]),
                    max([ret[r][y] for r in range(n)])
                ) + 1

            if prev != value:
                starter += 1
            prev, prev_x, prev_y = value, x, y
            

            print("===================================",ret)
        return ret
    
    
# [[1,2],[3,4]]
# [[7,7],[7,7]]
# [[20,-21,14],[-19,4,19],[22,-47,24],[-19,4,19]]
# [[7,3,6],[1,4,5],[9,8,2]]
# @lc code=end

