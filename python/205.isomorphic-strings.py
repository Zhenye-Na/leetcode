#
# @lc app=leetcode id=205 lang=python3
#
# [205] Isomorphic Strings
#
# https://leetcode.com/problems/isomorphic-strings/description/
#
# algorithms
# Easy (40.89%)
# Likes:    2445
# Dislikes: 520
# Total Accepted:    402.9K
# Total Submissions: 974.8K
# Testcase Example:  '"egg"\n"add"'
#
# Given two strings s and t, determine if they are isomorphic.
# 
# Two strings s and t are isomorphic if the characters in s can be replaced to
# get t.
# 
# All occurrences of a character must be replaced with another character while
# preserving the order of characters. No two characters may map to the same
# character, but a character may map to itself.
# 
# 
# Example 1:
# Input: s = "egg", t = "add"
# Output: true
# Example 2:
# Input: s = "foo", t = "bar"
# Output: false
# Example 3:
# Input: s = "paper", t = "title"
# Output: true
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 5 * 10^4
# t.length == s.length
# s and t consist of any valid ascii character.
# 
# 
#

# @lc code=start
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if not s or not t or len(s) == 0 or len(t) == 0 or len(s) != len(t):
            return False
        
        s2t, t2s = {}, {}
        n = len(s)
        
        for i in range(n):
            if s[i] not in s2t:
                if t[i] in t2s and t2s[t[i]] != s[i]:
                    return False
                s2t[s[i]] = t[i]
                t2s[t[i]] = s[i]
            else:
                # mapping contains s[i]
                if t[i] != s2t[s[i]]:
                    return False

        return True
# @lc code=end

