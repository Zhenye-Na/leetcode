# 186. Reverse Words in a String II

# Description
# Given an input character array, reverse the array word by word.
# A word is defined as a sequence of non-space characters.

# The input character array does not contain leading or trailing spaces
# and the words are always separated by a single space.


# Example

# Example1

# Input: s = "the sky is blue"
# Output: "blue is sky the"

# Example2

# Input: "a b c"
# Output: "c b a"

# Challenge
# Could you do it in-place without allocating extra space?


class Solution:
    """
    @param str: a string
    @return: return a string
    """
    def reverseWords(self, str):
        # write your code here
        s_lst = str.split(" ")
        for i in range(len(s_lst)):
            s_lst[i] = s_lst[i][::-1]

        new_str = " ".join(s_lst)
        return new_str[::-1]

