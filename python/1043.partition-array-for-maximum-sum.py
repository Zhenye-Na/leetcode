#
# @lc app=leetcode id=1043 lang=python3
#
# [1043] Partition Array for Maximum Sum
#
# https://leetcode.com/problems/partition-array-for-maximum-sum/description/
#
# algorithms
# Medium (72.19%)
# Likes:    3751
# Dislikes: 255
# Total Accepted:    93K
# Total Submissions: 128.2K
# Testcase Example:  '[1,15,7,9,2,5,10]\n3'
#
# Given an integer array arr, partition the array into (contiguous) subarrays
# of length at most k. After partitioning, each subarray has their values
# changed to become the maximum value of that subarray.
# 
# Return the largest sum of the given array after partitioning. Test cases are
# generated so that the answer fits in a 32-bit integer.
# 
# 
# Example 1:
# 
# 
# Input: arr = [1,15,7,9,2,5,10], k = 3
# Output: 84
# Explanation: arr becomes [15,15,15,9,10,10,10]
# 
# 
# Example 2:
# 
# 
# Input: arr = [1,4,1,5,7,3,6,1,9,9,3], k = 4
# Output: 83
# 
# 
# Example 3:
# 
# 
# Input: arr = [1], k = 1
# Output: 1
# 
# 
# 
# Constraints:
# 
# 
# 1 <= arr.length <= 500
# 0 <= arr[i] <= 10^9
# 1 <= k <= arr.length
# 
# 
#

# @lc code=start
class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:

        dp = [0] * (len(arr) + 1)
        for i in range(1, len(arr) + 1):
            end = i - 1 
            start = max(end - k, -1)
            curr_max = 0

            for p in range(end, start, -1):
                curr_max = max(curr_max, arr[p])
                dp[i] = max(dp[i], dp[p] + curr_max * (i - p))

        return dp[-1]
# @lc code=end

