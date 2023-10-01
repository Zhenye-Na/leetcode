#
# @lc app=leetcode id=557 lang=python3
#
# [557] Reverse Words in a String III
#
# https://leetcode.com/problems/reverse-words-in-a-string-iii/description/
#
# algorithms
# Easy (73.37%)
# Likes:    5226
# Dislikes: 233
# Total Accepted:    738K
# Total Submissions: 898.5K
# Testcase Example:  `"Let's take LeetCode contest"`
#
# Given a string s, reverse the order of characters in each word within a
# sentence while still preserving whitespace and initial word order.
# 
# 
# Example 1:
# Input: s = "Let's take LeetCode contest"
# Output: "s'teL ekat edoCteeL tsetnoc"
# Example 2:
# Input: s = "God Ding"
# Output: "doG gniD"
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 5 * 10^4
# s contains printable ASCII characters.
# s does not contain any leading or trailing spaces.
# There is at least one word in s.
# All the words in s are separated by a single space.
# 
# 
#

# @lc code=start
class Solution:
    def reverseWords(self, s: str) -> str:

        words = s.split(" ")
        res = []
        for word in words:
            res.append(word[::-1][:])

        return " ".join(res)

class Solution:
    def reverseWords(self, s: str) -> str:
        if not s or len(s) == 0:
            return s

        i, j = 0, 0
        while j < len(s):
            i = j
            while j < len(s) and s[j] != " ":
                j += 1

            s = self.swap(s, i, j)
            j += 1

        return s

    def swap(self, s, start, end):
        left, right = start, end - 1
        while left < right:
            if right + 1 < len(s):
                s = s[:left] + s[right] + s[left + 1: right] + s[left] + s[right + 1:]
            else:
                s = s[:left] + s[right] + s[left + 1: right] + s[left]
            left += 1
            right -= 1

        return s
# @lc code=end

