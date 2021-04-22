#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#
# https://leetcode.com/problems/two-sum/description/
#
# algorithms
# Easy (46.28%)
# Likes:    18950
# Dislikes: 675
# Total Accepted:    3.8M
# Total Submissions: 8.2M
# Testcase Example:  '[2,7,11,15]\n9'
#
# Given an array of integers nums and an integer target, return indices of the
# two numbers such that they add up to target.
# 
# You may assume that each input would have exactly one solution, and you may
# not use the same element twice.
# 
# You can return the answer in any order.
# 
# 
# Example 1:
# 
# 
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Output: Because nums[0] + nums[1] == 9, we return [0, 1].
# 
# 
# Example 2:
# 
# 
# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# 
# 
# Example 3:
# 
# 
# Input: nums = [3,3], target = 6
# Output: [0,1]
# 
# 
# 
# Constraints:
# 
# 
# 2 <= nums.length <= 10^3
# -10^9 <= nums[i] <= 10^9
# -10^9 <= target <= 10^9
# Only one valid answer exists.
# 
# 
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) < 2:
            return [-1, -1]

        nums_idx = [idx for idx, num in sorted(enumerate(nums), key=lambda x: x[1])]
        nums.sort()

        left, right = 0, len(nums) - 1
        while left + 1 <= right:
            if nums[left] + nums[right] == target:
                return sorted([nums_idx[left], nums_idx[right]])
            elif nums[left] + nums[right] > target:
                right -= 1
            else:
                left += 1

        return [-1, -1]
# @lc code=end

