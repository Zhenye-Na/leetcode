#
# @lc app=leetcode id=78 lang=python3
#
# [78] Subsets
#
# https://leetcode.com/problems/subsets/description/
#
# algorithms
# Medium (64.66%)
# Likes:    5346
# Dislikes: 109
# Total Accepted:    728.5K
# Total Submissions: 1.1M
# Testcase Example:  '[1,2,3]'
#
# Given an integer array nums of unique elements, return all possible subsets
# (the power set).
# 
# The solution set must not contain duplicate subsets. Return the solution in
# any order.
# 
# 
# Example 1:
# 
# 
# Input: nums = [1,2,3]
# Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
# 
# 
# Example 2:
# 
# 
# Input: nums = [0]
# Output: [[],[0]]
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 10
# -10 <= nums[i] <= 10
# All the numbers of nums are unique.
# 
# 
#

# @lc code=start
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        self._dfs(nums, [], res, 0)
        return res


    def _dfs(self, nums, curr, res, start):
        # exit
        res.append(curr[:])

        for i in range(start, len(nums)):
            curr.append(nums[i])
            self._dfs(nums, curr, res, i + 1)
            curr.pop()
# @lc code=end

