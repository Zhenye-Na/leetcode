#
# @lc app=leetcode id=462 lang=python3
#
# [462] Minimum Moves to Equal Array Elements II
#
# https://leetcode.com/problems/minimum-moves-to-equal-array-elements-ii/description/
#
# algorithms
# Medium (54.30%)
# Likes:    881
# Dislikes: 60
# Total Accepted:    67K
# Total Submissions: 120.8K
# Testcase Example:  '[1,2,3]'
#
# Given an integer array nums of size n, return the minimum number of moves
# required to make all array elements equal.
# 
# In one move, you can increment or decrement an element of the array by 1.
# 
# 
# Example 1:
# 
# 
# Input: nums = [1,2,3]
# Output: 2
# Explanation:
# Only two moves are needed (remember each move increments or decrements one
# element):
# [1,2,3]  =>  [2,2,3]  =>  [2,2,2]
# 
# 
# Example 2:
# 
# 
# Input: nums = [1,10,2,9]
# Output: 16
# 
# 
# 
# Constraints:
# 
# 
# n == nums.length
# 1 <= nums.length <= 10^5
# -10^9 <= nums[i] <= 10^9
# 
# 
#

# @lc code=start
class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        ans = 0
        median = nums[len(nums) // 2]
        for i in range(len(nums)):
            ans += abs(nums[i] - median)

        return ans
# @lc code=end

