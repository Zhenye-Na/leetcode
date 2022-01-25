#
# @lc app=leetcode id=941 lang=python3
#
# [941] Valid Mountain Array
#
# https://leetcode.com/problems/valid-mountain-array/description/
#
# algorithms
# Easy (32.56%)
# Likes:    1543
# Dislikes: 124
# Total Accepted:    235.6K
# Total Submissions: 717.2K
# Testcase Example:  '[2,1]'
#
# Given an array of integers arr, return true if and only if it is a valid
# mountain array.
# 
# Recall that arr is a mountain array if and only if:
# 
# 
# arr.length >= 3
# There exists some i with 0 < i < arr.length - 1 such that:
# 
# arr[0] < arr[1] < ... < arr[i - 1] < arr[i] 
# arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
# 
# 
# 
# 
# 
# Example 1:
# Input: arr = [2,1]
# Output: false
# Example 2:
# Input: arr = [3,5,5]
# Output: false
# Example 3:
# Input: arr = [0,3,2,1]
# Output: true
# 
# 
# Constraints:
# 
# 
# 1 <= arr.length <= 10^4
# 0 <= arr[i] <= 10^4
# 
# 
#

# @lc code=start
class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if not arr or len(arr) < 3:
            return False

        left = 0
        while left < len(arr) - 1 and arr[left] < arr[left + 1]:
            left += 1

        if left == 0 or left == len(arr) - 1:
            return False

        while left < len(arr) - 1 and arr[left] > arr[left + 1]:
            left += 1

        return left == len(arr) - 1
# @lc code=end

