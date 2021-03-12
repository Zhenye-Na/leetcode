#
# @lc app=leetcode id=131 lang=python3
#
# [131] Palindrome Partitioning
#
# https://leetcode.com/problems/palindrome-partitioning/description/
#
# algorithms
# Medium (51.53%)
# Likes:    3120
# Dislikes: 99
# Total Accepted:    299.8K
# Total Submissions: 574.2K
# Testcase Example:  '"aab"'
#
# Given a string s, partition s such that every substring of the partition is a
# palindrome. Return all possible palindrome partitioning of s.
# 
# A palindrome string is a string that reads the same backward as forward.
# 
# 
# Example 1:
# Input: s = "aab"
# Output: [["a","a","b"],["aa","b"]]
# Example 2:
# Input: s = "a"
# Output: [["a"]]
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 16
# s contains only lowercase English letters.
# 
# 
#

# @lc code=start
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        if not s or len(s) == 0:
            return []

        res = []
        self.palindromes = set([])
        self._dfs(s, res, [], 0)

        return res


    def _dfs(self, s, res, curr, start):
        if start == len(s):
            res.append(curr[:])
            return

        for i in range(start, len(s)):
            if not self.is_palindromes(s[start:i + 1]):
                continue

            curr.append(s[start:i + 1])
            self._dfs(s, res, curr, i + 1)
            curr.pop()


    def is_palindromes(self, s):
        if s in self.palindromes:
            return True

        if s == s[::-1]:
            self.palindromes.add(s)
            return True
        return False


# @lc code=end

