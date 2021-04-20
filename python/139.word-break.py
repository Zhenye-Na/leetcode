#
# @lc app=leetcode id=139 lang=python3
#
# [139] Word Break
#
# https://leetcode.com/problems/word-break/description/
#
# algorithms
# Medium (41.49%)
# Likes:    6240
# Dislikes: 293
# Total Accepted:    728.8K
# Total Submissions: 1.7M
# Testcase Example:  '"leetcode"\n["leet","code"]'
#
# Given a string s and a dictionary of strings wordDict, return true if s can
# be segmented into a space-separated sequence of one or more dictionary
# words.
# 
# Note that the same word in the dictionary may be reused multiple times in the
# segmentation.
# 
# 
# Example 1:
# 
# 
# Input: s = "leetcode", wordDict = ["leet","code"]
# Output: true
# Explanation: Return true because "leetcode" can be segmented as "leet
# code".
# 
# 
# Example 2:
# 
# 
# Input: s = "applepenapple", wordDict = ["apple","pen"]
# Output: true
# Explanation: Return true because "applepenapple" can be segmented as "apple
# pen apple".
# Note that you are allowed to reuse a dictionary word.
# 
# 
# Example 3:
# 
# 
# Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
# Output: false
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 300
# 1 <= wordDict.length <= 1000
# 1 <= wordDict[i].length <= 20
# s and wordDict[i] consist of only lowercase English letters.
# All the strings of wordDict are unique.
# 
# 
#

# @lc code=start
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if not s or len(s) == 0 or not wordDict or len(wordDict) == 0:
            return True

        f = [False for _ in range(len(s) + 1)]
        f[0] = True

        max_length = max([len(word) for word in wordDict])

        for i in range(1, len(s) + 1):
            for j in range(max(i - max_length, 0), i):
                if not f[j]:
                    continue
                if s[j:i] in wordDict:
                    f[i] = True
                    break

        return f[-1]
# @lc code=end

