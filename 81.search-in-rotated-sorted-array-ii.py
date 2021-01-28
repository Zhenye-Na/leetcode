#
# @lc app=leetcode id=81 lang=python3
#
# [81] Search in Rotated Sorted Array II
#
# https://leetcode.com/problems/search-in-rotated-sorted-array-ii/description/
#
# algorithms
# Medium (33.48%)
# Likes:    1879
# Dislikes: 551
# Total Accepted:    288.3K
# Total Submissions: 861.1K
# Testcase Example:  '[2,5,6,0,0,1,2]\n0'
#
# You are given an integer array nums sorted in ascending order (not
# necessarily distinct values), and an integer target.
# 
# Suppose that nums is rotated at some pivot unknown to you beforehand (i.e.,
# [0,1,2,4,4,4,5,6,6,7] might become [4,5,6,6,7,0,1,2,4,4]).
# 
# If target is found in the array return its index, otherwise, return -1.
# 
# 
# Example 1:
# Input: nums = [2,5,6,0,0,1,2], target = 0
# Output: true
# Example 2:
# Input: nums = [2,5,6,0,0,1,2], target = 3
# Output: false
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 5000
# -10^4 <= nums[i] <= 10^4
# nums is guaranteed to be rotated at some pivot.
# -10^4 <= target <= 10^4
# 
# 
# 
# Follow up: This problem is the same as Search in Rotated Sorted Array, where
# nums may contain duplicates. Would this affect the run-time complexity? How
# and why?
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        if not nums or len(nums) == 0:
            return False

        left, right = 0, len(nums) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            if target == nums[mid]:
                return True

            # dedup
            elif nums[left] == nums[mid] == nums[right]:
                left += 1
                right -= 1

            elif nums[mid] >= nums[left]:
                if nums[left] <= target < nums[mid]:
                    right = mid
                else:
                    left = mid
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid
                else:
                    right = mid

        # double check
        if nums[left] == target or nums[right] == target:
            return True
        return False
# @lc code=end

