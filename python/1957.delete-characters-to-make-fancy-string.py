#
# @lc app=leetcode id=1957 lang=python3
#
# [1957] Delete Characters to Make Fancy String
#
# https://leetcode.com/problems/delete-characters-to-make-fancy-string/description/
#
# algorithms
# Easy (58.89%)
# Likes:    537
# Dislikes: 28
# Total Accepted:    64.3K
# Total Submissions: 98.3K
# Testcase Example:  '"leeetcode"'
#
# A fancy string is a string where no three consecutive characters are equal.
#
# Given a string s, delete the minimum possible number of characters from s to
# make it fancy.
#
# Return the final string after the deletion. It can be shown that the answer
# will always be unique.
#
#
# Example 1:
#
#
# Input: s = "leeetcode"
# Output: "leetcode"
# Explanation:
# Remove an 'e' from the first group of 'e's to create "leetcode".
# No three consecutive characters are equal, so return "leetcode".
#
#
# Example 2:
#
#
# Input: s = "aaabaaaa"
# Output: "aabaa"
# Explanation:
# Remove an 'a' from the first group of 'a's to create "aabaaaa".
# Remove two 'a's from the second group of 'a's to create "aabaa".
# No three consecutive characters are equal, so return "aabaa".
#
#
# Example 3:
#
#
# Input: s = "aab"
# Output: "aab"
# Explanation: No three consecutive characters are equal, so return "aab".
#
#
#
# Constraints:
#
#
# 1 <= s.length <= 10^5
# s consists only of lowercase English letters.
#
#
#


# @lc code=start
class Solution:
    def makeFancyString(self, s: str) -> str:
        result = []

        for char in s:
            if len(result) >= 2 and result[-1] == char and result[-2] == char:
                continue
            result.append(char)

        return "".join(result)


# @lc code=end
