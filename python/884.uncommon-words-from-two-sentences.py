#
# @lc app=leetcode id=884 lang=python3
#
# [884] Uncommon Words from Two Sentences
#
# https://leetcode.com/problems/uncommon-words-from-two-sentences/description/
#
# algorithms
# Easy (66.64%)
# Likes:    1365
# Dislikes: 172
# Total Accepted:    151.1K
# Total Submissions: 221.5K
# Testcase Example:  '"this apple is sweet"\n"this apple is sour"'
#
# A sentence is a string of single-space separated words where each word
# consists only of lowercase letters.
#
# A word is uncommon if it appears exactly once in one of the sentences, and
# does not appear in the other sentence.
#
# Given two sentences s1 and s2, return a list of all the uncommon words. You
# may return the answer in any order.
#
#
# Example 1:
#
#
# Input: s1 = "this apple is sweet", s2 = "this apple is sour"
#
# Output: ["sweet","sour"]
#
# Explanation:
#
# The word "sweet" appears only in s1, while the word "sour" appears only in
# s2.
#
#
# Example 2:
#
#
# Input: s1 = "apple apple", s2 = "banana"
#
# Output: ["banana"]
#
#
#
# Constraints:
#
#
# 1 <= s1.length, s2.length <= 200
# s1 and s2 consist of lowercase English letters and spaces.
# s1 and s2 do not have leading or trailing spaces.
# All the words in s1 and s2 are separated by a single space.
#
#
#

# @lc code=start
from typing import Counter


class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        lst1, lst2 = s1.split(" "), s2.split(" ")
        counter1, counter2 = Counter(lst1), Counter(lst2)

        res = []
        for word in counter1:
            if word in counter2:
                continue

            if counter1[word] != 1:
                continue

            res.append(word)

        for word in counter2:
            if word in counter1:
                continue

            if counter2[word] != 1:
                continue

            res.append(word)

        return res


# @lc code=end
