#
# @lc app=leetcode id=792 lang=python3
#
# [792] Number of Matching Subsequences
#
# https://leetcode.com/problems/number-of-matching-subsequences/description/
#
# algorithms
# Medium (48.70%)
# Likes:    1848
# Dislikes: 106
# Total Accepted:    81K
# Total Submissions: 166K
# Testcase Example:  '"abcde"\n["a","bb","acd","ace"]'
#
# Given a string s and an array of strings words, return the number of words[i]
# that is a subsequence of s.
# 
# A subsequence of a string is a new string generated from the original string
# with some characters (can be none) deleted without changing the relative
# order of the remaining characters.
# 
# 
# For example, "ace" is a subsequence of "abcde".
# 
# 
# 
# Example 1:
# 
# 
# Input: s = "abcde", words = ["a","bb","acd","ace"]
# Output: 3
# Explanation: There are three strings in words that are a subsequence of s:
# "a", "acd", "ace".
# 
# 
# Example 2:
# 
# 
# Input: s = "dsahjpjauf", words = ["ahjpjau","ja","ahbwzgqnuk","tnmlanowax"]
# Output: 2
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 5 * 10^4
# 1 <= words.length <= 5000
# 1 <= words[i].length <= 50
# s and words[i] consist of only lowercase English letters.
# 
# 
#

# @lc code=start
from collections import defaultdict

import bisect

class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        def issubseq(t):
            current_pos = -1
            stack = []
            for i in t:
                if indices[i]:
                    pos = bisect.bisect_right(indices[i], current_pos)
                    if pos == len(indices[i]):
                        return False
                    current_pos = indices[i][pos]
                else:
                    return False
            return True

        indices = defaultdict(list)
        for i, c in enumerate(s):
            indices[c].append(i)
     
        hashmap = {}

        count = 0
        for word in words:
            if word not in hashmap:
                if issubseq(word):
                    count += 1
                    hashmap[word] = True
                else:
                    hashmap[word] = False
            else:
                if hashmap[word]:
                    count += 1
        return count
# @lc code=end

