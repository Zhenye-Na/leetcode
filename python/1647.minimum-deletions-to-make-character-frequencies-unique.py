#
# @lc app=leetcode id=1647 lang=python3
#
# [1647] Minimum Deletions to Make Character Frequencies Unique
#
# https://leetcode.com/problems/minimum-deletions-to-make-character-frequencies-unique/description/
#
# algorithms
# Medium (55.79%)
# Likes:    3821
# Dislikes: 56
# Total Accepted:    194.9K
# Total Submissions: 326.9K
# Testcase Example:  '"aab"'
#
# A string s is called good if there are no two different characters in s that
# have the same frequency.
# 
# Given a string s, return the minimum number of characters you need to delete
# to make s good.
# 
# The frequency of a character in a string is the number of times it appears in
# the string. For example, in the string "aab", the frequency of 'a' is 2,
# while the frequency of 'b' is 1.
# 
# 
# Example 1:
# 
# 
# Input: s = "aab"
# Output: 0
# Explanation: s is already good.
# 
# 
# Example 2:
# 
# 
# Input: s = "aaabbbcc"
# Output: 2
# Explanation: You can delete two 'b's resulting in the good string "aaabcc".
# Another way it to delete one 'b' and one 'c' resulting in the good string
# "aaabbc".
# 
# Example 3:
# 
# 
# Input: s = "ceabaacb"
# Output: 2
# Explanation: You can delete both 'c's resulting in the good string "eabaab".
# Note that we only care about characters that are still in the string at the
# end (i.e. frequency of 0 is ignored).
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 10^5
# s contains only lowercase English letters.
# 
# 
#

# @lc code=start
from collections import Counter
from heapq import heappush, heappop

class Solution:
    def minDeletions(self, s: str) -> int:

        counts = Counter(s)
        occurences = set()

        heap = []
        for char in counts:
            heappush(heap, -counts[char])

        deletions = 0
        while heap:
            times = -heappop(heap)

            while times > 0 and times in occurences:
                times -= 1
                deletions += 1

            if times > 0:
                occurences.add(times)

        return deletions
# @lc code=end

