#
# @lc app=leetcode id=42 lang=python3
#
# [42] Trapping Rain Water
#
# https://leetcode.com/problems/trapping-rain-water/description/
#
# algorithms
# Hard (50.86%)
# Likes:    10171
# Dislikes: 156
# Total Accepted:    686.5K
# Total Submissions: 1.3M
# Testcase Example:  '[0,1,0,2,1,0,1,3,2,1,2,1]'
#
# Given n non-negative integers representing an elevation map where the width
# of each bar is 1, compute how much water it can trap after raining.
# 
# 
# Example 1:
# 
# 
# Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
# Explanation: The above elevation map (black section) is represented by array
# [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section)
# are being trapped.
# 
# 
# Example 2:
# 
# 
# Input: height = [4,2,0,3,2,5]
# Output: 9
# 
# 
# 
# Constraints:
# 
# 
# n == height.length
# 0 <= n <= 3 * 10^4
# 0 <= height[i] <= 10^5
# 
# 
#

# @lc code=start
class Solution:
    def trap(self, heights: List[int]) -> int:
        if not heights or len(heights) == 0:
            return 0

        left, right = 0, len(heights) - 1
        left_max, right_max = heights[0], heights[-1]
        water = 0
        while left <= right:
            if left_max < right_max:
                left_max = max(left_max, heights[left])
                water += (left_max - heights[left])
                left += 1
            else:
                right_max = max(right_max, heights[right])
                water += (right_max - heights[right])
                right -= 1

        return water


# @lc code=end

