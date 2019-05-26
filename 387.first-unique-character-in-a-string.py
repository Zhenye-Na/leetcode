#
# @lc app=leetcode id=387 lang=python3
#
# [387] First Unique Character in a String
#
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
