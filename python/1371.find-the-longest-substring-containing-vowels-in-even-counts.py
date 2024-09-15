#
# @lc app=leetcode id=1371 lang=python3
#
# [1371] Find the Longest Substring Containing Vowels in Even Counts
#
# https://leetcode.com/problems/find-the-longest-substring-containing-vowels-in-even-counts/description/
#
# algorithms
# Medium (63.54%)
# Likes:    1810
# Dislikes: 70
# Total Accepted:    45.1K
# Total Submissions: 65.1K
# Testcase Example:  '"eleetminicoworoep"'
#
# Given the string s, return the size of the longest substring containing each
# vowel an even number of times. That is, 'a', 'e', 'i', 'o', and 'u' must
# appear an even number of times.
#
#
# Example 1:
#
#
# Input: s = "eleetminicoworoep"
# Output: 13
# Explanation: The longest substring is "leetminicowor" which contains two each
# of the vowels: e, i and o and zero of the vowels: a and u.
#
#
# Example 2:
#
#
# Input: s = "leetcodeisgreat"
# Output: 5
# Explanation: The longest substring is "leetc" which contains two e's.
#
#
# Example 3:
#
#
# Input: s = "bcbcbc"
# Output: 6
# Explanation: In this case, the given string "bcbcbc" is the longest because
# all vowels: a, e, i, o and u appear zero times.
#
#
#
# Constraints:
#
#
# 1 <= s.length <= 5 x 10^5
# s contains only lowercase English letters.
#
#
#


# @lc code=start
class Solution:

    def __init__(self):
        self.mapping = {"a": 1, "e": 2, "i": 4, "o": 8, "u": 16}

    def findTheLongestSubstring(self, s: str) -> int:
        max_len = 0
        if not s or len(s) == 0:
            return max_len

        prefix_xor = 0
        seen = {0: -1}

        for j, char in enumerate(s):
            if char in self.mapping:
                prefix_xor ^= self.mapping[char]

            if prefix_xor in seen:
                i = seen[prefix_xor]
                max_len = max(max_len, j - i)
            else:
                seen[prefix_xor] = j

        return max_len


# @lc code=end
