#
# @lc app=leetcode id=300 lang=python3
#
# [300] Longest Increasing Subsequence
#
# https://leetcode.com/problems/longest-increasing-subsequence/description/
#
# algorithms
# Medium (43.74%)
# Likes:    6689
# Dislikes: 153
# Total Accepted:    512.2K
# Total Submissions: 1.2M
# Testcase Example:  '[10,9,2,5,3,7,101,18]'
#
# Given an integer array nums, return the length of the longest strictly
# increasing subsequence.
# 
# A subsequence is a sequence that can be derived from an array by deleting
# some or no elements without changing the order of the remaining elements. For
# example, [3,6,2,7] is a subsequence of the array [0,3,1,6,2,2,7].
# 
# 
# Example 1:
# 
# 
# Input: nums = [10,9,2,5,3,7,101,18]
# Output: 4
# Explanation: The longest increasing subsequence is [2,3,7,101], therefore the
# length is 4.
# 
# 
# Example 2:
# 
# 
# Input: nums = [0,1,0,3,2,3]
# Output: 4
# 
# 
# Example 3:
# 
# 
# Input: nums = [7,7,7,7,7,7,7]
# Output: 1
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 2500
# -10^4 <= nums[i] <= 10^4
# 
# 
# 
# Follow up:
# 
# 
# Could you come up with the O(n^2) solution?
# Could you improve it to O(n log(n)) time complexity?
# 
# 
#

# @lc code=start

# Dynamic Programming + Greedy + Binary Search
#   https://www.youtube.com/watch?v=l2rCz7skAlk&ab_channel=HuaHua
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        res = []
        for num in nums:
            idx = bisect_left(res, num)
            if idx == len(res):
                res.append(num)
            else:
                res[idx] = num

        return len(res)


class Solution_DP:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # initialization
        # every single number consist one increasing subseq
        dp = [1 for _ in range(len(nums))]

        for i in range(len(nums)):
            for j in range(0, i):
                if nums[i] > nums[j]:
                    # if current number is greater than prev number
                    # we can create a new subseq with length + 1, or current length
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)
# @lc code=end

