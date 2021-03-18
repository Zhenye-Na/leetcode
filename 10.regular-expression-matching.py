#
# @lc app=leetcode id=10 lang=python3
#
# [10] Regular Expression Matching
#
# https://leetcode.com/problems/regular-expression-matching/description/
#
# algorithms
# Hard (27.26%)
# Likes:    5443
# Dislikes: 831
# Total Accepted:    516.4K
# Total Submissions: 1.9M
# Testcase Example:  '"aa"\n"a"'
#
# Given an input string (s) and a pattern (p), implement regular expression
# matching with support for '.' and '*' where: 
# 
# 
# '.' Matches any single character.​​​​
# '*' Matches zero or more of the preceding element.
# 
# 
# The matching should cover the entire input string (not partial).
# 
# 
# Example 1:
# 
# 
# Input: s = "aa", p = "a"
# Output: false
# Explanation: "a" does not match the entire string "aa".
# 
# 
# Example 2:
# 
# 
# Input: s = "aa", p = "a*"
# Output: true
# Explanation: '*' means zero or more of the preceding element, 'a'. Therefore,
# by repeating 'a' once, it becomes "aa".
# 
# 
# Example 3:
# 
# 
# Input: s = "ab", p = ".*"
# Output: true
# Explanation: ".*" means "zero or more (*) of any character (.)".
# 
# 
# Example 4:
# 
# 
# Input: s = "aab", p = "c*a*b"
# Output: true
# Explanation: c can be repeated 0 times, a can be repeated 1 time. Therefore,
# it matches "aab".
# 
# 
# Example 5:
# 
# 
# Input: s = "mississippi", p = "mis*is*p*."
# Output: false
# 
# 
# 
# Constraints:
# 
# 
# 0 <= s.length <= 20
# 0 <= p.length <= 30
# s contains only lowercase English letters.
# p contains only lowercase English letters, '.', and '*'.
# It is guaranteed for each appearance of the character '*', there will be a
# previous valid character to match.
# 
# 
#

# @lc code=start
class Solution:

    def __init__(self):
        self.mem = {}

    def isMatch(self, s: str, p: str) -> bool:
        self.s, self.p = s, p
        return self._dfs(0, 0)


    def _dfs(self, i, j):
        if (i, j) in self.mem:
            return self.mem[(i, j)]

        if i >= len(self.s) and j >= len(self.p):
            self.mem[(i, j)] = True
            return self.mem[(i, j)]

        if j >= len(self.p):
            self.mem[(i, j)] = False
            return self.mem[(i, j)]

        # whether match for current position
        match = (i < len(self.s) and (self.s[i] == self.p[j] or self.p[j] == '.'))

        if j + 1 < len(self.p) and self.p[j + 1] == '*':
            # we have a * here, which divide the dfs to two parts
            #                       if match and we use *      ||   we do not use * -> '' empty string
            self.mem[(i, j)] = (match and self._dfs(i + 1, j)) or self._dfs(i, j + 2)
            return self.mem[(i, j)]

        if match:
            self.mem[(i, j)] = self._dfs(i + 1, j + 1)
            return self._dfs(i + 1, j + 1)


        self.mem[(i, j)] = False
        return self.mem[(i, j)]
# @lc code=end

