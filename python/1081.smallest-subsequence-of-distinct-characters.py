#
# @lc app=leetcode id=1081 lang=python3
#
# [1081] Smallest Subsequence of Distinct Characters
#
# https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/description/
#
# algorithms
# Medium (53.86%)
# Likes:    2350
# Dislikes: 174
# Total Accepted:    55.3K
# Total Submissions: 94.2K
# Testcase Example:  '"bcabc"'
#
# Given a string s, return the lexicographically smallest subsequence of s that
# contains all the distinct characters of s exactly once.
# 
# 
# Example 1:
# 
# 
# Input: s = "bcabc"
# Output: "abc"
# 
# 
# Example 2:
# 
# 
# Input: s = "cbacdcbc"
# Output: "acdb"
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 1000
# s consists of lowercase English letters.
# 
# 
# 
# Note: This question is the same as 316:
# https://leetcode.com/problems/remove-duplicate-letters/
#

# @lc code=start
class Solution:
    def smallestSubsequence(self, s: str) -> str:
        counter = Counter(s)
        stack = []
        for letter in s:
            if len(stack) == 0:
                stack.append(letter)
            else:
                if letter in stack:
                    counter[letter] -= 1
                    continue

                while len(stack) > 0 and stack[-1] > letter:

                    if counter[stack[-1]] <= 1:
                        break
                    counter[stack[-1]] -= 1
                    stack.pop()

                stack.append(letter)

        return "".join(stack)
# @lc code=end

