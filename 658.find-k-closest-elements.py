#
# @lc app=leetcode id=658 lang=python3
#
# [658] Find K Closest Elements
#
# https://leetcode.com/problems/find-k-closest-elements/description/
#
# algorithms
# Medium (38.92%)
# Likes:    826
# Dislikes: 171
# Total Accepted:    67.5K
# Total Submissions: 173.4K
# Testcase Example:  '[1,2,3,4,5]\n4\n3'
#
# 
# Given a sorted array, two integers k and x, find the k closest elements to x
# in the array. The result should also be sorted in ascending order.
# If there is a tie, the smaller elements are always preferred.
# 
# 
# Example 1:
# 
# Input: [1,2,3,4,5], k=4, x=3
# Output: [1,2,3,4]
# 
# 
# 
# 
# Example 2:
# 
# Input: [1,2,3,4,5], k=4, x=-1
# Output: [1,2,3,4]
# 
# 
# 
# Note:
# 
# The value k is positive and will always be smaller than the length of the
# sorted array.
# ⁠Length of the given array is positive and will not exceed 10^4
# ⁠Absolute value of elements in the array and x will not exceed 10^4
# 
# 
# 
# 
# 
# 
# UPDATE (2017/9/19):
# The arr parameter had been changed to an array of integers (instead of a list
# of integers). Please reload the code definition to get the latest changes.
# 
#

# @lc code=start
from heapq import heappush, heappop

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        if not arr or len(arr) == 0:
            return sorted(arr)

        results = []
        for point in arr:
            if len(results) < k:
                heappush(results, (- abs(point - x), point))
            else:
                if abs(point - x) < - results[0][0] or (
                    abs(point - x) == - results[0][0] and point < results[0][1]):
                    heappop(results)
                    heappush(results, (- abs(point - x), point))

        return sorted([result[1] for result in results])
# @lc code=end

