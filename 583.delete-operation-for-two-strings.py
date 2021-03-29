#
# @lc app=leetcode id=583 lang=python3
#
# [583] Delete Operation for Two Strings
#
# https://leetcode.com/problems/delete-operation-for-two-strings/description/
#
# algorithms
# Medium (49.83%)
# Likes:    1443
# Dislikes: 34
# Total Accepted:    62.5K
# Total Submissions: 124.4K
# Testcase Example:  '"sea"\n"eat"'
#
# Given two strings word1 and word2, return the minimum number of steps
# required to make word1 and word2 the same.
# 
# In one step, you can delete exactly one character in either string.
# 
# 
# Example 1:
# 
# 
# Input: word1 = "sea", word2 = "eat"
# Output: 2
# Explanation: You need one step to make "sea" to "ea" and another step to make
# "eat" to "ea".
# 
# 
# Example 2:
# 
# 
# Input: word1 = "leetcode", word2 = "etco"
# Output: 4
# 
# 
# 
# Constraints:
# 
# 
# 1 <= word1.length, word2.length <= 500
# word1 and word2 consist of only lowercase English letters.
# 
# 
#

# @lc code=start
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if not word1 or len(word1) == 0:
            return len(word2) if word2 else 0

        if not word2 or len(word2) == 0:
            return len(word1) if word1 else 0


        l1, l2 = len(word1), len(word2)
        word1 = "#" + word1
        word2 = "#" + word2

        # dp initialization
        # f[i][j] represents the longest common subsequence of
        # word1[:i] and word2[:j]
        f = [[0 for _ in range(l2 + 1)] for _ in range(l1 + 1)]

        for i in range(1, l1 + 1):
            for j in range(1, l2 + 1):
                if word1[i] == word2[j]:
                    f[i][j] = f[i - 1][j - 1] + 1
                else:
                    f[i][j] = max(
                        f[i - 1][j - 1],
                        f[i - 1][j],
                        f[i][j - 1]
                    )

        lcs = f[l1][l2]
        return l1 + l2 - 2 * lcs
# @lc code=end

