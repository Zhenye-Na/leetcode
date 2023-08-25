#
# @lc app=leetcode id=97 lang=python3
#
# [97] Interleaving String
#
# https://leetcode.com/problems/interleaving-string/description/
#
# algorithms
# Hard (32.44%)
# Likes:    1923
# Dislikes: 105
# Total Accepted:    177.4K
# Total Submissions: 542.6K
# Testcase Example:  '"aabcc"\n"dbbca"\n"aadbbcbcac"'
#
# Given strings s1, s2, and s3, find whether s3 is formed by an interleaving of
# s1 and s2.
# 
# An interleaving of two strings s and t is a configuration where they are
# divided into non-empty substrings such that:
# 
# 
# s = s1 + s2 + ... + sn
# t = t1 + t2 + ... + tm
# |n - m| <= 1
# The interleaving is s1 + t1 + s2 + t2 + s3 + t3 + ... or t1 + s1 + t2 + s2 +
# t3 + s3 + ...
# 
# 
# Note: a + b is the concatenation of strings a and b.
# 
# 
# Example 1:
# 
# 
# Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
# Output: true
# 
# 
# Example 2:
# 
# 
# Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
# Output: false
# 
# 
# Example 3:
# 
# 
# Input: s1 = "", s2 = "", s3 = ""
# Output: true
# 
# 
# 
# Constraints:
# 
# 
# 0 <= s1.length, s2.length <= 100
# 0 <= s3.length <= 200
# s1, s2, and s3 consist of lowercase English letters.
# 
# 
# 
# Follow up: Could you solve it using only O(s2.length) additional memory
# space?
# 
#

# @lc code=start
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # if not s1 or len(s1) == 0 or not s2 or len(s2) == 0:
        #     return not s3 or len(s3) == 0

        # if len(s1) + len(s2) != len(s3):
        #     return False

        l1, l2 = len(s1), len(s2)
        s1 = "#" + s1
        s2 = "#" + s2
        s3 = "#" + s3

        # dp initialization
        # f[i][j] represents:
        # s1[:i] and s2[:j] can form an interleaving string -> s3[:i + j]
        f = [[False for _ in range(l2 + 1)] for _ in range(l1 + 1)]
        for i in range(l1 + 1):
            if s1[i] == s3[i]:
                f[i][0] = True

        for j in range(l2 + 1):
            if s2[j] == s3[j]:
                f[0][j] = True

        for i in range(1, l1 + 1):
            for j in range(1, l2 + 1):
                if s1[i] == s3[i + j] and f[i - 1][j]:
                    f[i][j] = True
                if s2[j] == s3[i + j] and f[i][j - 1]:
                    f[i][j] = True

        return f[l1][l2]


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False

        l1, l2 = len(s1) + 1, len(s2) + 1
        f = [[False for _ in range(l2)] for _ in range(l1)]

        f[0][0] = True

        for i in range(1, l1):
            f[i][0] = s1[:i] == s3[:i]


        for j in range(1, l2):
            f[0][j] = s2[:j] == s3[:j]


        for i in range(1, l1):
            for j in range(1, l2):

                if f[i - 1][j]:
                    if s1[i - 1] == s3[i + j - 1]:
                        f[i][j] = True
                
                if f[i][j - 1]:
                    if s2[j - 1] == s3[i + j - 1]:
                        f[i][j] = True

        return f[-1][-1]
# @lc code=end

