#
# @lc app=leetcode id=68 lang=python3
#
# [68] Text Justification
#
# https://leetcode.com/problems/text-justification/description/
#
# algorithms
# Hard (29.35%)
# Likes:    950
# Dislikes: 1897
# Total Accepted:    162.9K
# Total Submissions: 546.2K
# Testcase Example:  '["This", "is", "an", "example", "of", "text", "justification."]\n16'
#
# Given an array of words and a width maxWidth, format the text such that each
# line has exactly maxWidth characters and is fully (left and right)
# justified.
# 
# You should pack your words in a greedy approach; that is, pack as many words
# as you can in each line. Pad extra spaces ' ' when necessary so that each
# line has exactly maxWidth characters.
# 
# Extra spaces between words should be distributed as evenly as possible. If
# the number of spaces on a line do not divide evenly between words, the empty
# slots on the left will be assigned more spaces than the slots on the right.
# 
# For the last line of text, it should be left justified and no extra space is
# inserted between words.
# 
# Note:
# 
# 
# A word is defined as a character sequence consisting of non-space characters
# only.
# Each word's length is guaranteed to be greater than 0 and not exceed
# maxWidth.
# The input array words contains at least one word.
# 
# 
# 
# Example 1:
# 
# 
# Input: words = ["This", "is", "an", "example", "of", "text",
# "justification."], maxWidth = 16
# Output:
# [
# "This    is    an",
# "example  of text",
# "justification.  "
# ]
# 
# Example 2:
# 
# 
# Input: words = ["What","must","be","acknowledgment","shall","be"], maxWidth =
# 16
# Output:
# [
# "What   must   be",
# "acknowledgment  ",
# "shall be        "
# ]
# Explanation: Note that the last line is "shall be    " instead of "shall
# be", because the last line must be left-justified instead of fully-justified.
# Note that the second line is also left-justified becase it contains only one
# word.
# 
# Example 3:
# 
# 
# Input: words =
# ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"],
# maxWidth = 20
# Output:
# [
# "Science  is  what we",
# ⁠ "understand      well",
# "enough to explain to",
# "a  computer.  Art is",
# "everything  else  we",
# "do                  "
# ]
# 
# 
# Constraints:
# 
# 
# 1 <= words.length <= 300
# 1 <= words[i].length <= 20
# words[i] consists of only English letters and symbols.
# 1 <= maxWidth <= 100
# words[i].length <= maxWidth
# 
# 
#

# @lc code=start
class Solution:
    def __init__(self):
        self.res = []

    def fullJustify(self, words: List[str], max_width: int) -> List[str]:
        i, j = 0, 0
        while i < len(words):
            j = i + 1
            curr_length = len(words[i])
            while j < len(words) and curr_length + len(words[j]) + (j - i) <= max_width:
                curr_length += len(words[j])
                j += 1

            # we already reach the limit of max_width
            if j >= len(words) or j - i == 1:
                # reach the last line or only one word this line
                self.left_justify(words, i, j, curr_length, max_width)
            else:
                self.justify(words, i, j, curr_length, max_width)

            i = j

        return self.res


    def left_justify(self, words, i, j, curr_length, max_width):
        spaces = max_width - curr_length - (j - i - 1)
        line = " ".join(words[i:j])
        line += " " * spaces
        self.res.append(line)


    def justify(self, words, i, j, curr_length, max_width):
        num_positions = j - i - 1
        num_spaces = (max_width - curr_length) // num_positions
        extra_spaces = (max_width - curr_length) % num_positions

        line = ""
        for ptr in range(i, j - 1):
            line = line + words[ptr] + " " * (num_spaces + 1 if extra_spaces > 0 else num_spaces)
            extra_spaces -= 1

        line = line + words[j - 1]
        self.res.append(line)
# @lc code=end

