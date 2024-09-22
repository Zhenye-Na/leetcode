#
# @lc app=leetcode id=440 lang=python3
#
# [440] K-th Smallest in Lexicographical Order
#
# https://leetcode.com/problems/k-th-smallest-in-lexicographical-order/description/
#
# algorithms
# Hard (31.58%)
# Likes:    898
# Dislikes: 99
# Total Accepted:    36.1K
# Total Submissions: 104.9K
# Testcase Example:  '13\n2'
#
# Given two integers n and k, return the k^th lexicographically smallest
# integer in the range [1, n].
#
#
# Example 1:
#
#
# Input: n = 13, k = 2
# Output: 10
# Explanation: The lexicographical order is [1, 10, 11, 12, 13, 2, 3, 4, 5, 6,
# 7, 8, 9], so the second smallest number is 10.
#
#
# Example 2:
#
#
# Input: n = 1, k = 1
# Output: 1
#
#
#
# Constraints:
#
#
# 1 <= k <= n <= 10^9
#
#
#


# @lc code=start
class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        curr = 1
        k -= 1

        while k > 0:
            steps = self._count_steps(curr, n)
            if steps <= k:
                curr += 1
                k -= steps
            else:
                curr *= 10
                k -= 1

        return curr

    def _count_steps(self, curr: int, n: int) -> int:
        steps = 0
        first, last = curr, curr

        while first <= n:
            steps += min(last, n) - first + 1
            first *= 10
            last = last * 10 + 9

        return steps


# @lc code=end
