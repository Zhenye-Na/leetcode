# [340] Longest Substring with At Most K Distinct Characters

# Description

# Given a string S, find the length of the longest substring T
# that contains at most k distinct characters.

# Example

# Example 1:
# Input: S = "eceba" and k = 3
# Output: 4
# Explanation: T = "eceb"

# Example 2:
# Input: S = "WORLD" and k = 4
# Output: 4
# Explanation: T = "WORL" or "ORLD"

# Challenge
# O(n) time

from collections import defaultdict

class Solution:
    """
    @param s: A string
    @param k: An integer
    @return: An integer
    """
    def lengthOfLongestSubstringKDistinct(self, s, k):
        # write your code here
        if not s or len(s) == 0 or k == 0:
            return 0

        j = 0
        counter = defaultdict(int)
        length = 0

        for i in range(len(s)):
            while j < len(s) and (len(counter) < k or s[j] in counter):
                counter[s[j]] += 1
                j += 1

            if len(counter) == k or j == len(s):
                length = max(length, j - i)

            counter[s[i]] -= 1
            if counter[s[i]] == 0:
                del counter[s[i]]


        return length


