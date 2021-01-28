#
# @lc app=leetcode id=154 lang=python3
#
# [154] Find Minimum in Rotated Sorted Array II
#
# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/description/
#
# algorithms
# Hard (41.95%)
# Likes:    1376
# Dislikes: 265
# Total Accepted:    231.7K
# Total Submissions: 552.3K
# Testcase Example:  '[1,3,5]'
#
# Suppose an array sorted in ascending order is rotated at some pivot unknown
# to you beforehand.
# 
# (i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).
# 
# Find the minimum element.
# 
# The array may contain duplicates.
# 
# Example 1:
# 
# 
# Input: [1,3,5]
# Output: 1
# 
# Example 2:
# 
# 
# Input: [2,2,2,0,1]
# Output: 0
# 
# Note:
# 
# 
# This is a follow up problem to Find Minimum in Rotated Sorted Array.
# Would allow duplicates affect the run-time complexity? How and why?
# 
# 
#

# @lc code=start
class Solution:
    def findMin(self, nums: List[int]) -> int:
        left , right = 0, len(nums) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            if nums[left] == nums[mid] == nums[right]:
                left += 1
                right -= 1
            elif nums[mid] <= nums[right]:
                right = mid
            else:
                left = mid

        return min(nums[left], nums[right])

# @lc code=end

