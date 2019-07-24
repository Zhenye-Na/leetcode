#
# @lc app=leetcode id=151 lang=python3
#
# [151] Reverse Words in a String
#
import re

class Solution:
    def reverseWords(self, s: str) -> str:
        if not s or len(s) == 0:
            return ''

        s = re.sub(' +', ' ', s)
        s_list = s.strip().split(' ')
        for i in range(len(s_list)):
            s_list[i] = s_list[i].strip()[::-1]

        new_s = ' '.join(s_list)
        return new_s[::-1]
