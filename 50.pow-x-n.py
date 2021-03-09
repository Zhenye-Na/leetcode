#
# @lc app=leetcode id=50 lang=python3
#
# [50] Pow(x, n)
#
# https://leetcode.com/problems/powx-n/description/
#
# algorithms
# Medium (30.84%)
# Likes:    2179
# Dislikes: 3634
# Total Accepted:    603.2K
# Total Submissions: 1.9M
# Testcase Example:  '2.00000\n10'
#
# Implement pow(x, n), which calculates x raised to the power n (i.e. x^n).
# 
# 
# Example 1:
# 
# 
# Input: x = 2.00000, n = 10
# Output: 1024.00000
# 
# 
# Example 2:
# 
# 
# Input: x = 2.10000, n = 3
# Output: 9.26100
# 
# 
# Example 3:
# 
# 
# Input: x = 2.00000, n = -2
# Output: 0.25000
# Explanation: 2^-2 = 1/2^2 = 1/4 = 0.25
# 
# 
# 
# Constraints:
# 
# 
# -100.0 < x < 100.0
# -2^31 <= n <= 2^31-1
# -10^4 <= x^n <= 10^4
# 
# 
#

# @lc code=start
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if (x == 0):
            return 0

        if (n == 0):
            return 1

        if (n == 1):
            return x

        if n < 0:
            x = 1 / x
            n = - n

        tmp = self.myPow(x, n // 2)

        if (n % 2 == 0):
            return tmp * tmp
        else:
            return x * tmp * tmp
# @lc code=end

