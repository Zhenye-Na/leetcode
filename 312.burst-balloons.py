#
# @lc app=leetcode id=312 lang=python3
#
# [312] Burst Balloons
#
# https://leetcode.com/problems/burst-balloons/description/
#
# algorithms
# Hard (53.66%)
# Likes:    3449
# Dislikes: 103
# Total Accepted:    131.1K
# Total Submissions: 243.5K
# Testcase Example:  '[3,1,5,8]'
#
# You are given n balloons, indexed from 0 to n - 1. Each balloon is painted
# with a number on it represented by an array nums. You are asked to burst all
# the balloons.
# 
# If you burst the i^th balloon, you will get nums[i - 1] * nums[i] * nums[i +
# 1] coins. If i - 1 or i + 1 goes out of bounds of the array, then treat it as
# if there is a balloon with a 1 painted on it.
# 
# Return the maximum coins you can collect by bursting the balloons wisely.
# 
# 
# Example 1:
# 
# 
# Input: nums = [3,1,5,8]
# Output: 167
# Explanation:
# nums = [3,1,5,8] --> [3,5,8] --> [3,8] --> [8] --> []
# coins =  3*1*5    +   3*5*8   +  1*3*8  + 1*8*1 = 167
# 
# Example 2:
# 
# 
# Input: nums = [1,5]
# Output: 10
# 
# 
# 
# Constraints:
# 
# 
# n == nums.length
# 1 <= n <= 500
# 0 <= nums[i] <= 100
# 
# 
#

# @lc code=start
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        n = len(nums)
        nums.insert(0, 1)
        nums.append(1)

        f = [[0 for _ in range(n + 2)] for _ in range(n + 2)]

        for l in range(1, n + 1):
            for i in range(1, (n - l + 1) + 1):
                j = i + l - 1
                for k in range(i, j + 1):
                    f[i][j] = max(f[i][j], f[i][k - 1] + f[k + 1][j] + nums[i - 1] * nums[k] * nums[j + 1])

        return f[1][n]
# @lc code=end

