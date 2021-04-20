#
# @lc app=leetcode id=345 lang=python3
#
# [345] Reverse Vowels of a String
#
# https://leetcode.com/problems/reverse-vowels-of-a-string/description/
#
# algorithms
# Easy (44.95%)
# Likes:    935
# Dislikes: 1434
# Total Accepted:    265.2K
# Total Submissions: 588.2K
# Testcase Example:  '"hello"'
#
# Write a function that takes a string as input and reverse only the vowels of
# a string.
# 
# Example 1:
# 
# 
# Input: "hello"
# Output: "holle"
# 
# 
# 
# Example 2:
# 
# 
# Input: "leetcode"
# Output: "leotcede"
# 
# 
# Note:
# The vowels does not include the letter "y".
# 
# 
# 
#

# @lc code=start
class Solution:
    def __init__(self):
        self.vowels = ["a", "e", "i", "o", "u"]

    def reverseVowels(self, s: str) -> str:
        if not s or len(s) == 0:
            return s

        left, right = 0, len(s) - 1
        s_lst = [i for i in s]
        while left <= right:
            while left <= right and not self._check_vowels(s_lst[left]):
                left += 1
            while left <= right and not self._check_vowels(s_lst[right]):
                right -= 1
            
            if left <= right:
                s_lst[left], s_lst[right] = s_lst[right], s_lst[left]
                left += 1
                right -= 1

        return "".join(s_lst)

    def _check_vowels(self, character):
        return character.lower() in self.vowels

# @lc code=end

