#
# @lc app=leetcode id=416 lang=python3
#
# [416] Partition Equal Subset Sum
#
# https://leetcode.com/problems/partition-equal-subset-sum/description/
#
# algorithms
# Medium (45.36%)
# Likes:    6111
# Dislikes: 101
# Total Accepted:    364.9K
# Total Submissions: 795.4K
# Testcase Example:  '[1,5,11,5]'
#
# Given a non-empty array nums containing only positive integers, find if the
# array can be partitioned into two subsets such that the sum of elements in
# both subsets is equal.
# 
# 
# Example 1:
# 
# 
# Input: nums = [1,5,11,5]
# Output: true
# Explanation: The array can be partitioned as [1, 5, 5] and [11].
# 
# 
# Example 2:
# 
# 
# Input: nums = [1,2,3,5]
# Output: false
# Explanation: The array cannot be partitioned into equal sum subsets.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 200
# 1 <= nums[i] <= 100
# 
# 
#

# @lc code=start
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if not nums or len(nums) == 0:
            return True

        total_sum = sum(nums)
        if total_sum % 2 != 0:
            return False

        subset_sum = total_sum // 2

        dp = [False for _ in range(subset_sum + 1)]
        dp[0] = True
    
        for num in nums:
            for curr in range(subset_sum, -1, -1):
                if curr >= num:
                    dp[curr] = dp[curr] or dp[curr - num]
                if curr == subset_sum and dp[curr]:
                    return True

        return dp[subset_sum]
# @lc code=end

