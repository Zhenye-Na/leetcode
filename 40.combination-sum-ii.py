#
# @lc app=leetcode id=40 lang=python3
#
# [40] Combination Sum II
#
# https://leetcode.com/problems/combination-sum-ii/description/
#
# algorithms
# Medium (49.91%)
# Likes:    2542
# Dislikes: 86
# Total Accepted:    392.7K
# Total Submissions: 782K
# Testcase Example:  '[10,1,2,7,6,1,5]\n8'
#
# Given a collection of candidate numbers (candidates) and a target number
# (target), find all unique combinations in candidates where the candidate
# numbers sum to target.
# 
# Each number in candidates may only be used once in the combination.
# 
# Note: The solution set must not contain duplicate combinations.
# 
# 
# Example 1:
# 
# 
# Input: candidates = [10,1,2,7,6,1,5], target = 8
# Output: 
# [
# [1,1,6],
# [1,2,5],
# [1,7],
# [2,6]
# ]
# 
# 
# Example 2:
# 
# 
# Input: candidates = [2,5,2,1,2], target = 5
# Output: 
# [
# [1,2,2],
# [5]
# ]
# 
# 
# 
# Constraints:
# 
# 
# 1 <= candidates.length <= 100
# 1 <= candidates[i] <= 50
# 1 <= target <= 30
# 
# 
#

# @lc code=start
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        if not candidates or len(candidates) == 0:
            return []

        res = []
        visited = [0 for _ in range(len(candidates))]
        candidates.sort()
        self._dfs(candidates, target, [], res, 0, visited)

        return res

    def _dfs(self, candidates, target, curr, res, start, visited):
        if target < 0:
            return

        if target == 0:
            res.append(curr[:])
            return

        for i in range(start, len(candidates)):
            if i != start and candidates[i] == candidates[i - 1] and visited[i - 1] == 0:
                continue
            
            if candidates[i] > target:
                continue

            curr.append(candidates[i])
            visited[i] = 1
            self._dfs(candidates, target - candidates[i], curr, res, i + 1, visited)
            curr.pop()
            visited[i] = 0
# @lc code=end

