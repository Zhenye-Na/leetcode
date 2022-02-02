#
# @lc app=leetcode id=438 lang=python3
#
# [438] Find All Anagrams in a String
#
# https://leetcode.com/problems/find-all-anagrams-in-a-string/description/
#
# algorithms
# Medium (45.86%)
# Likes:    6152
# Dislikes: 235
# Total Accepted:    457.7K
# Total Submissions: 965.3K
# Testcase Example:  '"cbaebabacd"\n"abc"'
#
# Given two strings s and p, return an array of all the start indices of p's
# anagrams in s. You may return the answer in any order.
# 
# An Anagram is a word or phrase formed by rearranging the letters of a
# different word or phrase, typically using all the original letters exactly
# once.
# 
# 
# Example 1:
# 
# 
# Input: s = "cbaebabacd", p = "abc"
# Output: [0,6]
# Explanation:
# The substring with start index = 0 is "cba", which is an anagram of "abc".
# The substring with start index = 6 is "bac", which is an anagram of "abc".
# 
# 
# Example 2:
# 
# 
# Input: s = "abab", p = "ab"
# Output: [0,1,2]
# Explanation:
# The substring with start index = 0 is "ab", which is an anagram of "ab".
# The substring with start index = 1 is "ba", which is an anagram of "ab".
# The substring with start index = 2 is "ab", which is an anagram of "ab".
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s.length, p.length <= 3 * 10^4
# s and p consist of lowercase English letters.
# 
# 
#

# @lc code=start
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        length = len(p)
        left, right = 0, length - 1
        res = []
        counts = collections.Counter(s[left:right + 1])
        p_counter = collections.Counter(p)
        if counts == p_counter:
            res.append(0)

        while right + 1 < len(s):
            if counts[s[left]] == 1:
                del counts[s[left]]
            else:
                counts[s[left]] -= 1
            left += 1
            right += 1
            counts[s[right]] = counts.get(s[right], 0) + 1

            if counts == p_counter:
                res.append(left)

        return res
# @lc code=end

