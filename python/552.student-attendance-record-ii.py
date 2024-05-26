#
# @lc app=leetcode id=552 lang=python3
#
# [552] Student Attendance Record II
#
# https://leetcode.com/problems/student-attendance-record-ii/description/
#
# algorithms
# Hard (42.03%)
# Likes:    1837
# Dislikes: 252
# Total Accepted:    76.2K
# Total Submissions: 168.6K
# Testcase Example:  '2'
#
# An attendance record for a student can be represented as a string where each
# character signifies whether the student was absent, late, or present on that
# day. The record only contains the following three characters:
# 
# 
# 'A': Absent.
# 'L': Late.
# 'P': Present.
# 
# 
# Any student is eligible for an attendance award if they meet both of the
# following criteria:
# 
# 
# The student was absent ('A') for strictly fewer than 2 days total.
# The student was never late ('L') for 3 or more consecutive days.
# 
# 
# Given an integer n, return the number of possible attendance records of
# length n that make a student eligible for an attendance award. The answer may
# be very large, so return it modulo 10^9 + 7.
# 
# 
# Example 1:
# 
# 
# Input: n = 2
# Output: 8
# Explanation: There are 8 records with length 2 that are eligible for an
# award:
# "PP", "AP", "PA", "LP", "PL", "AL", "LA", "LL"
# Only "AA" is not eligible because there are 2 absences (there need to be
# fewer than 2).
# 
# 
# Example 2:
# 
# 
# Input: n = 1
# Output: 3
# 
# 
# Example 3:
# 
# 
# Input: n = 10101
# Output: 183236316
# 
# 
# 
# Constraints:
# 
# 
# 1 <= n <= 10^5
# 
# 
#

# @lc code=start
class Solution:
    def checkRecord(self, n: int) -> int:
class Solution:
    def checkRecord(self, n: int) -> int:
        MOD = 10 ** 9 + 7

        # dp[i][A][L] will be the number of valid sequences of length i
        # with A 'A's and ending with L consecutive 'L's.
        dp = [[[0] * 3 for _ in range(2)] for _ in range(n + 1)]

        # Base case: one valid sequence of length 0
        dp[0][0][0] = 1

        for i in range(1, n + 1):
            for A in range(2):
                for L in range(3):
                    # Append 'P' (doesn't change the count of 'A' or 'L')
                    dp[i][A][0] = (dp[i][A][0] + dp[i - 1][A][L]) % MOD

                    # Append 'A' (increases the count of 'A' by 1, resets 'L' count)
                    if A > 0:
                        dp[i][A][0] = (dp[i][A][0] + dp[i - 1][A - 1][L]) % MOD

                    # Append 'L' (increases the count of 'L' by 1, doesn't change 'A')
                    if L > 0:
                        dp[i][A][L] = (dp[i][A][L] + dp[i - 1][A][L - 1]) % MOD

        # Sum up all valid sequences of length n
        result = sum(dp[n][A][L] for A in range(2) for L in range(3)) % MOD

        return result

# @lc code=end

