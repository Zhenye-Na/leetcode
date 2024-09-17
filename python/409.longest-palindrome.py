#
# @lc app=leetcode id=409 lang=python3
#
# [409] Longest Palindrome
#
# https://leetcode.com/problems/longest-palindrome/description/
#
# algorithms
# Easy (53.91%)
# Likes:    5944
# Dislikes: 413
# Total Accepted:    823.4K
# Total Submissions: 1.5M
# Testcase Example:  '"abccccdd"'
#
# Given a string s which consists of lowercase or uppercase letters, return the
# length of the longest palindrome that can be built with those letters.
#
# Letters are case sensitive, for example, "Aa" is not considered a
# palindrome.
#
#
# Example 1:
#
#
# Input: s = "abccccdd"
# Output: 7
# Explanation: One longest palindrome that can be built is "dccaccd", whose
# length is 7.
#
#
# Example 2:
#
#
# Input: s = "a"
# Output: 1
# Explanation: The longest palindrome that can be built is "a", whose length is
# 1.
#
#
#
# Constraints:
#
#
# 1 <= s.length <= 2000
# s consists of lowercase and/or uppercase English letters only.
#
#
#

# @lc code=start
from collections import Counter


class Solution:
    def longestPalindrome(self, s: str) -> int:
        counter = Counter(s)
        res = 0
        mid = False
        for char in counter:
            if counter[char] % 2 == 0:
                res += counter[char]
            else:
                if not mid:
                    res += counter[char]
                    mid = True
                else:
                    res += counter[char] - 1

        return res


# @lc code=end
