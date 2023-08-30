#
# @lc app=leetcode id=1914 lang=python3
#
# [1914] Cyclically Rotating a Grid
#
# https://leetcode.com/problems/cyclically-rotating-a-grid/description/
#
# algorithms
# Medium (43.45%)
# Likes:    218
# Dislikes: 265
# Total Accepted:    11.4K
# Total Submissions: 23.4K
# Testcase Example:  '[[40,10],[30,20]]\n1'
#
# You are given an m x n integer matrix grid​​​, where m and n are both even
# integers, and an integer k.
# 
# The matrix is composed of several layers, which is shown in the below image,
# where each color is its own layer:
# 
# 
# 
# A cyclic rotation of the matrix is done by cyclically rotating each layer in
# the matrix. To cyclically rotate a layer once, each element in the layer will
# take the place of the adjacent element in the counter-clockwise direction. An
# example rotation is shown below:
# 
# Return the matrix after applying k cyclic rotations to it.
# 
# 
# Example 1:
# 
# 
# Input: grid = [[40,10],[30,20]], k = 1
# Output: [[10,20],[40,30]]
# Explanation: The figures above represent the grid at every state.
# 
# 
# Example 2:
# ⁠ 
# 
# 
# Input: grid = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]], k = 2
# Output: [[3,4,8,12],[2,11,10,16],[1,7,6,15],[5,9,13,14]]
# Explanation: The figures above represent the grid at every state.
# 
# 
# 
# Constraints:
# 
# 
# m == grid.length
# n == grid[i].length
# 2 <= m, n <= 50
# Both m and n are even integers.
# 1 <= grid[i][j] <=^ 5000
# 1 <= k <= 10^9
# 
#

# @lc code=start
class Solution:

    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        self.m, self.n = len(grid), len(grid[0])
        num_layers = min(self.m // 2, self.n // 2)

        for l in range(num_layers):
            array = []

            # top row
            for i in range(l, self.n - l - 1):
                array.append(grid[l][i])

            # right col
            for i in range(l, self.m - l - 1):
                array.append(grid[i][self.n - l - 1])
        
            # bottom row
            for i in range(self.n - l - 1, l, -1):
                array.append(grid[self.m - l - 1][i])

            # left col
            for i in range(self.m - l - 1, l, -1):
                array.append(grid[i][l])
                
            kk = k % len(array)
            for i in range(kk):
                array.append(array[i])

            self.spiral_matrix(grid, array, l, kk)
                
        return grid

                
    def spiral_matrix(self, grid, array, l, start):
        print(array)
        print(len(array), start)
        
        # top row
        for i in range(l, self.n - l - 1):
            grid[l][i] = array[start]
            start += 1

        # right col
        for i in range(l, self.m - l - 1):
            grid[i][self.n - l - 1] = array[start]
            start += 1

        # bottom row
        for i in range(self.n - l - 1, l, -1):
            grid[self.m - l - 1][i] = array[start]
            start += 1

        # left col
        for i in range(self.m - l - 1, l, -1):
            grid[i][l] = array[start]
            start += 1
# @lc code=end

