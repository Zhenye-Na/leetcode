#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#
# https://leetcode.com/problems/longest-palindromic-substring/description/
#
# algorithms
# Medium (28.07%)
# Likes:    4553
# Dislikes: 412
# Total Accepted:    684.5K
# Total Submissions: 2.4M
# Testcase Example:  '"babad"'
#
# Given a string s, find the longest palindromic substring in s. You may assume
# that the maximum length of s is 1000.
# 
# Example 1:
# 
# 
# Input: "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.
# 
# 
# Example 2:
# 
# 
# Input: "cbbd"
# Output: "bb"
# 
# 
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        start, end, max_len = 0, 0, 0
        for i in range(len(s)):
            len1 = self._find_palindrome(s, i, i) # racecar
            len2 = self._find_palindrome(s, i, i + 1) # abba
            curr_max = max(len1, len2)

            if curr_max > max_len:
                start = i - (curr_max - 1) // 2
                end = i + curr_max // 2
                max_len = curr_max

        return s[start:end + 1]


    def _find_palindrome(self, s, left, right):
        if not s or len(s) < 1 or left > right:
            return 0

        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        
        return right - 1 - (left + 1) + 1


class Solution_DP:
    def longestPalindrome(self, s: str) -> str:
        dp = [[False] * len(s) for _ in range(len(s))]
        longest = ''

        for i in range(len(s)):
            for j in range(i + 1):
                if s[i] == s[j] and ((i + 1 - j) <= 3 or dp[i - 1][j + 1]):
                    dp[i][j] = True
                    if i + 1 - j > len(longest):
                        longest = s[j:i + 1]
        return longest
# @lc code=end

