#
# @lc app=leetcode id=290 lang=python3
#
# [290] Word Pattern
#
# https://leetcode.com/problems/word-pattern/description/
#
# algorithms
# Easy (38.27%)
# Likes:    1776
# Dislikes: 213
# Total Accepted:    249.3K
# Total Submissions: 649K
# Testcase Example:  '"abba"\n"dog cat cat dog"'
#
# Given a pattern and a string s, find if s follows the same pattern.
# 
# Here follow means a full match, such that there is a bijection between a
# letter in pattern and a non-empty word in s.
# 
# 
# Example 1:
# 
# 
# Input: pattern = "abba", s = "dog cat cat dog"
# Output: true
# 
# 
# Example 2:
# 
# 
# Input: pattern = "abba", s = "dog cat cat fish"
# Output: false
# 
# 
# Example 3:
# 
# 
# Input: pattern = "aaaa", s = "dog cat cat dog"
# Output: false
# 
# 
# Example 4:
# 
# 
# Input: pattern = "abba", s = "dog dog dog dog"
# Output: false
# 
# 
# 
# Constraints:
# 
# 
# 1 <= pattern.length <= 300
# pattern contains only lower-case English letters.
# 1 <= s.length <= 3000
# s contains only lower-case English letters and spaces ' '.
# s does not contain any leading or trailing spaces.
# All the words in s are separated by a single space.
# 
# 
#

# @lc code=start
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        if not pattern or not s or len(pattern) == 0 or len(s) == 0:
            return False

        word_lst = s.split(" ")
        if len(pattern) != len(word_lst):
            return False

        pattern2word = {}
        word2pattern = {}

        length = len(pattern)
        for i in range(length):
            if pattern[i] not in pattern2word:
                pattern2word[pattern[i]] = word_lst[i]
            
            if word_lst[i] not in word2pattern:
                word2pattern[word_lst[i]] = pattern[i]

            if word_lst[i] in word2pattern:
                if word2pattern[word_lst[i]] != pattern[i]:
                    return False

            if pattern2word[pattern[i]] != word_lst[i]:
                return False

        return True
# @lc code=end

