#
# @lc app=leetcode id=316 lang=python3
#
# [316] Remove Duplicate Letters
#
# https://leetcode.com/problems/remove-duplicate-letters/description/
#
# algorithms
# Medium (38.92%)
# Likes:    2316
# Dislikes: 175
# Total Accepted:    116.3K
# Total Submissions: 296.5K
# Testcase Example:  '"bcabc"'
#
# Given a string s, remove duplicate letters so that every letter appears once
# and only once. You must make sure your result is the smallest in
# lexicographical order among all possible results.
# 
# Note: This question is the same as 1081:
# https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/
# 
# 
# Example 1:
# 
# 
# Input: s = "bcabc"
# Output: "abc"
# 
# 
# Example 2:
# 
# 
# Input: s = "cbacdcbc"
# Output: "acdb"
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 10^4
# s consists of lowercase English letters.
# 
# 
#

# @lc code=start
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        
# @lc code=end

