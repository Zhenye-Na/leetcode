#
# @lc app=leetcode id=1704 lang=python3
#
# [1704] Determine if String Halves Are Alike
#
# https://leetcode.com/problems/determine-if-string-halves-are-alike/description/
#
# algorithms
# Easy (78.04%)
# Likes:    254
# Dislikes: 24
# Total Accepted:    47.8K
# Total Submissions: 60.1K
# Testcase Example:  '"book"'
#
# You are given a string s of even length. Split this string into two halves of
# equal lengths, and let a be the first half and b be the second half.
# 
# Two strings are alike if they have the same number of vowels ('a', 'e', 'i',
# 'o', 'u', 'A', 'E', 'I', 'O', 'U'). Notice that s contains uppercase and
# lowercase letters.
# 
# Return true if a and b are alike. Otherwise, return false.
# 
# 
# Example 1:
# 
# 
# Input: s = "book"
# Output: true
# Explanation: a = "bo" and b = "ok". a has 1 vowel and b has 1 vowel.
# Therefore, they are alike.
# 
# 
# Example 2:
# 
# 
# Input: s = "textbook"
# Output: false
# Explanation: a = "text" and b = "book". a has 1 vowel whereas b has 2.
# Therefore, they are not alike.
# Notice that the vowel o is counted twice.
# 
# 
# Example 3:
# 
# 
# Input: s = "MerryChristmas"
# Output: false
# 
# 
# Example 4:
# 
# 
# Input: s = "AbCdEfGh"
# Output: true
# 
# 
# 
# Constraints:
# 
# 
# 2 <= s.length <= 1000
# s.length is even.
# s consists of uppercase and lowercase letters.
# 
# 
#

# @lc code=start
class Solution:

    def __init__(self):
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        self.vowels = set(vowels)    


    def halvesAreAlike(self, s: str) -> bool:
        mid = len(s) // 2
        count = 0

        for i in range(mid):
            count += 1 if s[i] in self.vowels else 0

        for i in range(mid, len(s)):
            count -= 1 if s[i] in self.vowels else 0

        return count == 0
# @lc code=end

