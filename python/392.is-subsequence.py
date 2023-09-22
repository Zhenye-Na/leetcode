#
# @lc app=leetcode id=392 lang=python3
#
# [392] Is Subsequence
#
# https://leetcode.com/problems/is-subsequence/description/
#
# algorithms
# Easy (49.76%)
# Likes:    2692
# Dislikes: 246
# Total Accepted:    312.6K
# Total Submissions: 627.9K
# Testcase Example:  '"abc"\n"ahbgdc"'
#
# Given two strings s and t, return true if s is a subsequence of t, or false
# otherwise.
# 
# A subsequence of a string is a new string that is formed from the original
# string by deleting some (can be none) of the characters without disturbing
# the relative positions of the remaining characters. (i.e., "ace" is a
# subsequence of "abcde" while "aec" is not).
# 
# 
# Example 1:
# Input: s = "abc", t = "ahbgdc"
# Output: true
# Example 2:
# Input: s = "axc", t = "ahbgdc"
# Output: false
# 
# 
# Constraints:
# 
# 
# 0 <= s.length <= 100
# 0 <= t.length <= 10^4
# s and t consist only of lowercase English letters.
# 
# 
# 
# Follow up: Suppose there are lots of incoming s, say s1, s2, ..., sk where k
# >= 10^9, and you want to check one by one to see if t has its subsequence. In
# this scenario, how would you change your code?
#

# @lc code=start
class Solution_TwoPointers:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s or len(s) == 0:
            return True

        s_, t_ = 0, 0

        while t_ < len(t):
            if t[t_] == s[s_]:
                s_ += 1

            if s_ == len(s):
                return True

            t_ += 1

        return False


class Solution_TwoPointers:
    def isSubsequence(self, s: str, t: str) -> bool:

        sp = 0
        for tp in range(len(t)):
            if sp < len(s) and t[tp] == s[sp]:
                sp += 1

            if sp >= len(s):
                break

        if sp < len(s):
            return False
        return True


class Solution_DP:
    def isSubsequence(self, s: str, t: str) -> bool:
        s = "#" + s
        t = "#" + t

        # state[i][j] = True represents that s[:i] is a subsequenceof t[:j]
        ls, lt = len(s), len(t)
        state = [[False for _ in range(lt)] for _ in range(ls)]
        state[0][0] = True

        for j in range(1, lt):
            state[0][j] = True

        for i in range(1, ls):
            for j in range(1, lt):
                if s[i] == t[j] and state[i - 1][j - 1]:
                    state[i][j] = True
                else:
                    state[i][j] = state[i][j - 1]

        return state[-1][-1]
# @lc code=end

