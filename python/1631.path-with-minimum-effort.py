#
# @lc app=leetcode id=1631 lang=python3
#
# [1631] Path With Minimum Effort
#
# https://leetcode.com/problems/path-with-minimum-effort/description/
#
# algorithms
# Medium (50.43%)
# Likes:    4808
# Dislikes: 164
# Total Accepted:    165.7K
# Total Submissions: 292.5K
# Testcase Example:  '[[1,2,2],[3,8,2],[5,3,5]]'
#
# You are a hiker preparing for an upcoming hike. You are given heights, a 2D
# array of size rows x columns, where heights[row][col] represents the height
# of cell (row, col). You are situated in the top-left cell, (0, 0), and you
# hope to travel to the bottom-right cell, (rows-1, columns-1) (i.e.,
# 0-indexed). You can move up, down, left, or right, and you wish to find a
# route that requires the minimum effort.
# 
# A route's effort is the maximum absolute difference in heights between two
# consecutive cells of the route.
# 
# Return the minimum effort required to travel from the top-left cell to the
# bottom-right cell.
# 
# 
# Example 1:
# 
# 
# 
# 
# Input: heights = [[1,2,2],[3,8,2],[5,3,5]]
# Output: 2
# Explanation: The route of [1,3,5,3,5] has a maximum absolute difference of 2
# in consecutive cells.
# This is better than the route of [1,2,2,2,5], where the maximum absolute
# difference is 3.
# 
# 
# Example 2:
# 
# 
# 
# 
# Input: heights = [[1,2,3],[3,8,4],[5,3,5]]
# Output: 1
# Explanation: The route of [1,2,3,4,5] has a maximum absolute difference of 1
# in consecutive cells, which is better than route [1,3,5,3,5].
# 
# 
# Example 3:
# 
# 
# Input: heights =
# [[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]]
# Output: 0
# Explanation: This route does not require any effort.
# 
# 
# 
# Constraints:
# 
# 
# rows == heights.length
# columns == heights[i].length
# 1 <= rows, columns <= 100
# 1 <= heights[i][j] <= 10^6
# 
#

# @lc code=start
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:

        self.rows, self.cols = len(heights), len(heights[0])
        efforts = self.constructEfforts(heights)

        visited = set()
        min_effort = 0
        heap = [(0, (0, 0))]
        while heap:

            effort, next_point = heappop(heap)
            if next_point in visited:
                continue

            min_effort = max(min_effort, effort)
            visited.add(tuple(next_point))
            if next_point[0] == self.rows - 1 and next_point[1] == self.cols - 1:
                return min_effort

            for points in efforts[(next_point[0], next_point[1])]:
                heappush(heap, points)

        return 0


    def constructEfforts(self, heights):
        efforts = defaultdict(list)

        for i in range(self.rows):
            for j in range(self.cols):
                if 0 <= i <= self.rows - 1 and 0 <= j + 1<= self.cols - 1:
                    efforts[(i, j)].append((abs(heights[i][j] - heights[i][j + 1]), (i, j + 1)))
                    
                if 0 <= i + 1 <= self.rows - 1 and 0 <= j <= self.cols - 1:
                    efforts[(i, j)].append((abs(heights[i][j] - heights[i + 1][j]), (i + 1, j)))
                    
                if 0 <= i <= self.rows - 1 and 0 <= j - 1 <= self.cols - 1:
                    efforts[(i, j)].append((abs(heights[i][j] - heights[i][j - 1]), (i, j - 1)))
                    
                if 0 <= i - 1 <= self.rows - 1 and 0 <= j <= self.cols - 1:
                    efforts[(i, j)].append((abs(heights[i][j] - heights[i - 1][j]), (i - 1, j)))

        return efforts
# @lc code=end

