#
# @lc app=leetcode id=72 lang=python3
#
# [72] Edit Distance
#
# https://leetcode.com/problems/edit-distance/description/
#
# algorithms
# Hard (46.50%)
# Likes:    5362
# Dislikes: 66
# Total Accepted:    343.8K
# Total Submissions: 731.8K
# Testcase Example:  '"horse"\n"ros"'
#
# Given two strings word1 and word2, return the minimum number of operations
# required to convert word1 to word2.
# 
# You have the following three operations permitted on a word:
# 
# 
# Insert a character
# Delete a character
# Replace a character
# 
# 
# 
# Example 1:
# 
# 
# Input: word1 = "horse", word2 = "ros"
# Output: 3
# Explanation: 
# horse -> rorse (replace 'h' with 'r')
# rorse -> rose (remove 'r')
# rose -> ros (remove 'e')
# 
# 
# Example 2:
# 
# 
# Input: word1 = "intention", word2 = "execution"
# Output: 5
# Explanation: 
# intention -> inention (remove 't')
# inention -> enention (replace 'i' with 'e')
# enention -> exention (replace 'n' with 'x')
# exention -> exection (replace 'n' with 'c')
# exection -> execution (insert 'u')
# 
# 
# 
# Constraints:
# 
# 
# 0 <= word1.length, word2.length <= 500
# word1 and word2 consist of lowercase English letters.
# 
# 
#

# @lc code=start
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if not word1 or len(word1) == 0:
            return len(word2)

        if not word2 or len(word2) == 0:
            return len(word1)

        l1, l2 = len(word1), len(word2)
        word1 = "#" + word1
        word2 = "#" + word2

        # dp initialization
        # f[i][j] represents the minimum number of operations required to convert word1[:i] to word2[:j]
        f = [[l1 + l2 + 1 for _ in range(l2 + 1)] for _ in range(l1 + 1)]

        # word1[:i] and ""
        for i in range(l1 + 1):
            f[i][0] = i

        # word2[:j] and ""
        for j in range(l2 + 1):
            f[0][j] = j

        for i in range(1, l1 + 1):
            for j in range(1, l2 + 1):
                if word1[i] == word2[j]:
                    # no need to edit
                    f[i][j] = f[i - 1][j - 1]
                else:
                    f[i][j] = min(

                        # edit_distance of word1[i - 1] and word2[j - 1]
                        # replace word1[i] or replace word2[j] with another
                        f[i - 1][j - 1] + 1,
                        
                        # edit_distance of word1[i] and word2[j - 1]
                        # remove word2[j]
                        f[i][j - 1] + 1,
                        
                        # edit_distance of word1[i - 1] and word2[j]
                        # and `add` character word1[i] to word2[j + 1]
                        f[i - 1][j] + 1
                    )

        return f[l1][l2]
# @lc code=end

