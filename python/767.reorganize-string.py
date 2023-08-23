#
# @lc app=leetcode id=767 lang=python3
#
# [767] Reorganize String
#
# https://leetcode.com/problems/reorganize-string/description/
#
# algorithms
# Medium (50.77%)
# Likes:    6437
# Dislikes: 206
# Total Accepted:    275.5K
# Total Submissions: 519K
# Testcase Example:  '"aab"'
#
# Given a string s, rearrange the characters of s so that any two adjacent
# characters are not the same.
# 
# Return any possible rearrangement of s or return "" if not possible.
# 
# 
# Example 1:
# Input: s = "aab"
# Output: "aba"
# Example 2:
# Input: s = "aaab"
# Output: ""
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 500
# s consists of lowercase English letters.
# 
# 
#

# @lc code=start
from heapq import heapify, heappop

class Solution:

    def reorganizeString(self, s: str) -> str:
        res = []
        heap = [(-count, char) for char, count in Counter(s).items()]
        heapify(heap)

        while heap:

            count, char = heappop(heap)
            if not res or res[-1] != char:
                res.append(char)
                count += 1
                if count < 0:
                    heappush(heap, (count, char))

            else:
                if not heap:
                    return ""
                
                next_count, next_char = heappop(heap)
                res.append(next_char)
                next_count += 1
                if next_count < 0:
                    heappush(heap, (next_count, next_char))
                heappush(heap, (count, char))


        return "".join(res)
# @lc code=end

