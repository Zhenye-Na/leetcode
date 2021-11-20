#
# @lc app=leetcode id=540 lang=python3
#
# [540] Single Element in a Sorted Array
#
# https://leetcode.com/problems/single-element-in-a-sorted-array/description/
#
# algorithms
# Medium (58.01%)
# Likes:    3544
# Dislikes: 93
# Total Accepted:    223.8K
# Total Submissions: 385.3K
# Testcase Example:  '[1,1,2,3,3,4,4,8,8]'
#
# You are given a sorted array consisting of only integers where every element
# appears exactly twice, except for one element which appears exactly once.
# 
# Return the single element that appears only once.
# 
# Your solution must run in O(log n) time and O(1) space.
# 
# 
# Example 1:
# Input: nums = [1,1,2,3,3,4,4,8,8]
# Output: 2
# Example 2:
# Input: nums = [3,3,7,7,10,11,11]
# Output: 10
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 10^5
# 0 <= nums[i] <= 10^5
# 
# 
#

# @lc code=start
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        if not nums or len(nums) == 0:
            return -1
        
        left, right = 0, len(nums) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            
            if mid % 2 == 0:
                if not (nums[mid - 1] < nums[mid] and nums[mid] == nums[mid + 1]):
                    right = mid
                elif nums[mid - 1] < nums[mid] and nums[mid] == nums[mid + 1]:
                    left = mid
                else:
                    return nums[mid]
            else:
                if not (nums[mid - 1] == nums[mid] and nums[mid] < nums[mid + 1]):
                    right = mid
                elif nums[mid - 1] == nums[mid] and nums[mid] < nums[mid + 1]:
                    left = mid
                else:
                    return nums[mid]
                
        if left - 1 >= 0 and nums[left] == nums[left - 1]:
            return nums[right]
        
        return nums[left]
# @lc code=end

