#
# @lc app=leetcode id=1922 lang=python3
#
# [1922] Count Good Numbers
#
# https://leetcode.com/problems/count-good-numbers/description/
#
# algorithms
# Medium (39.20%)
# Likes:    1064
# Dislikes: 363
# Total Accepted:    35.1K
# Total Submissions: 83.6K
# Testcase Example:  '1'
#
# A digit string is good if the digits (0-indexed) at even indices are even and
# the digits at odd indices are prime (2, 3, 5, or 7).
# 
# 
# For example, "2582" is good because the digits (2 and 8) at even positions
# are even and the digits (5 and 2) at odd positions are prime. However, "3245"
# is not good because 3 is at an even index but is not even.
# 
# 
# Given an integer n, return the total number of good digit strings of length
# n. Since the answer may be large, return it modulo 10^9 + 7.
# 
# A digit string is a string consisting of digits 0 through 9 that may contain
# leading zeros.
# 
# 
# Example 1:
# 
# 
# Input: n = 1
# Output: 5
# Explanation: The good numbers of length 1 are "0", "2", "4", "6", "8".
# 
# 
# Example 2:
# 
# 
# Input: n = 4
# Output: 400
# 
# 
# Example 3:
# 
# 
# Input: n = 50
# Output: 564908303
# 
# 
# 
# Constraints:
# 
# 
# 1 <= n <= 10^15
# 
# 
#

# @lc code=start
class Solution:
    def countGoodNumbers(self, n: int) -> int:
        mod = 10 ** 9 + 7
        res = 1

        if n % 2 == 0:
            res *= pow(4, n // 2, mod)
            res *= pow(5, n // 2, mod)
            res %= mod
        else:
            res *= pow(4, n // 2, mod)
            res *= pow(5, (n + 1) // 2, mod)
            res %= mod

        return res


class Solution_DP:
    def countGoodNumbers(self, n: int) -> int:
        # dp initialization
        # f[i][j] represents the number of good number length i, ending with digit[j]

        f = [[0 for _ in range(10)] for _ in range(n)]
        mod = 10 ** 9 + 7
        for j in range(10):
            f[0][j] = 1 if j % 2 == 0 else 0

        for i in range(1, n):
            for j in range(10):
                if i % 2 == 0:
                    if j % 2 == 0:
                        for k in range(10):
                            if k in self.primes:
                                f[i][j] += f[i - 1][k]
                    else:
                        f[i][j] = 0
                else:
                    if j in self.primes:
                        for k in range(10):
                            if k % 2 == 0:
                                f[i][j] += f[i - 1][k]
                    else:
                        f[i][j] = 0

        res = 0
        for j in range(10):
            res += f[n - 1][j]

        return res % mod

# @lc code=end

