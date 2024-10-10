#
# @lc app=leetcode id=962 lang=python3
#
# [962] Maximum Width Ramp
#
# https://leetcode.com/problems/maximum-width-ramp/description/
#
# algorithms
# Medium (49.19%)
# Likes:    1747
# Dislikes: 53
# Total Accepted:    55.1K
# Total Submissions: 107.3K
# Testcase Example:  '[6,0,8,2,1,5]'
#
# A ramp in an integer array nums is a pair (i, j) for which i < j and nums[i]
# <= nums[j]. The width of such a ramp is j - i.
#
# Given an integer array nums, return the maximum width of a ramp in nums. If
# there is no ramp in nums, return 0.
#
#
# Example 1:
#
#
# Input: nums = [6,0,8,2,1,5]
# Output: 4
# Explanation: The maximum width ramp is achieved at (i, j) = (1, 5): nums[1] =
# 0 and nums[5] = 5.
#
#
# Example 2:
#
#
# Input: nums = [9,8,1,0,1,9,4,0,4,1]
# Output: 7
# Explanation: The maximum width ramp is achieved at (i, j) = (2, 9): nums[2] =
# 1 and nums[9] = 1.
#
#
#
# Constraints:
#
#
# 2 <= nums.length <= 5 * 10^4
# 0 <= nums[i] <= 5 * 10^4
#
#
#


# @lc code=start
from typing import List


class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        stack = []
        for i, num in enumerate(nums):
            if not stack or nums[stack[-1]] > num:
                stack.append(i)

        max_ramp = 0
        for i in range(len(nums) - 1, -1, -1):
            while stack and nums[i] >= nums[stack[-1]]:
                max_ramp = max(max_ramp, i - stack.pop())

        return max_ramp


# @lc code=end
