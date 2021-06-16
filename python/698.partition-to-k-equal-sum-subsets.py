#
# @lc app=leetcode id=698 lang=python3
#
# [698] Partition to K Equal Sum Subsets
#
# https://leetcode.com/problems/partition-to-k-equal-sum-subsets/description/
#
# algorithms
# Medium (44.94%)
# Likes:    3134
# Dislikes: 200
# Total Accepted:    131.4K
# Total Submissions: 292.2K
# Testcase Example:  '[4,3,2,3,5,2,1]\n4'
#
# Given an integer array nums and an integer k, return true if it is possible
# to divide this array into k non-empty subsets whose sums are all equal.
# 
# 
# Example 1:
# 
# 
# Input: nums = [4,3,2,3,5,2,1], k = 4
# Output: true
# Explanation: It's possible to divide it into 4 subsets (5), (1, 4), (2,3),
# (2,3) with equal sums.
# 
# 
# Example 2:
# 
# 
# Input: nums = [1,2,3,4], k = 3
# Output: false
# 
# 
# 
# Constraints:
# 
# 
# 1 <= k <= nums.length <= 16
# 1 <= nums[i] <= 10^4
# The frequency of each element is in the range [1, 4].
# 
# 
#

# @lc code=start
class Solution:
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

