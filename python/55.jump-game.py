#
# @lc app=leetcode id=55 lang=python3
#
# [55] Jump Game
#
# https://leetcode.com/problems/jump-game/description/
#
# algorithms
# Medium (32.70%)
# Likes:    2490
# Dislikes: 237
# Total Accepted:    316K
# Total Submissions: 966.5K
# Testcase Example:  '[2,3,1,1,4]'
#
# Given an array of non-negative integers, you are initially positioned at the
# first index of the array.
# 
# Each element in the array represents your maximum jump length at that
# position.
# 
# Determine if you are able to reach the last index.
# 
# Example 1:
# 
# 
# Input: [2,3,1,1,4]
# Output: true
# Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
# 
# 
# Example 2:
# 
# 
# Input: [3,2,1,0,4]
# Output: false
# Explanation: You will always arrive at index 3 no matter what. Its
# maximum
# jump length is 0, which makes it impossible to reach the last index.
# 
# 
#

# @lc code=start
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # Dynamic Programming
        # state: f[i] represents whether can jump to ith position
        f = [False] * len(nums)
        f[0] = True

        # function: f[i] <- f[j] and f[j] + j > i for j in 0 ... i
        for i in range(len(nums)):
            for j in range(i):
                if f[j] and f[j] + j >= i:
                    f[i] = True
                    break

        return f[-1]
# @lc code=end

