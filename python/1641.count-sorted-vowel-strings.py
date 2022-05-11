#
# @lc app=leetcode id=1641 lang=python3
#
# [1641] Count Sorted Vowel Strings
#
# https://leetcode.com/problems/count-sorted-vowel-strings/description/
#
# algorithms
# Medium (75.00%)
# Likes:    2138
# Dislikes: 52
# Total Accepted:    99.7K
# Total Submissions: 130.9K
# Testcase Example:  '1'
#
# Given an integer n, return the number of strings of length n that consist
# only of vowels (a, e, i, o, u) and are lexicographically sorted.
# 
# A string s is lexicographically sorted if for all valid i, s[i] is the same
# as or comes before s[i+1] in the alphabet.
# 
# 
# Example 1:
# 
# 
# Input: n = 1
# Output: 5
# Explanation: The 5 sorted strings that consist of vowels only are
# ["a","e","i","o","u"].
# 
# 
# Example 2:
# 
# 
# Input: n = 2
# Output: 15
# Explanation: The 15 sorted strings that consist of vowels only are
# ["aa","ae","ai","ao","au","ee","ei","eo","eu","ii","io","iu","oo","ou","uu"].
# Note that "ea" is not a valid string since 'e' comes after 'a' in the
# alphabet.
# 
# 
# Example 3:
# 
# 
# Input: n = 33
# Output: 66045
# 
# 
# 
# Constraints:
# 
# 
# 1 <= n <= 50 
# 
# 
#

# @lc code=start
class Solution:
    def countVowelStrings(self, n: int) -> int:
        # f[i][j] represents the number of strings, end with jth vowel
        # with length == i
        f = [[0 for _ in range(6)] for _ in range(n + 1)]
        for j in range(1, 6):
            f[1][j] = 1
            
        for i in range(2, len(f)):
            for j in range(1, 6):
                f[i][j] = f[i][j - 1] + max(f[i - 1][j], 1)

        return sum(f[-1])
# @lc code=end

