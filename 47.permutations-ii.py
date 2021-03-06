#
# @lc app=leetcode id=47 lang=python3
#
# [47] Permutations II
#
# https://leetcode.com/problems/permutations-ii/description/
#
# algorithms
# Medium (49.10%)
# Likes:    2784
# Dislikes: 77
# Total Accepted:    436.4K
# Total Submissions: 882.3K
# Testcase Example:  '[1,1,2]'
#
# Given a collection of numbers, nums, that might contain duplicates, return
# all possible unique permutations in any order.
# 
# 
# Example 1:
# 
# 
# Input: nums = [1,1,2]
# Output:
# [[1,1,2],
# ⁠[1,2,1],
# ⁠[2,1,1]]
# 
# 
# Example 2:
# 
# 
# Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 8
# -10 <= nums[i] <= 10
# 
# 
#

# @lc code=start
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        permutations = []
        nums.sort()
        self.visited = [False for _ in range(len(nums))]
        self._dfs(nums, permutations, [])
        return permutations


    def _dfs(self, nums, permutations, curr):
        if len(curr) == len(nums):
            permutations.append(curr[:])
            return

        for i in range(len(nums)):
                if self.visited[i]  or (i > 0 and nums[i - 1] == nums[i] and not self.visited[i - 1]):
                    continue

                self.visited[i] = True
                curr.append(nums[i])
                self._dfs(nums, permutations, curr)
                curr.pop()
                self.visited[i] = False

# @lc code=end

