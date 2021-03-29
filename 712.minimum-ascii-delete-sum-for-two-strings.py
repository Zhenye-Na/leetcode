#
# @lc app=leetcode id=712 lang=python3
#
# [712] Minimum ASCII Delete Sum for Two Strings
#
# https://leetcode.com/problems/minimum-ascii-delete-sum-for-two-strings/description/
#
# algorithms
# Medium (59.39%)
# Likes:    1275
# Dislikes: 54
# Total Accepted:    44.9K
# Total Submissions: 75.3K
# Testcase Example:  '"sea"\n"eat"'
#
# Given two strings s1, s2, find the lowest ASCII sum of deleted characters to
# make two strings equal.
# 
# Example 1:
# 
# Input: s1 = "sea", s2 = "eat"
# Output: 231
# Explanation: Deleting "s" from "sea" adds the ASCII value of "s" (115) to the
# sum.
# Deleting "t" from "eat" adds 116 to the sum.
# At the end, both strings are equal, and 115 + 116 = 231 is the minimum sum
# possible to achieve this.
# 
# 
# 
# Example 2:
# 
# Input: s1 = "delete", s2 = "leet"
# Output: 403
# Explanation: Deleting "dee" from "delete" to turn the string into "let",
# adds 100[d]+101[e]+101[e] to the sum.  Deleting "e" from "leet" adds 101[e]
# to the sum.
# At the end, both strings are equal to "let", and the answer is
# 100+101+101+101 = 403.
# If instead we turned both strings into "lee" or "eet", we would get answers
# of 433 or 417, which are higher.
# 
# 
# 
# Note:
# 0 < s1.length, s2.length .
# All elements of each string will have an ASCII value in [97, 122]. 
# 
#

# @lc code=start
class Solution:

    def __init__(self):
        self.lcs = set([])

    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        if not s1 or len(s1) == 0:
            return sum([ord(char) for char in s2]) if s2 else 0

        if not s2 or len(s2) == 0:
            return sum([ord(char) for char in s1]) if s1 else 0

        total_s1, total_s2 = sum([ord(char) for char in s1]), sum([ord(char) for char in s2])
        l1, l2 = len(s1), len(s2)

        s1 = "#" + s1
        s2 = "#" + s2

        # dp initialziation
        # f[i][j] represents LCS with largest ascii from s1[:i] and s2[:j]
        f = [[0 for _ in range(l2 + 1)] for _ in range(l1 + 1)] 

        for i in range(1, l1 + 1):
            for j in range(1, l2 + 1):
                if s1[i] == s2[j]:
                    f[i][j] = f[i - 1][j - 1] + ord(s1[i])
                else:
                    f[i][j] = max(
                        f[i - 1][j - 1],
                        f[i - 1][j],
                        f[i][j - 1]
                    )

        return total_s1 + total_s2 - 2 * f[l1][l2]


    def _get_all_lcs(self, f, s1, s2, l1, l2, curr):
        """
        This can be optimized by memoization
        """
        if l1 <= 0 or l2 <= 0:
            curr_lcs = curr[:][::-1]
            if curr_lcs not in self.lcs:
                self.lcs.add(curr_lcs)
            return

        if s1[l1] == s2[l2]:
            curr.append(s1[l1])
            self._get_lcs(f, s1, s2, l1 - 1, l2 - 1, curr)
            curr.pop()
        else:
            if f[l1 - 1][l2] > f[l1][l2 - 1]:
                self._get_lcs(f, s1, s2, l1 - 1, l2, curr)
            elif f[l1 - 1][l2] < f[l1][l2 - 1]:
                self._get_lcs(f, s1, s2, l1, l2 - 1, curr)
            else:
                self._get_lcs(f, s1, s2, l1 - 1, l2, curr)
                self._get_lcs(f, s1, s2, l1, l2 - 1, curr)
# @lc code=end

