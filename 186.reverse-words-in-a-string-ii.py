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
    def reverseWords(self, string):
        string = [char for char in string]
        
        # reverse every word in the string
        i = j = 0
        while i < len(string) and j < len(string):
            while i < len(string) and not string[i].isalpha():
                i += 1
            # string[i] is a letter
            j = i
            while j < len(string) and string[j].isalpha():
                j += 1
            # string[j] will be the space after a char

            # swap i ~ j - 1
            left , right = i, j - 1
            while left <= right:
                string[left], string[right] = string[right], string[left]
                left += 1
                right -= 1

            # move pointer forward
            i = j

        # reverse the entire string
        left, right = 0, len(string) - 1
        while left <= right:
            string[left], string[right] = string[right], string[left]
            left += 1
            right -= 1

        return "".join(string)


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

