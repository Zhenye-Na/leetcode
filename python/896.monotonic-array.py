#
# @lc app=leetcode id=896 lang=python3
#
# [896] Monotonic Array
#
# https://leetcode.com/problems/monotonic-array/description/
#
# algorithms
# Easy (57.86%)
# Likes:    2243
# Dislikes: 69
# Total Accepted:    288.1K
# Total Submissions: 489.7K
# Testcase Example:  '[1,2,2,3]'
#
# An array is monotonic if it is either monotone increasing or monotone
# decreasing.
# 
# An array nums is monotone increasing if for all i <= j, nums[i] <= nums[j].
# An array nums is monotone decreasing if for all i <= j, nums[i] >= nums[j].
# 
# Given an integer array nums, return true if the given array is monotonic, or
# false otherwise.
# 
# 
# Example 1:
# 
# 
# Input: nums = [1,2,2,3]
# Output: true
# 
# 
# Example 2:
# 
# 
# Input: nums = [6,5,4,4]
# Output: true
# 
# 
# Example 3:
# 
# 
# Input: nums = [1,3,2]
# Output: false
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 10^5
# -10^5 <= nums[i] <= 10^5
# 
# 
#

# @lc code=start
class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        
        if not nums or len(nums) <= 1:
            return True

        return self._is_monotonic_increasing(nums) or self._is_monotonic_decreasing(nums)

    def _is_monotonic_increasing(self, nums):
        left, right = 0, 1
        while right < len(nums):
            if nums[left] > nums[right]:
                return False

            left += 1
            right += 1

        return True

    def _is_monotonic_decreasing(self, nums):
        left, right = 0, 1
        while right < len(nums):
            if nums[left] < nums[right]:
                return False

            left += 1
            right += 1

        return True
# @lc code=end

