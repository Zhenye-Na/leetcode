#
# @lc app=leetcode id=115 lang=python3
#
# [115] Distinct Subsequences
#
# https://leetcode.com/problems/distinct-subsequences/description/
#
# algorithms
# Hard (39.50%)
# Likes:    1838
# Dislikes: 63
# Total Accepted:    159.9K
# Total Submissions: 400.6K
# Testcase Example:  '"rabbbit"\n"rabbit"'
#
# Given two strings s and t, return the number of distinct subsequences of s
# which equals t.
# 
# A string's subsequence is a new string formed from the original string by
# deleting some (can be none) of the characters without disturbing the
# remaining characters' relative positions. (i.e., "ACE" is a subsequence of
# "ABCDE" while "AEC" is not).
# 
# It is guaranteed the answer fits on a 32-bit signed integer.
# 
# 
# Example 1:
# 
# 
# Input: s = "rabbbit", t = "rabbit"
# Output: 3
# Explanation:
# As shown below, there are 3 ways you can generate "rabbit" from S.
# rabbbit
# rabbbit
# rabbbit
# 
# 
# Example 2:
# 
# 
# Input: s = "babgbag", t = "bag"
# Output: 5
# Explanation:
# As shown below, there are 5 ways you can generate "bag" from S.
# babgbag
# babgbag
# babgbag
# babgbag
# babgbag
# 
# 
# Constraints:
# 
# 
# 1 <= s.length, t.length <= 1000
# s and t consist of English letters.
# 
# 
#

# @lc code=start
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        if not s or not t or len(s) == 0 or len(t) == 0:
            return 0

        l1, l2 = len(s), len(t)
        s = "#" + s
        t = "#" + t

        # dp initialization
        # f[i][j] represents the ways generating t[:j] from s[:i]
        f = [[0 for _ in range(l2 + 1)] for _ in range(l1 + 1)]

        for i in range(l1 + 1):
            f[i][0] = 1


        for i in range(1, l1 + 1):
            for j in range(1, l2 + 1):
                if s[i] == t[j]:
                    f[i][j] = f[i - 1][j] + f[i - 1][j - 1]
                else:
                    f[i][j] = f[i - 1][j] + 0

        return f[l1][l2]
# @lc code=end

