#
# @lc app=leetcode id=624 lang=python3
#
# [624] Maximum Distance in Arrays
#
# https://leetcode.com/problems/maximum-distance-in-arrays/description/
#
# algorithms
# Medium (53.12%)
# Likes:    677
# Dislikes: 44
# Total Accepted:    62.4K
# Total Submissions: 117.4K
# Testcase Example:  '[[1,2,3],[4,5],[1,2,3]]'
#
# You are given `m` arrays, where each array is sorted in ascending order.
#
# You can pick up two integers from two different arrays (each array picks one)
# and calculate the distance. We define the distance between two integers `a` and `b`
# to be their absolute difference `|a - b|`.
#
# Return the maximum distance.
#
# Example 1:
#
# Input:
# [[1,2,3],
# ⁠[4,5],
# ⁠[1,2,3]]
# Output: 4
# Explanation:
# One way to reach the maximum distance 4 is to pick 1 in the first or third
# array and pick 5 in the second array.
#
#
#
# Note:
#
# 1. Each given array will have at least 1 number. There will be at least two
# arrays in total.
# 2. The total number of the integers in all the m arrays will not exceed 10^4.
# 3. The integers in the m arrays will be in the range of [-10^4, 10^4].
#
#

# @lc code=start
from typing import List


class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        min_val = arrays[0][0]
        max_val = arrays[0][-1]
        max_distance = 0

        for i in range(1, len(arrays)):
            current_min = arrays[i][0]
            current_max = arrays[i][-1]

            max_distance = max(
                max_distance, abs(current_max - min_val), abs(max_val - current_min)
            )

            min_val = min(min_val, current_min)
            max_val = max(max_val, current_max)

        return max_distance


# @lc code=end
