#
# @lc app=leetcode id=554 lang=python3
#
# [554] Brick Wall
#
# https://leetcode.com/problems/brick-wall/description/
#
# algorithms
# Medium (50.59%)
# Likes:    1380
# Dislikes: 71
# Total Accepted:    81.5K
# Total Submissions: 158.3K
# Testcase Example:  '[[1,2,2,1],[3,1,2],[1,3,2],[2,4],[3,1,2],[1,3,1,1]]'
#
# There is a brick wall in front of you. The wall is rectangular and has
# several rows of bricks. The bricks have the same height but different width.
# You want to draw a vertical line from the top to the bottom and cross the
# least bricks.
# 
# The brick wall is represented by a list of rows. Each row is a list of
# integers representing the width of each brick in this row from left to
# right.
# 
# If your line go through the edge of a brick, then the brick is not considered
# as crossed. You need to find out how to draw the line to cross the least
# bricks and return the number of crossed bricks.
# 
# You cannot draw a line just along one of the two vertical edges of the wall,
# in which case the line will obviously cross no bricks. 
# 
# 
# 
# Example:
# 
# 
# Input: [[1,2,2,1],
# ⁠       [3,1,2],
# ⁠       [1,3,2],
# ⁠       [2,4],
# ⁠       [3,1,2],
# ⁠       [1,3,1,1]]
# 
# Output: 2
# 
# Explanation: 
# 
# 
# 
# 
# 
# Note:
# 
# 
# The width sum of bricks in different rows are the same and won't exceed
# INT_MAX.
# The number of bricks in each row is in range [1,10,000]. The height of wall
# is in range [1,10,000]. Total number of bricks of the wall won't exceed
# 20,000.
# 
# 
#

# this question is interesting, if you draw down the brick as line, and the you move the vertical
# line from left to right, the aim is to find the position of vertical line with the least number
# of bricks where it crossing.
# By thinking it reversedly, if you draw the plot out, If you find the posistion that has the
# most # of bricks aligns (say `max_sum`), where the edges there, then you subtract `max_sum` from total lines

# @lc code=start
class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        if not wall or len(wall) == 0:
            return 0

        m = len(wall)
        width = sum(wall[0])
        slots = defaultdict(int)

        for i in range(m):
            row_sum = 0
            for j in range(len(wall[i])):
                row_sum += wall[i][j]
                slots[row_sum] += 1

        max_sum = 0
        for row_sum in slots:
            if row_sum != width:
                max_sum = max(max_sum, slots[row_sum])

        return m - max_sum
# @lc code=end

