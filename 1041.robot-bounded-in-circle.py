#
# @lc app=leetcode id=1041 lang=python3
#
# [1041] Robot Bounded In Circle
#
# https://leetcode.com/problems/robot-bounded-in-circle/description/
#
# algorithms
# Medium (54.78%)
# Likes:    907
# Dislikes: 274
# Total Accepted:    61.2K
# Total Submissions: 111.2K
# Testcase Example:  '"GGLLGG"'
#
# On an infinite plane, a robot initially stands at (0, 0) and faces north. The
# robot can receive one of three instructions:
# 
# 
# "G": go straight 1 unit;
# "L": turn 90 degrees to the left;
# "R": turn 90 degrees to the right.
# 
# 
# The robot performs the instructions given in order, and repeats them
# forever.
# 
# Return true if and only if there exists a circle in the plane such that the
# robot never leaves the circle.
# 
# 
# Example 1:
# 
# 
# Input: instructions = "GGLLGG"
# Output: true
# Explanation: The robot moves from (0,0) to (0,2), turns 180 degrees, and then
# returns to (0,0).
# When repeating these instructions, the robot remains in the circle of radius
# 2 centered at the origin.
# 
# Example 2:
# 
# 
# Input: instructions = "GG"
# Output: false
# Explanation: The robot moves north indefinitely.
# 
# Example 3:
# 
# 
# Input: instructions = "GL"
# Output: true
# Explanation: The robot moves from (0, 0) -> (0, 1) -> (-1, 1) -> (-1, 0) ->
# (0, 0) -> ...
# 
# 
# Constraints:
# 
# 
# 1 <= instructions.length <= 100
# instructions[i] is 'G', 'L' or, 'R'.
# 
# 
#

# @lc code=start
class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        start = [0, 0]
        direction = [0, 1] # which axis is the robot facing

        for ins in instructions:
            if ins == "G":
                start[0], start[1] = start[0] + direction[0], start[1] + direction[1]
            elif ins == "L":
                direction = [- direction[1], direction[0]]
            else:
                direction = [direction[1], - direction[0]]

        # Rules to check if the trajactory is bounded
        # 1. if the robot back to starting point, the route is closed
        # 2. as long as the robot is not facing the same direction after one pass
        #    it will somehow the route is closed after several passes
        return start == [0, 0] or direction != [0, 1]
# @lc code=end


# References:
#   1. https://www.youtube.com/watch?v=xgJh5HPCi3A&ab_channel=SaiAnishMalla
#   2. https://www.youtube.com/watch?v=i3Alr_FNu_c&ab_channel=MaxMing

