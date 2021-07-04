#
# @lc app=leetcode id=1220 lang=python3
#
# [1220] Count Vowels Permutation
#
# https://leetcode.com/problems/count-vowels-permutation/description/
#
# algorithms
# Hard (54.24%)
# Likes:    593
# Dislikes: 76
# Total Accepted:    30.2K
# Total Submissions: 52.8K
# Testcase Example:  '1'
#
# Given an integer n, your task is to count how many strings of length n can be
# formed under the following rules:
# 
# 
# Each character is a lower case vowel ('a', 'e', 'i', 'o', 'u')
# Each vowel 'a' may only be followed by an 'e'.
# Each vowel 'e' may only be followed by an 'a' or an 'i'.
# Each vowel 'i' may not be followed by another 'i'.
# Each vowel 'o' may only be followed by an 'i' or a 'u'.
# Each vowel 'u' may only be followed by an 'a'.
# 
# 
# Since the answer may be too large, return it modulo 10^9 + 7.
# 
# 
# Example 1:
# 
# 
# Input: n = 1
# Output: 5
# Explanation: All possible strings are: "a", "e", "i" , "o" and "u".
# 
# 
# Example 2:
# 
# 
# Input: n = 2
# Output: 10
# Explanation: All possible strings are: "ae", "ea", "ei", "ia", "ie", "io",
# "iu", "oi", "ou" and "ua".
# 
# 
# Example 3: 
# 
# 
# Input: n = 5
# Output: 68
# 
# 
# Constraints:
# 
# 
# 1 <= n <= 2 * 10^4
# 
# 
#

# @lc code=start
class Solution:
    def countVowelPermutation(self, n: int) -> int:
        if not n or n == 0:
            return 0

        # dp initializtion
        # f[i][j] represents a i-length string ending with vowel[j]
        f = [[0 for _ in range(5)] for _ in range(n)]

        for j in range(5):
            f[0][j] = 1

        for i in range(1, n):
            for j in range(5):
                f[i][0] = f[i - 1][1] + f[i - 1][2] + f[i - 1][4]
                f[i][1] = f[i - 1][0] + f[i - 1][2]
                f[i][2] = f[i - 1][1] + f[i - 1][3]
                f[i][3] = f[i - 1][2]
                f[i][4] = f[i - 1][2] + f[i - 1][3]

        res = sum(f[-1])
        return res % (10 ** 9 + 7)
# @lc code=end

