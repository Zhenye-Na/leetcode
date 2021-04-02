#
# @lc app=leetcode id=18 lang=python3
#
# [18] 4Sum
#
# https://leetcode.com/problems/4sum/description/
#
# algorithms
# Medium (34.69%)
# Likes:    3133
# Dislikes: 405
# Total Accepted:    402.2K
# Total Submissions: 1.1M
# Testcase Example:  '[1,0,-1,0,-2,2]\n0'
#
# Given an array nums of n integers and an integer target, are there elements
# a, b, c, and d in nums such that a + b + c + d = target? Find all unique
# quadruplets in the array which gives the sum of target.
# 
# Notice that the solution set must not contain duplicate quadruplets.
# 
# 
# Example 1:
# Input: nums = [1,0,-1,0,-2,2], target = 0
# Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
# Example 2:
# Input: nums = [], target = 0
# Output: []
# 
# 
# Constraints:
# 
# 
# 0 <= nums.length <= 200
# -10^9 <= nums[i] <= 10^9
# -10^9 <= target <= 10^9
# 
# 
#

# @lc code=start
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        self.res = []
        nums.sort()
        self.dfs(nums, target, 4, [])

        return self.res


    def dfs(self, nums, target, k, curr):
        if k == 0 and target == 0:
            self.res.append(curr[:])
            return

        if len(nums) == 0 or nums[0] * k > target or target > nums[-1] * k:
            return

        for i in range(len(nums)):
            if i == 0 or nums[i - 1] != nums[i]:
                curr.append(nums[i])
                self.dfs(nums[i + 1:], target - nums[i], k - 1, curr)
                curr.pop()
# @lc code=end

