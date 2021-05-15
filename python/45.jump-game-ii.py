#
# @lc app=leetcode id=45 lang=python3
#
# [45] Jump Game II
#
# https://leetcode.com/problems/jump-game-ii/description/
#
# algorithms
# Hard (31.31%)
# Likes:    3703
# Dislikes: 171
# Total Accepted:    316.6K
# Total Submissions: 1M
# Testcase Example:  '[2,3,1,1,4]'
#
# Given an array of non-negative integers nums, you are initially positioned at
# the first index of the array.
# 
# Each element in the array represents your maximum jump length at that
# position.
# 
# Your goal is to reach the last index in the minimum number of jumps.
# 
# You can assume that you can always reach the last index.
# 
# 
# Example 1:
# 
# 
# Input: nums = [2,3,1,1,4]
# Output: 2
# Explanation: The minimum number of jumps to reach the last index is 2. Jump 1
# step from index 0 to 1, then 3 steps to the last index.
# 
# 
# Example 2:
# 
# 
# Input: nums = [2,3,0,1,4]
# Output: 2
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 3 * 10^4
# 0 <= nums[i] <= 10^5
# 
# 
#

# @lc code=start
class Solution:
    def jump(self, nums: List[int]) -> int:
        if not nums or len(nums) == 0:
            return 0

        length = len(nums)
        steps= [length + 1 for _ in range(length)]
        steps[0] = 0
        for i in range(length):
            for j in range(i):
                if nums[j] + j >= i:
                    steps[i] = min(steps[i], steps[j] + 1)

        return steps[-1]
# @lc code=end

