#
# @lc app=leetcode id=473 lang=python3
#
# [473] Matchsticks to Square
#
# https://leetcode.com/problems/matchsticks-to-square/description/
#
# algorithms
# Medium (38.50%)
# Likes:    1096
# Dislikes: 99
# Total Accepted:    59.7K
# Total Submissions: 149.8K
# Testcase Example:  '[1,1,2,2,2]'
#
# You are given an integer array matchsticks where matchsticks[i] is the length
# of the i^th matchstick. You want to use all the matchsticks to make one
# square. You should not break any stick, but you can link them up, and each
# matchstick must be used exactly one time.
# 
# Return true if you can make this square and false otherwise.
# 
# 
# Example 1:
# 
# 
# Input: matchsticks = [1,1,2,2,2]
# Output: true
# Explanation: You can form a square with length 2, one side of the square came
# two sticks with length 1.
# 
# 
# Example 2:
# 
# 
# Input: matchsticks = [3,3,3,3,4]
# Output: false
# Explanation: You cannot find a way to form a square with all the
# matchsticks.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= matchsticks.length <= 15
# 0 <= matchsticks[i] <= 10^9
# 
# 
#

# @lc code=start
class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        return self.canPartitionKSubsets(matchsticks, 4)


    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if not nums or len(nums) == 0 or sum(nums) % k != 0:
            return False

        nums.sort(reverse=True)

        self.k = k
        self.target = sum(nums) // k
        self.seen = [False for _ in range(16)]

        return self.dfs(nums, 0, 0, 0)


    def dfs(self, nums, start, group, curr):
        if group == self.k:
            return True
        
        if curr > self.target:
            return False

        if curr == self.target:
            return self.dfs(nums, 0, group + 1, 0)

        for i in range(start, len(nums)):
            if self.seen[i]:
                continue

            self.seen[i] = True
            if self.dfs(nums, i + 1, group, curr + nums[i]):
                return True
            self.seen[i] = False
        return False
# @lc code=end

