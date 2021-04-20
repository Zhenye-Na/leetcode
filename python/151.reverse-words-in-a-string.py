#
# @lc app=leetcode id=151 lang=python3
#
# [151] Reverse Words in a String
#
# https://leetcode.com/problems/reverse-words-in-a-string/description/
#
# algorithms
# Medium (23.41%)
# Likes:    1547
# Dislikes: 3170
# Total Accepted:    505.7K
# Total Submissions: 2.1M
# Testcase Example:  '"the sky is blue"'
#
# Given an input string s, reverse the order of the words.
# 
# A word is defined as a sequence of non-space characters. The words in s will
# be separated by at least one space.
# 
# Return a string of the words in reverse order concatenated by a single
# space.
# 
# Note that s may contain leading or trailing spaces or multiple spaces between
# two words. The returned string should only have a single space separating the
# words. Do not include any extra spaces.
# 
# 
# Example 1:
# 
# 
# Input: s = "the sky is blue"
# Output: "blue is sky the"
# 
# 
# Example 2:
# 
# 
# Input: s = "  hello world  "
# Output: "world hello"
# Explanation: Your reversed string should not contain leading or trailing
# spaces.
# 
# 
# Example 3:
# 
# 
# Input: s = "a good   example"
# Output: "example good a"
# Explanation: You need to reduce multiple spaces between two words to a single
# space in the reversed string.
# 
# 
# Example 4:
# 
# 
# Input: s = "  Bob    Loves  Alice   "
# Output: "Alice Loves Bob"
# 
# 
# Example 5:
# 
# 
# Input: s = "Alice does not even like bob"
# Output: "bob like even not does Alice"
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 10^4
# s contains English letters (upper-case and lower-case), digits, and spaces '
# '.
# There is at least one word in s.
# 
# 
# 
# Follow up: Could you solve it in-place with O(1) extra space?
# 
#

# @lc code=start
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


class Solution_Swap:
    def reverseWords(self, s: str) -> str:
        if not s or len(s) == 0:
            return s
        
        s = s.lstrip().rstrip()
        s = re.sub(' +', ' ', s)
        s = [char for char in s] + [" "]
        n = len(s)

        i, j = 0, 0
        while i < n and j <= n:
            while i < n and s[i] == " ":
                i += 1
            j = i + 1
            while j <= n and s[j] != " ":
                j += 1

            # swap s[i:j]
            if i < n and j <= n:
                left, right = i, j - 1
                while left <= right:
                    s[left], s[right] = s[right], s[left]
                    left += 1
                    right -= 1

            i = j

        return "".join(s[::-1]).lstrip()
# @lc code=end

