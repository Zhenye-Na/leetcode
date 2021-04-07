#
# @lc app=leetcode id=443 lang=python3
#
# [443] String Compression
#
# https://leetcode.com/problems/string-compression/description/
#
# algorithms
# Medium (43.21%)
# Likes:    1248
# Dislikes: 3164
# Total Accepted:    163.1K
# Total Submissions: 369.8K
# Testcase Example:  '["a","a","b","b","c","c","c"]'
#
# Given an array of characters chars, compress it using the following
# algorithm:
# 
# Begin with an empty string s. For each group of consecutive repeating
# characters in chars:
# 
# 
# If the group's length is 1, append the character to s.
# Otherwise, append the character followed by the group's length.
# 
# 
# The compressed string s should not be returned separately, but instead be
# stored in the input character array chars. Note that group lengths that are
# 10 or longer will be split into multiple characters in chars.
# 
# After you are done modifying the input array, return the new length of the
# array.
# 
# 
# Follow up:
# Could you solve it using only O(1) extra space?
# 
# 
# Example 1:
# 
# 
# Input: chars = ["a","a","b","b","c","c","c"]
# Output: Return 6, and the first 6 characters of the input array should be:
# ["a","2","b","2","c","3"]
# Explanation: The groups are "aa", "bb", and "ccc". This compresses to
# "a2b2c3".
# 
# 
# Example 2:
# 
# 
# Input: chars = ["a"]
# Output: Return 1, and the first character of the input array should be: ["a"]
# Explanation: The only group is "a", which remains uncompressed since it's a
# single character.
# 
# 
# Example 3:
# 
# 
# Input: chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
# Output: Return 4, and the first 4 characters of the input array should be:
# ["a","b","1","2"].
# Explanation: The groups are "a" and "bbbbbbbbbbbb". This compresses to
# "ab12".
# 
# Example 4:
# 
# 
# Input: chars = ["a","a","a","b","b","a","a"]
# Output: Return 6, and the first 6 characters of the input array should be:
# ["a","3","b","2","a","2"].
# Explanation: The groups are "aaa", "bb", and "aa". This compresses to
# "a3b2a2". Note that each group is independent even if two groups have the
# same character.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= chars.length <= 2000
# chars[i] is a lower-case English letter, upper-case English letter, digit, or
# symbol.
# 
# 
#

# @lc code=start
class Solution:
    def compress(self, chars: List[str]) -> int:
        i, j = 0, 0
        start = 0
        while i < len(chars) and j < len(chars):
            curr = chars[i]
            while j < len(chars) and chars[j] == curr:
                j += 1

            # chars[j] is a different letter
            counts = j - i
            if counts == 1:
                chars[start] = curr
                start += 1
            else:
                chars[start] = curr
                start += 1
                for digit in str(counts):
                    chars[start] = digit
                    start += 1

            i = j

        return start
# @lc code=end

