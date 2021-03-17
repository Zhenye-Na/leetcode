#
# @lc app=leetcode id=84 lang=python3
#
# [84] Largest Rectangle in Histogram
#
# https://leetcode.com/problems/largest-rectangle-in-histogram/description/
#
# algorithms
# Hard (36.89%)
# Likes:    5443
# Dislikes: 110
# Total Accepted:    345.4K
# Total Submissions: 927K
# Testcase Example:  '[2,1,5,6,2,3]'
#
# Given an array of integers heights representing the histogram's bar height
# where the width of each bar is 1, return the area of the largest rectangle in
# the histogram.
# 
# 
# Example 1:
# 
# 
# Input: heights = [2,1,5,6,2,3]
# Output: 10
# Explanation: The above is a histogram where width of each bar is 1.
# The largest rectangle is shown in the red area, which has an area = 10
# units.
# 
# 
# Example 2:
# 
# 
# Input: heights = [2,4]
# Output: 4
# 
# 
# 
# Constraints:
# 
# 
# 1 <= heights.length <= 10^5
# 0 <= heights[i] <= 10^4
# 
# 
#

# @lc code=start
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        mono_stack = []
        heights += [-1]

        max_area = 0
        for idx, height in enumerate(heights):
            while mono_stack and heights[mono_stack[-1]] >= height:
                # pop mono_stack
                curr_height = heights[mono_stack.pop()]
                left_idx = mono_stack[-1] if len(mono_stack) > 0 else -1
                curr_width = idx - left_idx - 1
                max_area = max(max_area, curr_height * curr_width)

            mono_stack.append(idx)

        return max_area
# @lc code=end

