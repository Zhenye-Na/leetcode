#
# @lc app=leetcode id=880 lang=python3
#
# [880] Decoded String at Index
#
# https://leetcode.com/problems/decoded-string-at-index/description/
#
# algorithms
# Medium (28.19%)
# Likes:    1619
# Dislikes: 241
# Total Accepted:    47.3K
# Total Submissions: 154.3K
# Testcase Example:  '"leet2code3"\n10'
#
# You are given an encoded string s. To decode the string to a tape, the
# encoded string is read one character at a time and the following steps are
# taken:
# 
# 
# If the character read is a letter, that letter is written onto the tape.
# If the character read is a digit d, the entire current tape is repeatedly
# written d - 1 more times in total.
# 
# 
# Given an integer k, return the k^th letter (1-indexed) in the decoded
# string.
# 
# 
# Example 1:
# 
# 
# Input: s = "leet2code3", k = 10
# Output: "o"
# Explanation: The decoded string is "leetleetcodeleetleetcodeleetleetcode".
# The 10^th letter in the string is "o".
# 
# 
# Example 2:
# 
# 
# Input: s = "ha22", k = 5
# Output: "h"
# Explanation: The decoded string is "hahahaha".
# The 5^th letter is "h".
# 
# 
# Example 3:
# 
# 
# Input: s = "a2345678999999999999999", k = 1
# Output: "a"
# Explanation: The decoded string is "a" repeated 8301530446056247680 times.
# The 1^st letter is "a".
# 
# 
# 
# Constraints:
# 
# 
# 2 <= s.length <= 100
# s consists of lowercase English letters and digits 2 through 9.
# s starts with a letter.
# 1 <= k <= 10^9
# It is guaranteed that k is less than or equal to the length of the decoded
# string.
# The decoded string is guaranteed to have less than 2^63 letters.
# 
# 
#

# @lc code=start
class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:

        stack = []
        total_len = 0

        for char in s:
            if char.isdigit():
                total_len *= int(char)
            else:
                total_len += 1
            stack.append(char)

        while stack:
            char = stack.pop()
            if char.isdigit():
                total_len //= int(char)
                k %= total_len
            else:
                if k == 0 or k == total_len:
                    return char
                total_len -= 1

        return ""
# @lc code=end

