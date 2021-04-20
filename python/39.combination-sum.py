#
# @lc app=leetcode id=39 lang=python3
#
# [39] Combination Sum
#
# https://leetcode.com/problems/combination-sum/description/
#
# algorithms
# Medium (58.89%)
# Likes:    5551
# Dislikes: 144
# Total Accepted:    696.6K
# Total Submissions: 1.2M
# Testcase Example:  '[2,3,6,7]\n7'
#
# Given an array of distinct integers candidates and a target integer target,
# return a list of all unique combinations of candidates where the chosen
# numbers sum to target. You may return the combinations in any order.
# 
# The same number may be chosen from candidates an unlimited number of times.
# Two combinations are unique if the frequency of at least one of the chosen
# numbers is different.
# 
# It is guaranteed that the number of unique combinations that sum up to target
# is less than 150 combinations for the given input.
# 
# 
# Example 1:
# 
# 
# Input: candidates = [2,3,6,7], target = 7
# Output: [[2,2,3],[7]]
# Explanation:
# 2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple
# times.
# 7 is a candidate, and 7 = 7.
# These are the only two combinations.
# 
# 
# Example 2:
# 
# 
# Input: candidates = [2,3,5], target = 8
# Output: [[2,2,2,2],[2,3,3],[3,5]]
# 
# 
# Example 3:
# 
# 
# Input: candidates = [2], target = 1
# Output: []
# 
# 
# Example 4:
# 
# 
# Input: candidates = [1], target = 1
# Output: [[1]]
# 
# 
# Example 5:
# 
# 
# Input: candidates = [1], target = 2
# Output: [[1,1]]
# 
# 
# 
# Constraints:
# 
# 
# 1 <= candidates.length <= 30
# 1 <= candidates[i] <= 200
# All elements of candidates are distinct.
# 1 <= target <= 500
# 
# 
#

# @lc code=start
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        if not candidates or len(candidates) == 0:
            return []

        candidates.sort()
        res = []
        self._dfs(candidates, target, [], 0, res)

        return res

    def _dfs(self, candidates, target, curr, start_index, res):
        if target < 0:
            return

        if target == 0:
            res.append(curr[:])
            return


        for i in range(start_index, len(candidates)):
            if candidates[i] > target:
                continue
            
            curr.append(candidates[i])
            self._dfs(candidates, target - candidates[i], curr, i, res)
            curr.pop()
# @lc code=end

