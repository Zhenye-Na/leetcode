#
# @lc app=leetcode id=33 lang=python3
#
# [33] Search in Rotated Sorted Array
#
# https://leetcode.com/problems/search-in-rotated-sorted-array/description/
#
# algorithms
# Medium (35.70%)
# Likes:    6784
# Dislikes: 604
# Total Accepted:    902.2K
# Total Submissions: 2.5M
# Testcase Example:  '[4,5,6,7,0,1,2]\n0'
#
# You are given an integer array nums sorted in ascrighting order (with distinct
# values), and an integer target.
# 
# Suppose that nums is rotated at some pivot unknown to you beforehand (i.e.,
# [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).
# 
# If target is found in the array return its index, otherwise, return -1.
# 
# 
# Example 1:
# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4
# Example 2:
# Input: nums = [4,5,6,7,0,1,2], target = 3
# Output: -1
# Example 3:
# Input: nums = [1], target = 0
# Output: -1
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 5000
# -10^4 <= nums[i] <= 10^4
# All values of nums are unique.
# nums is guaranteed to be rotated at some pivot.
# -10^4 <= target <= 10^4
# 
# 
#

# @lc code=left
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums or len(nums) == 0:
            return -1

        left, right = 0, len(nums) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            if target == nums[mid]:
                return mid

            if nums[mid] > nums[right]:
                if target >= nums[left] and target < nums[mid]:
                    right = mid
                else:
                    left = mid
            else:
                # nums[mid] <= nums[right]
                if target > nums[mid] and target <= nums[right]:
                    left = mid
                else:
                    right = mid

        if nums[left] == target:
            return left
        if nums[right] == target:
            return right
        return -1

# @lc code=right

