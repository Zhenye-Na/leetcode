#
# @lc app=leetcode id=763 lang=python3
#
# [763] Partition Labels
#
# https://leetcode.com/problems/partition-labels/description/
#
# algorithms
# Medium (72.51%)
# Likes:    1323
# Dislikes: 73
# Total Accepted:    73.7K
# Total Submissions: 101.5K
# Testcase Example:  '"ababcbacadefegdehijhklij"'
#
# 
# A string S of lowercase letters is given.  We want to partition this string
# into as many parts as possible so that each letter appears in at most one
# part, and return a list of integers representing the size of these parts.
# 
# 
# Example 1:
# 
# Input: S = "ababcbacadefegdehijhklij"
# Output: [9,7,8]
# Explanation:
# The partition is "ababcbaca", "defegde", "hijhklij".
# This is a partition so that each letter appears in at most one part.
# A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it
# splits S into less parts.
# 
# 
# 
# Note:
# S will have length in range [1, 500].
# S will consist of lowercase letters ('a' to 'z') only.
# 
#

# @lc code=start
class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        last_occurences = {}
        for i in range(len(s)):
            last_occurences[s[i]] = i

        res = []
        i = 0
        while i < len(s):
            left = i
            right = last_occurences[s[i]]

            ptr = i + 1
            while ptr < right:
                right = max(right, last_occurences[s[ptr]])
                ptr += 1

            res.append(right - left + 1)
            i = right + 1

        return res
# @lc code=end

