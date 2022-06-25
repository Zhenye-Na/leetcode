#
# @lc app=leetcode id=665 lang=python3
#
# [665] Non-decreasing Array
#
# https://leetcode.com/problems/non-decreasing-array/description/
#
# algorithms
# Medium (20.98%)
# Likes:    3967
# Dislikes: 675
# Total Accepted:    184.1K
# Total Submissions: 832.4K
# Testcase Example:  '[4,2,3]'
#
# Given an array nums with n integers, your task is to check if it could become
# non-decreasing by modifying at most one element.
# 
# We define an array is non-decreasing if nums[i] <= nums[i + 1] holds for
# every i (0-based) such that (0 <= i <= n - 2).
# 
# 
# Example 1:
# 
# 
# Input: nums = [4,2,3]
# Output: true
# Explanation: You could modify the first 4 to 1 to get a non-decreasing
# array.
# 
# 
# Example 2:
# 
# 
# Input: nums = [4,2,1]
# Output: false
# Explanation: You can't get a non-decreasing array by modify at most one
# element.
# 
# 
# 
# Constraints:
# 
# 
# n == nums.length
# 1 <= n <= 10^4
# -10^5 <= nums[i] <= 10^5
# 
# 
#

# @lc code=start
class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        if not nums or len(nums) <= 2:
            return True

        count = 0
        for i in range(len(nums)-1):
            if nums[i+1] - nums[i]<0:
                count += 1
            if ( i > 1 and nums[i] - nums[i - 2] < 0 and nums[i + 1] - nums[i - 1] < 0 ) or count > 1:
                return False
        return True
# @lc code=end

