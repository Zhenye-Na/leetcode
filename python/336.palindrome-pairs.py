#
# @lc app=leetcode id=336 lang=python3
#
# [336] Palindrome Pairs
#
# https://leetcode.com/problems/palindrome-pairs/description/
#
# algorithms
# Hard (34.46%)
# Likes:    1735
# Dislikes: 169
# Total Accepted:    114.1K
# Total Submissions: 327.9K
# Testcase Example:  '["abcd","dcba","lls","s","sssll"]'
#
# Given a list of unique words, return all the pairs of the distinct indices
# (i, j) in the given list, so that the concatenation of the two words words[i]
# + words[j] is a palindrome.
# 
# 
# Example 1:
# 
# 
# Input: words = ["abcd","dcba","lls","s","sssll"]
# Output: [[0,1],[1,0],[3,2],[2,4]]
# Explanation: The palindromes are ["dcbaabcd","abcddcba","slls","llssssll"]
# 
# 
# Example 2:
# 
# 
# Input: words = ["bat","tab","cat"]
# Output: [[0,1],[1,0]]
# Explanation: The palindromes are ["battab","tabbat"]
# 
# 
# Example 3:
# 
# 
# Input: words = ["a",""]
# Output: [[0,1],[1,0]]
# 
# 
# 
# Constraints:
# 
# 
# 1 <= words.length <= 5000
# 0 <= words[i].length <= 300
# words[i] consists of lower-case English letters.
# 
# 
#

# @lc code=start
class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        
        if not words or len(words) == 0:
            return []

        res = []
        self.palindrome = set([])

        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if words[i] in self.palindrome and words[j] in self.palindrome:
                    res.append([i, j])
                    res.append([j, i])
                    continue

                if self.is_palindrome(words[i]):
                    self.palindrome.add(words[i])

                if self.is_palindrome(words[j]):
                    self.palindrome.add(words[j])

                if self.is_palindrome(words[i] + words[j]):
                    res.append([i, j])
                if self.is_palindrome(words[j] + words[i]):
                    res.append([j, i])

        return res


    def is_palindrome(self, s):
        if s == s[::-1]:
            self.palindrome.add(s)
            return True
        return False

# @lc code=end

