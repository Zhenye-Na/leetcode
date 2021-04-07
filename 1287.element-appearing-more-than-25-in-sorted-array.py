#
# @lc app=leetcode id=1287 lang=python3
#
# [1287] Element Appearing More Than 25% In Sorted Array
#
# https://leetcode.com/problems/element-appearing-more-than-25-in-sorted-array/description/
#
# algorithms
# Easy (60.17%)
# Likes:    436
# Dislikes: 30
# Total Accepted:    41.5K
# Total Submissions: 68.8K
# Testcase Example:  '[1,2,2,6,6,6,6,7,10]'
#
# Given an integer array sorted in non-decreasing order, there is exactly one
# integer in the array that occurs more than 25% of the time.
# 
# Return that integer.
# 
# 
# Example 1:
# Input: arr = [1,2,2,6,6,6,6,7,10]
# Output: 6
# 
# 
# Constraints:
# 
# 
# 1 <= arr.length <= 10^4
# 0 <= arr[i] <= 10^5
# 
#

# @lc code=start
class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        prev, curr = 0, 0
        limit = len(arr) // 4 + 1

        for i in range(1, len(arr)):
            if arr[i] > arr[i - 1]:
                prev = curr
                curr = i
            else:
                prev = curr

            if curr - prev >= limit:
                return arr[i - 1]

        # no results
        return arr[-1]
# @lc code=end

