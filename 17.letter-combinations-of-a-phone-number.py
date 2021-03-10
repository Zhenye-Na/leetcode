#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#
# https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/
#
# algorithms
# Medium (48.78%)
# Likes:    5494
# Dislikes: 499
# Total Accepted:    775.5K
# Total Submissions: 1.6M
# Testcase Example:  '"23"'
#
# Given a string containing digits from 2-9 inclusive, return all possible
# letter combinations that the number could represent. Return the answer in any
# order.
# 
# A mapping of digit to letters (just like on the telephone buttons) is given
# below. Note that 1 does not map to any letters.
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: digits = "23"
# Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
# 
# 
# Example 2:
# 
# 
# Input: digits = ""
# Output: []
# 
# 
# Example 3:
# 
# 
# Input: digits = "2"
# Output: ["a","b","c"]
# 
# 
# 
# Constraints:
# 
# 
# 0 <= digits.length <= 4
# digits[i] is a digit in the range ['2', '9'].
# 
# 
#

# @lc code=start
class Solution:
    def __init__(self):
        self.int2letter = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }


    def letterCombinations(self, digits: str) -> List[str]:
        if not digits or len(digits) == 0:
            return []
        res = []
        self._dfs(digits, res, "", 0)
        return res


    def _dfs(self, digits, res, curr, idx):
        if len(curr) == len(digits):
            res.append(curr[:])
            return

        if idx >= len(digits):
            return

        for char in self.int2letter[digits[idx]]:
            self._dfs(digits, res, curr + char, idx + 1)
# @lc code=end

