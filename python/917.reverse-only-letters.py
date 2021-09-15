#
# @lc app=leetcode id=917 lang=python3
#
# [917] Reverse Only Letters
#
# https://leetcode.com/problems/reverse-only-letters/description/
#
# algorithms
# Easy (59.56%)
# Likes:    1163
# Dislikes: 47
# Total Accepted:    112.6K
# Total Submissions: 185.9K
# Testcase Example:  '"ab-cd"'
#
# Given a string s, reverse the string according to the following rules:
# 
# 
# All the characters that are not English letters remain in the same
# position.
# All the English letters (lowercase or uppercase) should be reversed.
# 
# 
# Return s after reversing it.
# 
# 
# Example 1:
# Input: s = "ab-cd"
# Output: "dc-ba"
# Example 2:
# Input: s = "a-bC-dEf-ghIj"
# Output: "j-Ih-gfE-dCba"
# Example 3:
# Input: s = "Test1ng-Leet=code-Q!"
# Output: "Qedo1ct-eeLg=ntse-T!"
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 100
# s consists of characters with ASCII values in the range [33, 122].
# s does not contain '\"' or '\\'.
# 
# 
#

# @lc code=start
class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        if not s or len(s) == 0:
            return s

        s = [char for char in s]
        left, right = 0, len(s) - 1
        while left < right:
            while left < right and not s[left].lower().isalpha():
                left += 1
            while left < right and not s[right].lower().isalpha():
                right -= 1
    
            if left < right:
                print(left, right, s[left], s[right])
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1

        return "".join(s)
# @lc code=end

