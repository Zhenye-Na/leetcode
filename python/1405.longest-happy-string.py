#
# @lc app=leetcode id=1405 lang=python3
#
# [1405] Longest Happy String
#
# https://leetcode.com/problems/longest-happy-string/description/
#
# algorithms
# Medium (57.52%)
# Likes:    2045
# Dislikes: 252
# Total Accepted:    89.1K
# Total Submissions: 154.6K
# Testcase Example:  '1\n1\n7'
#
# A string s is called happy if it satisfies the following conditions:
#
#
# s only contains the letters 'a', 'b', and 'c'.
# s does not contain any of "aaa", "bbb", or "ccc" as a substring.
# s contains at most a occurrences of the letter 'a'.
# s contains at most b occurrences of the letter 'b'.
# s contains at most c occurrences of the letter 'c'.
#
#
# Given three integers a, b, and c, return the longest possible happy string.
# If there are multiple longest happy strings, return any of them. If there is
# no such string, return the empty string "".
#
# A substring is a contiguous sequence of characters within a string.
#
#
# Example 1:
#
#
# Input: a = 1, b = 1, c = 7
# Output: "ccaccbcc"
# Explanation: "ccbccacc" would also be a correct answer.
#
#
# Example 2:
#
#
# Input: a = 7, b = 1, c = 0
# Output: "aabaa"
# Explanation: It is the only correct answer in this case.
#
#
#
# Constraints:
#
#
# 0 <= a, b, c <= 100
# a + b + c > 0
#
#
#

# @lc code=start
from heapq import heapify, heappop, heappush


class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        heap = [(-a, "a"), (-b, "b"), (-c, "c")]
        heap = [(count, char) for count, char in heap if count != 0]
        heapify(heap)

        res = []
        while heap:
            count, char = heappop(heap)

            if len(res) >= 2 and res[-1] == res[-2] == char:
                if not heap:
                    break

                next_count, next_char = heappop(heap)
                res.append(next_char)
                next_count += 1

                if next_count < 0:
                    heappush(heap, (next_count, next_char))
                heappush(heap, (count, char))

            else:
                res.append(char)
                count += 1

                if count < 0:
                    heappush(heap, (count, char))

        return "".join(res)


# @lc code=end
