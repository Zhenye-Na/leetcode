#
# @lc app=leetcode id=709 lang=python3
#
# [709] To Lower Case
#
# https://leetcode.com/problems/to-lower-case/description/
#
# algorithms
# Easy (79.98%)
# Likes:    739
# Dislikes: 1972
# Total Accepted:    282.5K
# Total Submissions: 350.6K
# Testcase Example:  '"Hello"'
#
# Given a string s, return the string after replacing every uppercase letter
# with the same lowercase letter.
# 
# 
# Example 1:
# 
# 
# Input: s = "Hello"
# Output: "hello"
# 
# 
# Example 2:
# 
# 
# Input: s = "here"
# Output: "here"
# 
# 
# Example 3:
# 
# 
# Input: s = "LOVELY"
# Output: "lovely"
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 100
# s consists of printable ASCII characters.
# 
# 
#

# @lc code=start
class Solution:
    def toLowerCase(self, s: str) -> str:
        res = ""
        for i in range(len(s)):
            if 65 <= ord(s[i]) <= 90:
                res += chr(ord(s[i]) + 32)
            else:
                res += s[i]
        return res
# @lc code=end

