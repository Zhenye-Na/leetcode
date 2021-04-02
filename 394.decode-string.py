#
# @lc app=leetcode id=394 lang=python3
#
# [394] Decode String
#
# https://leetcode.com/problems/decode-string/description/
#
# algorithms
# Medium (52.43%)
# Likes:    4808
# Dislikes: 228
# Total Accepted:    314.7K
# Total Submissions: 594.8K
# Testcase Example:  '"3[a]2[bc]"'
#
# Given an encoded string, return its decoded string.
# 
# The encoding rule is: k[encoded_string], where the encoded_string inside the
# square brackets is being repeated exactly k times. Note that k is guaranteed
# to be a positive integer.
# 
# You may assume that the input string is always valid; No extra white spaces,
# square brackets are well-formed, etc.
# 
# Furthermore, you may assume that the original data does not contain any
# digits and that digits are only for those repeat numbers, k. For example,
# there won't be input like 3a or 2[4].
# 
# 
# Example 1:
# Input: s = "3[a]2[bc]"
# Output: "aaabcbc"
# Example 2:
# Input: s = "3[a2[c]]"
# Output: "accaccacc"
# Example 3:
# Input: s = "2[abc]3[cd]ef"
# Output: "abcabccdcdcdef"
# Example 4:
# Input: s = "abc3[cd]xyz"
# Output: "abccdcdcdxyz"
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 30
# s consists of lowercase English letters, digits, and square brackets
# '[]'.
# s is guaranteed to be a valid input.
# All the integers in s are in the range [1, 300].
# 
# 
#

# @lc code=start
class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        i = 0

        res = 0
        while i < len(s):

            if s[i].isdigit():
                num = int(s[i])
                i += 1
                while i < len(s) and s[i].isdigit():
                    num = num * 10 + int(s[i])
                    i += 1

                stack.append(num)

            elif s[i] == "[" or s[i].isalpha():
                stack.append(s[i])
                i += 1

            else:
                # s[i] == "]"
                string_stack = []
                while stack and stack[-1] != "[":
                    string_stack.append(stack.pop())

                strings = ""
                while string_stack:
                    strings += string_stack.pop()

                stack.pop() # pop the "["
                dup = stack.pop()

                strings = strings * dup

                stack.append(strings)

                i += 1

        return "".join(stack)
# @lc code=end

