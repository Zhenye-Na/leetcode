#
# @lc app=leetcode id=198 lang=python3
#
# [198] House Robber
#
# https://leetcode.com/problems/house-robber/description/
#
# algorithms
# Medium (42.77%)
# Likes:    6670
# Dislikes: 187
# Total Accepted:    688.8K
# Total Submissions: 1.6M
# Testcase Example:  '[1,2,3,1]'
#
# You are a professional robber planning to rob houses along a street. Each
# house has a certain amount of money stashed, the only constraint stopping you
# from robbing each of them is that adjacent houses have security systems
# connected and it will automatically contact the police if two adjacent houses
# were broken into on the same night.
# 
# Given an integer array nums representing the amount of money of each house,
# return the maximum amount of money you can rob tonight without alerting the
# police.
# 
# 
# Example 1:
# 
# 
# Input: nums = [1,2,3,1]
# Output: 4
# Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
# Total amount you can rob = 1 + 3 = 4.
# 
# 
# Example 2:
# 
# 
# Input: nums = [2,7,9,3,1]
# Output: 12
# Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5
# (money = 1).
# Total amount you can rob = 2 + 9 + 1 = 12.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 100
# 0 <= nums[i] <= 400
# 
# 
#

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
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

