#
# @lc app=leetcode id=926 lang=python3
#
# [926] Flip String to Monotone Increasing
#
# https://leetcode.com/problems/flip-string-to-monotone-increasing/description/
#
# algorithms
# Medium (53.92%)
# Likes:    1228
# Dislikes: 36
# Total Accepted:    51.8K
# Total Submissions: 91.8K
# Testcase Example:  '"00110"'
#
# A binary string is monotone increasing if it consists of some number of 0's
# (possibly none), followed by some number of 1's (also possibly none).
# 
# You are given a binary string s. You can flip s[i] changing it from 0 to 1 or
# from 1 to 0.
# 
# Return the minimum number of flips to make s monotone increasing.
# 
# 
# Example 1:
# 
# 
# Input: s = "00110"
# Output: 1
# Explanation: We flip the last digit to get 00111.
# 
# 
# Example 2:
# 
# 
# Input: s = "010110"
# Output: 2
# Explanation: We flip to get 011111, or alternatively 000111.
# 
# 
# Example 3:
# 
# 
# Input: s = "00011000"
# Output: 2
# Explanation: We flip to get 00000000.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 10^5
# s[i] is either '0' or '1'.
# 
# 
#

# @lc code=start
class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        n = len(s)
        n0 = s.count("0")
        n1 = 0

        res = n - n0
        for i in range(n):
            if s[i] == "0":
                n0 -= 1
            else:
                res = min(res, n0 + n1)
                n1 += 1

        return res
# @lc code=end

