#
# @lc app=leetcode id=3163 lang=python3
#
# [3163] String Compression III
#
# https://leetcode.com/problems/string-compression-iii/description/
#
# algorithms
# Medium (56.00%)
# Likes:    230
# Dislikes: 17
# Total Accepted:    69.1K
# Total Submissions: 110.6K
# Testcase Example:  '"abcde"'
#
# Given a string word, compress it using the following algorithm:
#
#
# Begin with an empty string comp. While word is not empty, use the following
# operation:
#
#
# Remove a maximum length prefix of word made of a single character c repeating
# at most 9 times.
# Append the length of the prefix followed by c to comp.
#
#
#
#
# Return the string comp.
#
#
# Example 1:
#
#
# Input: word = "abcde"
#
# Output: "1a1b1c1d1e"
#
# Explanation:
#
# Initially, comp = "". Apply the operation 5 times, choosing "a", "b", "c",
# "d", and "e" as the prefix in each operation.
#
# For each prefix, append "1" followed by the character to comp.
#
#
# Example 2:
#
#
# Input: word = "aaaaaaaaaaaaaabb"
#
# Output: "9a5a2b"
#
# Explanation:
#
# Initially, comp = "". Apply the operation 3 times, choosing "aaaaaaaaa",
# "aaaaa", and "bb" as the prefix in each operation.
#
#
# For prefix "aaaaaaaaa", append "9" followed by "a" to comp.
# For prefix "aaaaa", append "5" followed by "a" to comp.
# For prefix "bb", append "2" followed by "b" to comp.
#
#
#
#
# Constraints:
#
#
# 1 <= word.length <= 2 * 10^5
# word consists only of lowercase English letters.
#
#
#


# @lc code=start
class Solution:
    def compressedString(self, word: str) -> str:
        comp = ""
        i = 0

        while i < len(word):
            count = 1
            while i + count < len(word) and word[i] == word[i + count] and count < 9:
                count += 1

            comp += str(count) + word[i]
            i += count

        return comp


# @lc code=end
