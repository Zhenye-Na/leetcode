#
# @lc app=leetcode id=213 lang=python3
#
# [213] House Robber II
#
# https://leetcode.com/problems/house-robber-ii/description/
#
# algorithms
# Medium (37.45%)
# Likes:    2687
# Dislikes: 63
# Total Accepted:    233.2K
# Total Submissions: 620.4K
# Testcase Example:  '[2,3,2]'
#
# You are a professional robber planning to rob houses along a street. Each
# house has a certain amount of money stashed. All houses at this place are
# arranged in a circle. That means the first house is the neighbor of the last
# one. Meanwhile, adjacent houses have a security system connected, and it will
# automatically contact the police if two adjacent houses were broken into on
# the same night.
# 
# Given an integer array nums representing the amount of money of each house,
# return the maximum amount of money you can rob tonight without alerting the
# police.
# 
# 
# Example 1:
# 
# 
# Input: nums = [2,3,2]
# Output: 3
# Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money =
# 2), because they are adjacent houses.
# 
# 
# Example 2:
# 
# 
# Input: nums = [1,2,3,1]
# Output: 4
# Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
# Total amount you can rob = 1 + 3 = 4.
# 
# 
# Example 3:
# 
# 
# Input: nums = [0]
# Output: 0
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 100
# 0 <= nums[i] <= 1000
# 
# 
#

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        return max(
            self._rob(nums[:len(nums) - 1]),
            self._rob(nums[1:])
        )


    def _rob(self, nums):
        if not nums:
            return 0

        # initilization
        # dp[i][j] represents
        #   for house i_th, 0 reprents dont rob, 1 stands for rob it
        dp = [[0 for _ in range(2)] for _ in range(len(nums))]
        dp[0][0] = 0
        dp[0][1] = nums[0]

        for i in range(1, len(nums)):
            # we do not rob current house
            #   which means i-1 house could be robbed or not, we just select the maximum
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1])

            # if we decide to rob the current house
            #   which means the previous house should not be robbed before
            dp[i][1] = dp[i - 1][0] + nums[i]

        # return the max value for two state for last house
        return max(dp[-1])
# @lc code=end

