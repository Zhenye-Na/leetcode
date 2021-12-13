#
# @lc app=leetcode id=1446 lang=python3
#
# [1446] Consecutive Characters
#
# https://leetcode.com/problems/consecutive-characters/description/
#
# algorithms
# Easy (61.14%)
# Likes:    870
# Dislikes: 19
# Total Accepted:    93K
# Total Submissions: 150.5K
# Testcase Example:  '"leetcode"'
#
# The power of the string is the maximum length of a non-empty substring that
# contains only one unique character.
# 
# Given a string s, return the power of s.
# 
# 
# Example 1:
# 
# 
# Input: s = "leetcode"
# Output: 2
# Explanation: The substring "ee" is of length 2 with the character 'e' only.
# 
# 
# Example 2:
# 
# 
# Input: s = "abbcccddddeeeeedcba"
# Output: 5
# Explanation: The substring "eeeee" is of length 5 with the character 'e'
# only.
# 
# 
# Example 3:
# 
# 
# Input: s = "triplepillooooow"
# Output: 5
# 
# 
# Example 4:
# 
# 
# Input: s = "hooraaaaaaaaaaay"
# Output: 11
# 
# 
# Example 5:
# 
# 
# Input: s = "tourist"
# Output: 1
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 500
# s consists of only lowercase English letters.
# 
# 
#

# @lc code=start
class Solution:
    def maxPower(self, s: str) -> int:
        if not s or len(s) == 0:
            return 0

        max_len, curr_len = 1, 1
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                curr_len += 1
                max_len = max(max_len, curr_len)
            else:
                curr_len = 1

        return max_len


    def maxPower_solution2(self, s: str) -> int:
        if not s or len(s) == 0:
            return 0

        max_len = 1
        left, right = 0, 0
        while right < len(s):
            while right < len(s) and s[right] == s[left]:
                right += 1

            if right <= len(s) and s[right - 1] == s[left] and left != right:
                max_len = max(right - left, max_len)
            left = right
            right += 1

        return max_len
# @lc code=end

