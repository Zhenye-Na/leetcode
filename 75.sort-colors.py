#
# @lc app=leetcode id=75 lang=python3
#
# [75] Sort Colors
#
# https://leetcode.com/problems/sort-colors/description/
#
# algorithms
# Medium (49.05%)
# Likes:    4934
# Dislikes: 281
# Total Accepted:    638K
# Total Submissions: 1.3M
# Testcase Example:  '[2,0,2,1,1,0]'
#
# Given an array nums with n objects colored red, white, or blue, sort them
# in-place so that objects of the same color are adjacent, with the colors in
# the order red, white, and blue.
# 
# We will use the integers 0, 1, and 2 to represent the color red, white, and
# blue, respectively.
# 
# 
# Example 1:
# Input: nums = [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]
# Example 2:
# Input: nums = [2,0,1]
# Output: [0,1,2]
# Example 3:
# Input: nums = [0]
# Output: [0]
# Example 4:
# Input: nums = [1]
# Output: [1]
# 
# 
# Constraints:
# 
# 
# n == nums.length
# 1 <= n <= 300
# nums[i] is 0, 1, or 2.
# 
# 
# 
# Follow up:
# 
# 
# Could you solve this problem without using the library's sort function?
# Could you come up with a one-pass algorithm using only O(1) constant space?
# 
# 
#

# @lc code=start
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left, right = 0, len(nums) - 1
        i = 0
        while i <= right:
            if nums[i] == 0:
                nums[left], nums[i] = nums[i], nums[left]
                i += 1
                left += 1
            elif nums[i] == 2:
                nums[right], nums[i] = nums[i], nums[right]
                right -= 1
                # do not increase `i` pointer, since the value swapped here could be 2
            else:
                i += 1


# @lc code=end

