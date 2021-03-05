#
# @lc app=leetcode id=264 lang=python3
#
# [264] Ugly Number II
#
# https://leetcode.com/problems/ugly-number-ii/description/
#
# algorithms
# Medium (42.76%)
# Likes:    2460
# Dislikes: 155
# Total Accepted:    200.5K
# Total Submissions: 467.4K
# Testcase Example:  '10'
#
# Write a program to find the n-th ugly number.
# 
# Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. 
# 
# Example:
# 
# 
# Input: n = 10
# Output: 12
# Explanation: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10
# ugly numbers.
# 
# Note:  
# 
# 
# 1 is typically treated as an ugly number.
# n does not exceed 1690.
# 
#

# @lc code=start

from heapq import heappush, heappop
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        heap = [1]
        i = 1

        seen = set([1])
        while i < n:
            num = heappop(heap)
            for num in [num * 2, num * 3, num * 5]:
                if num not in seen:
                    heappush(heap, num)
                    seen.add(num)
            i += 1

        return heap[0]


# @lc code=end

