#
# @lc app=leetcode id=35 lang=python3
#
# [35] Search Insert Position
#
# https://leetcode.com/problems/search-insert-position/description/
#
# algorithms
# Easy (42.78%)
# Likes:    3231
# Dislikes: 284
# Total Accepted:    777K
# Total Submissions: 1.8M
# Testcase Example:  '[1,3,5,6]\n5'
#
# Given a sorted array of distinct integers and a target value, return the
# index if the target is found. If not, return the index where it would be if
# it were inserted in order.
# 
# 
# Example 1:
# Input: nums = [1,3,5,6], target = 5
# Output: 2
# Example 2:
# Input: nums = [1,3,5,6], target = 2
# Output: 1
# Example 3:
# Input: nums = [1,3,5,6], target = 7
# Output: 4
# Example 4:
# Input: nums = [1,3,5,6], target = 0
# Output: 0
# Example 5:
# Input: nums = [1], target = 0
# Output: 0
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 10^4
# -10^4 <= nums[i] <= 10^4
# nums contains distinct values sorted in ascending order.
# -10^4 <= target <= 10^4
# 
# 
#

# @lc code=start
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # the last number smaller than target, idx + 1
        if not nums or len(nums) == 0:
            return 0

        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if nums[mid] >= target:
                end = mid
            else:
                start = mid

        if nums[end] < target:
            return end + 1
        if nums[start] < target:
            return start + 1

        return 0



# @lc code=end

