#
# @lc app=leetcode id=673 lang=python3
#
# [673] Number of Longest Increasing Subsequence
#
# https://leetcode.com/problems/number-of-longest-increasing-subsequence/description/
#
# algorithms
# Medium (38.40%)
# Likes:    2157
# Dislikes: 116
# Total Accepted:    76.3K
# Total Submissions: 197.7K
# Testcase Example:  '[1,3,5,4,7]'
#
# Given an integer array nums, return the number of longest increasing
# subsequences.
# 
# Notice that the sequence has to be strictly increasing.
# 
# 
# Example 1:
# 
# 
# Input: nums = [1,3,5,4,7]
# Output: 2
# Explanation: The two longest increasing subsequences are [1, 3, 4, 7] and [1,
# 3, 5, 7].
# 
# 
# Example 2:
# 
# 
# Input: nums = [2,2,2,2,2]
# Output: 5
# Explanation: The length of longest continuous increasing subsequence is 1,
# and there are 5 subsequences' length is 1, so output 5.
# 
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 2000
# -10^6 <= nums[i] <= 10^6
# 
# 
#

# @lc code=start
class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        if not nums or len(nums) == 0:
            return 0

        n = len(nums)

        # initialization
        # length[i] represents, the length of LIS ending with nums[i]
        # counts[i] represents, how many subarray ending with nums[i] have the max length of LIS
        length = [1 for _ in range(n)]
        counts = [1 for _ in range(n)]

        for i in range(1, n):
            for j in range(i):
                if nums[j] < nums[i]:
                    if length[j] + 1 > length[i]:
                        # update length and counts
                        length[i] = length[j] + 1
                        counts[i] = counts[j]
                    elif length[j] + 1 == length[i]:
                        # current length is already the same
                        # update counts
                        counts[i] += counts[j]

        max_len = 0
        res = 0
        for i in range(n):
            if length[i] > max_len:
                max_len = length[i]
                res = counts[i]
            elif length[i] == max_len:
                res += counts[i]

        return res
# @lc code=end

