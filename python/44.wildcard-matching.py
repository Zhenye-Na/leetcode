#
# @lc app=leetcode id=44 lang=python3
#
# [44] Wildcard Matching
#
# https://leetcode.com/problems/wildcard-matching/description/
#
# algorithms
# Hard (25.32%)
# Likes:    2751
# Dislikes: 131
# Total Accepted:    289.9K
# Total Submissions: 1.1M
# Testcase Example:  '"aa"\n"a"'
#
# Given an input string (s) and a pattern (p), implement wildcard pattern
# matching with support for '?' and '*' where:
# 
# 
# '?' Matches any single character.
# '*' Matches any sequence of characters (including the empty sequence).
# 
# 
# The matching should cover the entire input string (not partial).
# 
# 
# Example 1:
# 
# 
# Input: s = "aa", p = "a"
# Output: false
# Explanation: "a" does not match the entire string "aa".
# 
# 
# Example 2:
# 
# 
# Input: s = "aa", p = "*"
# Output: true
# Explanation: '*' matches any sequence.
# 
# 
# Example 3:
# 
# 
# Input: s = "cb", p = "?a"
# Output: false
# Explanation: '?' matches 'c', but the second letter is 'a', which does not
# match 'b'.
# 
# 
# Example 4:
# 
# 
# Input: s = "adceb", p = "*a*b"
# Output: true
# Explanation: The first '*' matches the empty sequence, while the second '*'
# matches the substring "dce".
# 
# 
# Example 5:
# 
# 
# Input: s = "acdcb", p = "a*c?b"
# Output: false
# 
# 
# 
# Constraints:
# 
# 
# 0 <= s.length, p.length <= 2000
# s contains only lowercase English letters.
# p contains only lowercase English letters, '?' or '*'.
# 
# 
#

# @lc code=start
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        s = '#' + s
        p = '#' + p

        # dp[i][j] represents p[0:j] matches s[0:i]
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

        # initialization
        dp[0][0] = 1

        # is s is "", p must be all "*", "****s***" will be false after "s***"
        for i in range(1, n + 1):
            if p[i] != '*':
                break
            dp[0][i] = 1

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j] == '?':
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j] == '*':
                    dp[i][j] = dp[i][j - 1] or dp[i - 1][j]
                elif s[i] == p[j]:
                    dp[i][j] = dp[i - 1][j - 1]

        return dp[m][n] == 1
# @lc code=end

