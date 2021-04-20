#
# @lc app=leetcode id=1092 lang=python3
#
# [1092] Shortest Common Supersequence 
#
# https://leetcode.com/problems/shortest-common-supersequence/description/
#
# algorithms
# Hard (52.85%)
# Likes:    887
# Dislikes: 24
# Total Accepted:    21.2K
# Total Submissions: 39.9K
# Testcase Example:  '"abac"\n"cab"'
#
# Given two strings str1 and str2, return the shortest string that has both
# str1 and str2 as subsequences.  If multiple answers exist, you may return any
# of them.
# 
# (A string S is a subsequence of string T if deleting some number of
# characters from T (possibly 0, and the characters are chosen anywhere from T)
# results in the string S.)
# 
# 
# 
# Example 1:
# 
# 
# Input: str1 = "abac", str2 = "cab"
# Output: "cabac"
# Explanation: 
# str1 = "abac" is a subsequence of "cabac" because we can delete the first
# "c".
# str2 = "cab" is a subsequence of "cabac" because we can delete the last "ac".
# The answer provided is the shortest such string that satisfies these
# properties.
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= str1.length, str2.length <= 1000
# str1 and str2 consist of lowercase English letters.
# 
# 
#

# @lc code=start

class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        if not str1 or not str2 or len(str1) == 0 or len(str2) == 0:
            return ""

        # dp initialization
        # f[i][j] represents the SCS of str1[:i] and str2[:j]
        l1, l2 = len(str1), len(str2)
        str1 = "#" + str1
        str2 = "#" + str2
        f = [[0 for _ in range(l2 + 1)] for _ in range(l1 + 1)]

        for i in range(1, l1 +1):
            f[i][0] = i

        for j in range(1, l2 +1):
            f[0][j] = j

        for i in range(1, l1 + 1):
            for j in range(1, l2 + 1):
                if str1[i] == str2[j]:
                    f[i][j] = f[i - 1][j - 1] + 1
                else:
                    f[i][j] = min(
                        f[i][j - 1] + 1,
                        f[i - 1][j] + 1
                    )

        res = ""
        i, j = l1, l2
        while i > 0 and j > 0:
            if str1[i] == str2[j]:
                res += str1[i]
                i -= 1
                j -= 1
            elif f[i][j] == f[i][j - 1] + 1:
                res += str2[j]
                j -= 1
            elif f[i][j] == f[i - 1][j] + 1:
                res += str1[i]
                i -= 1

        while i > 0:
            res += str1[i]
            i -= 1

        while j > 0:
            res += str2[j]
            j -= 1

        return res[::-1]
# @lc code=end

