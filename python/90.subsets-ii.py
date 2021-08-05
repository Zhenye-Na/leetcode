#
# @lc app=leetcode id=90 lang=python3
#
# [90] Subsets II
#
# https://leetcode.com/problems/subsets-ii/description/
#
# algorithms
# Medium (48.59%)
# Likes:    2306
# Dislikes: 102
# Total Accepted:    328.5K
# Total Submissions: 672K
# Testcase Example:  '[1,2,2]'
#
# Given an integer array nums that may contain duplicates, return all possible
# subsets (the power set).
# 
# The solution set must not contain duplicate subsets. Return the solution in
# any order.
# 
# 
# Example 1:
# Input: nums = [1,2,2]
# Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
# Example 2:
# Input: nums = [0]
# Output: [[],[0]]
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 10
# -10 <= nums[i] <= 10
# 
# 
#

# @lc code=start
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        self._dfs(nums, res, [], 0)
        return res


    def _dfs(self, nums, res, curr, start):
        res.append(curr[:])

        for i in range(start, len(nums)):
            if i > start and nums[i - 1] == nums[i]:
                continue

            curr.append(nums[i])
            self._dfs(nums, res, curr, i + 1)
            curr.pop()
# @lc code=end

