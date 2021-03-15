#
# @lc app=leetcode id=1465 lang=python3
#
# [1465] Maximum Area of a Piece of Cake After Horizontal and Vertical Cuts
#
# https://leetcode.com/problems/maximum-area-of-a-piece-of-cake-after-horizontal-and-vertical-cuts/description/
#
# algorithms
# Medium (31.90%)
# Likes:    235
# Dislikes: 98
# Total Accepted:    21.5K
# Total Submissions: 64.6K
# Testcase Example:  '5\n4\n[1,2,4]\n[1,3]'
#
# Given a rectangular cake with height h and width w, and two arrays of
# integers horizontalCuts and verticalCuts where horizontalCuts[i] is the
# distance from the top of the rectangular cake to the ith horizontal cut and
# similarly, verticalCuts[j] is the distance from the left of the rectangular
# cake to the jth vertical cut.
# 
# Return the maximum area of a piece of cake after you cut at each horizontal
# and vertical position provided in the arrays horizontalCuts and verticalCuts.
# Since the answer can be a huge number, return this modulo 10^9 + 7.
# 
# 
# Example 1:
# 
# 
# 
# 
# Input: h = 5, w = 4, horizontalCuts = [1,2,4], verticalCuts = [1,3]
# Output: 4 
# Explanation: The figure above represents the given rectangular cake. Red
# lines are the horizontal and vertical cuts. After you cut the cake, the green
# piece of cake has the maximum area.
# 
# 
# Example 2:
# 
# 
# 
# 
# Input: h = 5, w = 4, horizontalCuts = [3,1], verticalCuts = [1]
# Output: 6
# Explanation: The figure above represents the given rectangular cake. Red
# lines are the horizontal and vertical cuts. After you cut the cake, the green
# and yellow pieces of cake have the maximum area.
# 
# 
# Example 3:
# 
# 
# Input: h = 5, w = 4, horizontalCuts = [3], verticalCuts = [3]
# Output: 9
# 
# 
# 
# Constraints:
# 
# 
# 2 <= h, w <= 10^9
# 1 <= horizontalCuts.length < min(h, 10^5)
# 1 <= verticalCuts.length < min(w, 10^5)
# 1 <= horizontalCuts[i] < h
# 1 <= verticalCuts[i] < w
# It is guaranteed that all elements in horizontalCuts are distinct.
# It is guaranteed that all elements in verticalCuts are distinct.
# 
# 
#

# @lc code=start
import math
class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        return int((self._compute_max_length(h, horizontalCuts) * self._compute_max_length(w, verticalCuts)) % (math.pow(10, 9) + 7))


    def _compute_max_length(self, length, cuts):
        cuts = sorted([0] + cuts + [length])

        if len(cuts) == 0:
            return length

        cuts = list(cuts)
        max_length = cuts[0]
        for i in range(1, len(cuts)):
            max_length = max(max_length, cuts[i] - cuts[i - 1])

        max_length = max(max_length, length - cuts[len(cuts) - 1])
        return max_length
# @lc code=end

