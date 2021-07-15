#
# @lc app=leetcode id=791 lang=python3
#
# [791] Custom Sort String
#
# https://leetcode.com/problems/custom-sort-string/description/
#
# algorithms
# Medium (66.00%)
# Likes:    1362
# Dislikes: 243
# Total Accepted:    118.7K
# Total Submissions: 177.2K
# Testcase Example:  '"cba"\n"abcd"'
#
# order and str are strings composed of lowercase letters. In order, no letter
# occurs more than once.
# 
# order was sorted in some custom order previously. We want to permute the
# characters of str so that they match the order that order was sorted. More
# specifically, if x occurs before y in order, then x should occur before y in
# the returned string.
# 
# Return any permutation of str (as a string) that satisfies this property.
# 
# 
# Example:
# Input: 
# order = "cba"
# str = "abcd"
# Output: "cbad"
# Explanation: 
# "a", "b", "c" appear in order, so the order of "a", "b", "c" should be "c",
# "b", and "a". 
# Since "d" does not appear in order, it can be at any position in the returned
# string. "dcba", "cdba", "cbda" are also valid outputs.
# 
# 
# 
# 
# Note:
# 
# 
# order has length at most 26, and no character is repeated in order.
# str has length at most 200.
# order and str consist of lowercase letters only.
# 
# 
#

# @lc code=start
from collections import Counter

class Solution:
    def customSortString(self, order: str, str: str) -> str:
        if not order or not str or len(str) == 0:
            return str

        counter = Counter(str)
        
        res = ""
        for char in order:
            if char in counter:
                res += counter[char] * char
                del counter[char]

        for char in counter:
            res += char * counter[char]
                
        return res
# @lc code=end

