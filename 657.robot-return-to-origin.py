#
# @lc app=leetcode id=657 lang=python3
#
# [657] Robot Return to Origin
#
# https://leetcode.com/problems/robot-return-to-origin/description/
#
# algorithms
# Easy (73.67%)
# Likes:    1228
# Dislikes: 692
# Total Accepted:    274.1K
# Total Submissions: 371K
# Testcase Example:  '"UD"'
#
# There is a robot starting at position (0, 0), the origin, on a 2D plane.
# Given a sequence of its moves, judge if this robot ends up at (0, 0) after it
# completes its moves.
# 
# The move sequence is represented by a string, and the character moves[i]
# represents its ith move. Valid moves are R (right), L (left), U (up), and D
# (down). If the robot returns to the origin after it finishes all of its
# moves, return true. Otherwise, return false.
# 
# Note: The way that the robot is "facing" is irrelevant. "R" will always make
# the robot move to the right once, "L" will always make it move left, etc.
# Also, assume that the magnitude of the robot's movement is the same for each
# move.
# 
# 
# Example 1:
# 
# 
# Input: moves = "UD"
# Output: true
# Explanation: The robot moves up once, and then down once. All moves have the
# same magnitude, so it ended up at the origin where it started. Therefore, we
# return true.
# 
# 
# Example 2:
# 
# 
# Input: moves = "LL"
# Output: false
# Explanation: The robot moves left twice. It ends up two "moves" to the left
# of the origin. We return false because it is not at the origin at the end of
# its moves.
# 
# 
# Example 3:
# 
# 
# Input: moves = "RRDD"
# Output: false
# 
# 
# Example 4:
# 
# 
# Input: moves = "LDRRLRUULR"
# Output: false
# 
# 
# 
# Constraints:
# 
# 
# 1 <= moves.length <= 2 * 10^4
# moves only contains the characters 'U', 'D', 'L' and 'R'.
# 
# 
#

# @lc code=start
class Solution:
    def judgeCircle(self, moves: str) -> bool:
        start = [0, 0]

        for move in moves:
            if move == "U":
                start[0], start[1] = start[0] + 0, start[1] + 1
            elif move == "R":
                start[0], start[1] = start[0] + 1, start[1] + 0
            elif move == "D":
                start[0], start[1] = start[0] + 0, start[1] + (-1)
            else:
                start[0], start[1] = start[0] + (-1), start[1] + 0

        return start == [0, 0]

# @lc code=end

