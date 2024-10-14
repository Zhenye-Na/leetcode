#
# @lc app=leetcode id=632 lang=python3
#
# [632] Smallest Range Covering Elements from K Lists
#
# https://leetcode.com/problems/smallest-range-covering-elements-from-k-lists/description/
#
# algorithms
# Hard (61.87%)
# Likes:    3627
# Dislikes: 80
# Total Accepted:    129.2K
# Total Submissions: 199.2K
# Testcase Example:  '[[4,10,15,24,26],[0,9,12,20],[5,18,22,30]]'
#
# You have k lists of sorted integers in non-decreasing order. Find the
# smallest range that includes at least one number from each of the k lists.
#
# We define the range [a, b] is smaller than range [c, d] if b - a < d - c or a
# < c if b - a == d - c.
#
#
# Example 1:
#
#
# Input: nums = [[4,10,15,24,26],[0,9,12,20],[5,18,22,30]]
# Output: [20,24]
# Explanation:
# List 1: [4, 10, 15, 24,26], 24 is in range [20,24].
# List 2: [0, 9, 12, 20], 20 is in range [20,24].
# List 3: [5, 18, 22, 30], 22 is in range [20,24].
#
#
# Example 2:
#
#
# Input: nums = [[1,2,3],[1,2,3],[1,2,3]]
# Output: [1,1]
#
#
#
# Constraints:
#
#
# nums.length == k
# 1 <= k <= 3500
# 1 <= nums[i].length <= 50
# -10^5 <= nums[i][j] <= 10^5
# nums[i] is sorted in non-decreasing order.
#
#
#

# @lc code=start
import heapq
from typing import List


class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        min_heap = []
        current_max = float("-inf")

        for i in range(len(nums)):
            heapq.heappush(min_heap, (nums[i][0], i, 0))
            current_max = max(current_max, nums[i][0])

        smallest_range = [float("-inf"), float("inf")]

        while len(min_heap) == len(nums):
            current_min, row, idx = heapq.heappop(min_heap)

            if (current_max - current_min < smallest_range[1] - smallest_range[0]) or (
                current_max - current_min == smallest_range[1] - smallest_range[0]
                and current_min < smallest_range[0]
            ):
                smallest_range = [current_min, current_max]

            if idx + 1 < len(nums[row]):
                next_elem = nums[row][idx + 1]
                heapq.heappush(min_heap, (next_elem, row, idx + 1))
                current_max = max(current_max, next_elem)
            else:
                break

        return smallest_range


# @lc code=end
