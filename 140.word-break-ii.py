#
# @lc app=leetcode id=140 lang=python3
#
# [140] Word Break II
#
# https://leetcode.com/problems/word-break-ii/description/
#
# algorithms
# Hard (34.37%)
# Likes:    2992
# Dislikes: 444
# Total Accepted:    311.3K
# Total Submissions: 888.4K
# Testcase Example:  '"catsanddog"\n["cat","cats","and","sand","dog"]'
#
# Given a string s and a dictionary of strings wordDict, add spaces in s to
# construct a sentence where each word is a valid dictionary word. Return all
# such possible sentences in any order.
# 
# Note that the same word in the dictionary may be reused multiple times in the
# segmentation.
# 
# 
# Example 1:
# 
# 
# Input: s = "catsanddog", wordDict = ["cat","cats","and","sand","dog"]
# Output: ["cats and dog","cat sand dog"]
# 
# 
# Example 2:
# 
# 
# Input: s = "pineapplepenapple", wordDict =
# ["apple","pen","applepen","pine","pineapple"]
# Output: ["pine apple pen apple","pineapple pen apple","pine applepen apple"]
# Explanation: Note that you are allowed to reuse a dictionary word.
# 
# 
# Example 3:
# 
# 
# Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
# Output: []
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 20
# 1 <= wordDict.length <= 1000
# 1 <= wordDict[i].length <= 10
# s and wordDict[i] consist of only lowercase English letters.
# All the strings of wordDict are unique.
# 
# 
#

# @lc code=start
class Solution:

    def __init__(self):
        self.memo = {}

    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        return self._dfs(s, wordDict)


    def _dfs(self, s, word_dict):
        if s in self.memo:
            return self.memo[s]
        
        if not s or len(s) == 0:
            return []

        partitions = []
        if s in word_dict:
            partitions.append(s)

        for i in range(0, len(s)):
            prefix = s[:i]
            if prefix not in word_dict:
                continue

            suffix = self._dfs(s[i:], word_dict)
            for suf in suffix:
                partitions.append(prefix + " " + suf)

        self.memo[s] = partitions

        return partitions
# @lc code=end

