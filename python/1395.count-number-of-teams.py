#
# @lc app=leetcode id=1395 lang=python3
#
# [1395] Count Number of Teams
#
# https://leetcode.com/problems/count-number-of-teams/description/
#
# algorithms
# Medium (66.33%)
# Likes:    3289
# Dislikes: 226
# Total Accepted:    210.6K
# Total Submissions: 300.5K
# Testcase Example:  '[2,5,3,4,1]'
#
# There are n soldiers standing in a line. Each soldier is assigned a unique
# rating value.
#
# You have to form a team of 3 soldiers amongst them under the following
# rules:
#
#
# Choose 3 soldiers with index (i, j, k) with rating (rating[i], rating[j],
# rating[k]).
# A team is valid if: (rating[i] < rating[j] < rating[k]) or (rating[i] >
# rating[j] > rating[k]) where (0 <= i < j < k < n).
#
#
# Return the number of teams you can form given the conditions. (soldiers can
# be part of multiple teams).
#
#
# Example 1:
#
#
# Input: rating = [2,5,3,4,1]
# Output: 3
# Explanation: We can form three teams given the conditions. (2,3,4), (5,4,1),
# (5,3,1).
#
#
# Example 2:
#
#
# Input: rating = [2,1,3]
# Output: 0
# Explanation: We can't form any team given the conditions.
#
#
# Example 3:
#
#
# Input: rating = [1,2,3,4]
# Output: 4
#
#
#
# Constraints:
#
#
# n == rating.length
# 3 <= n <= 1000
# 1 <= rating[i] <= 10^5
# All the integers in rating are unique.
#
#
#


# @lc code=start
class Solution:
    def numTeams(self, rating: List[int]) -> int:
        n = len(rating)
        if n < 3:
            return 0

        dp_increasing = [0] * n
        dp_decreasing = [0] * n

        for j in range(1, n):
            for i in range(j):
                if rating[i] < rating[j]:
                    dp_increasing[j] += 1
                elif rating[i] > rating[j]:
                    dp_decreasing[j] += 1

        result = 0
        for k in range(2, n):
            for j in range(1, k):
                if rating[j] < rating[k]:
                    result += dp_increasing[j]
                elif rating[j] > rating[k]:
                    result += dp_decreasing[j]

        return result


# @lc code=end
