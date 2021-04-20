#
# @lc app=leetcode id=692 lang=python3
#
# [692] Top K Frequent Words
#
# https://leetcode.com/problems/top-k-frequent-words/description/
#
# algorithms
# Medium (52.94%)
# Likes:    2895
# Dislikes: 192
# Total Accepted:    270.7K
# Total Submissions: 508K
# Testcase Example:  '["i", "love", "leetcode", "i", "love", "coding"]\n2'
#
# Given a non-empty list of words, return the k most frequent elements.
# Your answer should be sorted by frequency from highest to lowest. If two
# words have the same frequency, then the word with the lower alphabetical
# order comes first.
# 
# Example 1:
# 
# Input: ["i", "love", "leetcode", "i", "love", "coding"], k = 2
# Output: ["i", "love"]
# Explanation: "i" and "love" are the two most frequent words.
# ⁠   Note that "i" comes before "love" due to a lower alphabetical order.
# 
# 
# 
# Example 2:
# 
# Input: ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is",
# "is"], k = 4
# Output: ["the", "is", "sunny", "day"]
# Explanation: "the", "is", "sunny" and "day" are the four most frequent words,
# ⁠   with the number of occurrence being 4, 3, 2 and 1 respectively.
# 
# 
# 
# Note:
# 
# You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
# Input words contain only lowercase letters.
# 
# 
# 
# Follow up:
# 
# Try to solve it in O(n log k) time and O(n) extra space.
# 
# 
#

# @lc code=start

# Runtime: 52 ms, faster than 83.32%
# Memory Usage: 14.1 MB, less than 99.64%
#   Time O(nlog(n))
#   Space O(n)
from heapq import heappush, heappop, heapreplace
from collections import Counter
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        freq = Counter(words)
        heap = []
        for word in freq:
            heappush(heap, (freq[word], word))

        # heap size == k, pop
        times, word = heappop(heap)
        res = []
        stack = [word]

        while heap:
            curr_freq, word = heappop(heap)

            if curr_freq == times:
                stack.append(word)
                times = curr_freq
            else:
                while stack:
                    res.append(stack.pop())
                stack.append(word)

                times = curr_freq

        while stack:
            res.append(stack.pop())
            
        return res[::-1][:k]


# Runtime: 56 ms, faster than 60.48%
# Memory Usage: 14.5 MB, less than 38.22%
#   Time O(nlog(n))
#   Space O(n)
from heapq import heappush, heappop, heapreplace
from collections import Counter

class ReverseLexiString:
    def __init__(self, string):
        self.val = string

    def __eq__(self, other):
        return self.val == other.val
        
    def __lt__(self, other):
        return self.val > other.val



class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        freq = Counter(words)
        heap = []
        for word in freq:
            heappush(heap, ((freq[word], ReverseLexiString(word)), word))
            if len(heap) > k:
                heappop(heap)

        res = []
        while heap:
            res.append(heappop(heap)[1])

        return res[::-1]
# @lc code=end

