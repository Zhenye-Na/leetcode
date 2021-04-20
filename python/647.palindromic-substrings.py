#
# @lc app=leetcode id=647 lang=python3
#
# [647] Palindromic Substrings
#
class Solution:
    def countSubstrings(self, s: str) -> int:
        # state: f[j][i] represents s[j:i + 1] is Palindrom or not.
        f = [[0 for _ in range(len(s))] for _ in range(len(s))]

        res = 0
        for i in range(len(s)):
            for j in range(i + 1):
                if s[j] == s[i] and (i - j <= 2 or f[j + 1][i - 1] == 1):
                    f[j][i] = 1
                res += f[j][i]

        return res

