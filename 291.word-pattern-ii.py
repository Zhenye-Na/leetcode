# Word Pattern II

# Given a pattern and a string str, find if str follows the same pattern.

# Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty substring in str.(i.e if a corresponds to s, then b cannot correspond to s. For example, given pattern = "ab", str = "ss", return false.)

# Example
# Example 1

# Input:
# pattern = "abab"
# str = "redblueredblue"
# Output: true
# Explanation: "a"->"red","b"->"blue"
# Example 2

# Input:
# pattern = "aaaa"
# str = "asdasdasdasd"
# Output: true
# Explanation: "a"->"asd"
# Example 3

# Input:
# pattern = "aabb"
# str = "xyzabcxzyabc"
# Output: false
# Notice
# You may assume both pattern and str contains only lowercase letters.


class Solution:
    """
    @param pattern: a string,denote pattern string
    @param str: a string, denote matching string
    @return: a boolean
    """
    def wordPatternMatch(self, pattern, string):
        # write your code here
        mapping = {}
        used = set([])
        return self._dfs(pattern, 0, string, 0, mapping, used)



    def _dfs(self, pattern, i, string, j, mapping, used):
        if i == len(pattern):
            return j >= len(string)

        char = pattern[i]
        if char in mapping:
            word = mapping[char]

            if not string[j:].startswith(word):
                return False

            return self._dfs(pattern, i + 1, string, j + len(word), mapping, used)

        for x in range(j, len(string)):
            curr = string[j:x + 1]
            if curr in used:
                continue

            used.add(curr)
            mapping[char] = curr
            
            if self._dfs(pattern, i + 1, string, x + 1, mapping, used):
                return True

            del mapping[char]
            used.remove(curr)

        return False

