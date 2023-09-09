#
# @lc app=leetcode id=377 lang=python3
#
# [377] Combination Sum IV
#
# https://leetcode.com/problems/combination-sum-iv/description/
#
# algorithms
# Medium (45.93%)
# Likes:    1986
# Dislikes: 236
# Total Accepted:    154.8K
# Total Submissions: 334.8K
# Testcase Example:  '[1,2,3]\n4'
#
# Given an array of distinct integers nums and a target integer target, return
# the number of possible combinations that add up to target.
# 
# The answer is guaranteed to fit in a 32-bit integer.
# 
# 
# Example 1:
# 
# 
# Input: nums = [1,2,3], target = 4
# Output: 7
# Explanation:
# The possible combination ways are:
# (1, 1, 1, 1)
# (1, 1, 2)
# (1, 2, 1)
# (1, 3)
# (2, 1, 1)
# (2, 2)
# (3, 1)
# Note that different sequences are counted as different combinations.
# 
# 
# Example 2:
# 
# 
# Input: nums = [9], target = 3
# Output: 0
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 200
# 1 <= nums[i] <= 1000
# All the elements of nums are unique.
# 1 <= target <= 1000
# 
# 
# 
# Follow up: What if negative numbers are allowed in the given array? How does
# it change the problem? What limitation we need to add to the question to
# allow negative numbers?
# 
#

# @lc code=start

# Run time: 32 ms
# Memory: 14.3 MB
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        nums.sort()

        # f[i] represents the number of combinations that add up to i
        f = [0 for _ in range(target + 1)]
        f[0] = 1

        for i in range(target + 1):
            for num in nums:
                if num > i:
                    break

                f[i] += f[i - num]

        return f[target]


class Solution_DFS:

    def combinationSum4(self, nums: List[int], target: int) -> int:
        self.res = set([])
        nums.sort()
        self.dfs(nums, target, [], 0)

        return len(self.res)


    def dfs(self, nums, target, curr, start):
        if target == 0:
            combination = tuple(curr[:])
            if combination not in self.res:
                self.res.add(combination)
            return

        for i in range(start, len(nums)):
            if nums[i] > target:
                continue

            curr.append(nums[i])
            self.dfs(nums, target - nums[i], curr, 0)
            curr.pop()
# @lc code=end

