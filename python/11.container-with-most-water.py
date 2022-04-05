#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#
# https://leetcode.com/problems/container-with-most-water/description/
#
# algorithms
# Medium (46.49%)
# Likes:    4092
# Dislikes: 480
# Total Accepted:    466.7K
# Total Submissions: 989.6K
# Testcase Example:  '[1,8,6,2,5,4,8,3,7]'
#
# Given n non-negative integers a1, a2, ..., an , where each represents a point
# at coordinate (i, ai). n vertical lines are drawn such that the two endpoints
# of line i is at (i, ai) and (i, 0). Find two lines, which together with
# x-axis forms a container, such that the container contains the most water.
# 
# Note: You may not slant the container and n is at least 2.
# 
# image:
# https://s3-lc-upload.s3.amazonaws.com/uploads/2018/07/17/question_11.jpg
# 
# 
# The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In
# this case, the max area of water (blue section) the container can contain is
# 49. 
# 
# 
# 
# Example:
# 
# 
# Input: [1,8,6,2,5,4,8,3,7]
# Output: 49
# 
# Youtube solution:
#   https://www.youtube.com/watch?v=IONgE6QZgGI
#   https://www.youtube.com/watch?v=JMmKtYH5VOE&ab_channel=MichaelMuinos
#

# @lc code=start
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        if not heights or len(heights) == 0:
            return 0

        left, right = 0, len(heights) - 1
        max_area = 0
        while left < right:
            curr_area = (right - left) * min(heights[left], heights[right])
            max_area = max(max_area, curr_area)
            if heights[left] <= heights[right]:
                left += 1
            else:
                right -= 1

        return max_area
# @lc code=end

