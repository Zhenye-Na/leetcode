#
# @lc app=leetcode id=387 lang=python3
#
# [387] First Unique Character in a String
#
# https://leetcode.com/problems/first-unique-character-in-a-string/description/
#
# algorithms
# Easy (53.74%)
# Likes:    2697
# Dislikes: 133
# Total Accepted:    690.3K
# Total Submissions: 1.3M
# Testcase Example:  '"leetcode"'
#
# Given a string, find the first non-repeating character in it and return its
# index. If it doesn't exist, return -1.
# 
# Examples:
# 
# 
# s = "leetcode"
# return 0.
# 
# s = "loveleetcode"
# return 2.
# 
# 
# 
# 
# Note: You may assume the string contains only lowercase English letters.
# 
#

# @lc code=start
class Solution:
    def firstUniqChar(self, s: str) -> int:

        mapping = {}

        if not s or len(s) <= 0:
            return -1

        for idx, char in enumerate(s):
            mapping[char] = mapping.get(char, 0) + 1

        for idx, key in enumerate(s):
            if mapping[key] == 1:
                return idx

        return -1
# @lc code=end

