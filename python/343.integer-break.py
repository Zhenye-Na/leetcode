#
# @lc app=leetcode id=343 lang=python3
#
# [343] Integer Break
#
# https://leetcode.com/problems/integer-break/description/
#
# algorithms
# Medium (56.72%)
# Likes:    4046
# Dislikes: 381
# Total Accepted:    255.4K
# Total Submissions: 446.5K
# Testcase Example:  '2'
#
# Given an integer n, break it into the sum of k positive integers, where k >=
# 2, and maximize the product of those integers.
# 
# Return the maximum product you can get.
# 
# 
# Example 1:
# 
# 
# Input: n = 2
# Output: 1
# Explanation: 2 = 1 + 1, 1 × 1 = 1.
# 
# 
# Example 2:
# 
# 
# Input: n = 10
# Output: 36
# Explanation: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36.
# 
# 
# 
# Constraints:
# 
# 
# 2 <= n <= 58
# 
# 
#

# @lc code=start
class Solution:
    def integerBreak(self, n: int) -> int:

        dp = [0 for _ in range(n + 1)]

        dp[0] = 1
        dp[1] = 1
        dp[2] = 1
        for i in range(3, n + 1):
            val = dp[i]
            for j in range(2, i):
                val = max(val, max(j, dp[j]) * max(i - j, dp[i - j]))
            
            dp[i] = val

        return dp[n]
# @lc code=end

