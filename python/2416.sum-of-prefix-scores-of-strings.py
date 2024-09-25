#
# @lc app=leetcode id=2416 lang=python3
#
# [2416] Sum of Prefix Scores of Strings
#
# https://leetcode.com/problems/sum-of-prefix-scores-of-strings/description/
#
# algorithms
# Hard (44.49%)
# Likes:    759
# Dislikes: 65
# Total Accepted:    39.1K
# Total Submissions: 76.1K
# Testcase Example:  '["abc","ab","bc","b"]'
#
# You are given an array words of size n consisting of non-empty strings.
#
# We define the score of a string word as the number of strings words[i] such
# that word is a prefix of words[i].
#
#
# For example, if words = ["a", "ab", "abc", "cab"], then the score of "ab" is
# 2, since "ab" is a prefix of both "ab" and "abc".
#
#
# Return an array answer of size n where answer[i] is the sum of scores of
# every non-empty prefix of words[i].
#
# Note that a string is considered as a prefix of itself.
#
#
# Example 1:
#
#
# Input: words = ["abc","ab","bc","b"]
# Output: [5,4,3,2]
# Explanation: The answer for each string is the following:
# - "abc" has 3 prefixes: "a", "ab", and "abc".
# - There are 2 strings with the prefix "a", 2 strings with the prefix "ab",
# and 1 string with the prefix "abc".
# The total is answer[0] = 2 + 2 + 1 = 5.
# - "ab" has 2 prefixes: "a" and "ab".
# - There are 2 strings with the prefix "a", and 2 strings with the prefix
# "ab".
# The total is answer[1] = 2 + 2 = 4.
# - "bc" has 2 prefixes: "b" and "bc".
# - There are 2 strings with the prefix "b", and 1 string with the prefix "bc".
# The total is answer[2] = 2 + 1 = 3.
# - "b" has 1 prefix: "b".
# - There are 2 strings with the prefix "b".
# The total is answer[3] = 2.
#
#
# Example 2:
#
#
# Input: words = ["abcd"]
# Output: [4]
# Explanation:
# "abcd" has 4 prefixes: "a", "ab", "abc", and "abcd".
# Each prefix has a score of one, so the total is answer[0] = 1 + 1 + 1 + 1 =
# 4.
#
#
#
# Constraints:
#
#
# 1 <= words.length <= 1000
# 1 <= words[i].length <= 1000
# words[i] consists of lowercase English letters.
#
#
#

# @lc code=start
from typing import List


class TrieNode:

    def __init__(self):
        self.count = 0
        self.children = {}
        self.word = None


class Solution:

    def __init__(self):
        self.root = TrieNode()

    def sumPrefixScoresIterative(self, words: List[str]) -> List[int]:
        for word in words:
            self.insert_word(word)

        mapping = {}
        self.dfs(mapping, self.root, 0)

        res = []
        for word in words:
            res.append(mapping[word])

        return res

    def sumPrefixScoresDFS(self, words: List[str]) -> List[int]:
        for word in words:
            self.insert_word(word)

        mapping = {}
        self.dfs(mapping, self.root, 0)

        res = []
        for word in words:
            res.append(mapping[word])

        return res

    def insert_word(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            node.count += 1

        node.word = word

    def get_prefix_score(self, word):
        node = self.root
        prefix_score = 0
        for char in word:
            node = node.children[char]
            prefix_score += node.count
        return prefix_score

    def dfs(self, mapping, node, prev_words):
        if not node:
            return

        curr_words = len(node.words) + prev_words
        if node.word is not None:
            mapping[node.word] = curr_words
        else:
            for child in node.children:
                self.dfs(mapping, node.children[child], curr_words)


# @lc code=end
