#
# @lc app=leetcode id=76 lang=python3
#
# [76] Minimum Window Substring
#
# https://leetcode.com/problems/minimum-window-substring/description/
#
# algorithms
# Hard (35.77%)
# Likes:    6218
# Dislikes: 421
# Total Accepted:    509.7K
# Total Submissions: 1.4M
# Testcase Example:  '"ADOBECODEBANC"\n"ABC"'
#
# Given two strings s and t, return the minimum window in s which will contain
# all the characters in t. If there is no such window in s that covers all
# characters in t, return the empty string "".
# 
# Note that If there is such a window, it is guaranteed that there will always
# be only one unique minimum window in s.
# 
# 
# Example 1:
# Input: s = "ADOBECODEBANC", t = "ABC"
# Output: "BANC"
# Example 2:
# Input: s = "a", t = "a"
# Output: "a"
# 
# 
# Constraints:
# 
# 
# 1 <= s.length, t.length <= 10^5
# s and t consist of English letters.
# 
# 
# 
# Follow up: Could you find an algorithm that runs in O(n) time?
#

# @lc code=start
from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        res, min_len = "", len(s) + 1
        counter_t = Counter(t)
        counter_s = {}
        j = 0
        num_letter = len(set(list(t)))
        counter_letter = 0

        for i in range(len(s)):
            while j < len(s) and counter_letter < num_letter:
                counter_s[s[j]] = counter_s.get(s[j], 0) + 1
                if s[j] in counter_t and counter_s[s[j]] == counter_t[s[j]]:
                    # we have collected all the occurences of this letter
                    counter_letter += 1
            
                j += 1

            if num_letter == counter_letter:
                # we have collected all
                if j - i < min_len:
                    res = s[i:j]
                    min_len = j - i

            # delete previous s[i]
            counter_s[s[i]] -= 1
            if s[i] in counter_t and counter_s[s[i]] == counter_t[s[i]] - 1:
                counter_letter -= 1

        return res
# @lc code=end

