#
# @lc app=leetcode id=1551 lang=python3
#
# [1551] Minimum Operations to Make Array Equal
#
# https://leetcode.com/problems/minimum-operations-to-make-array-equal/description/
#
# algorithms
# Medium (77.86%)
# Likes:    358
# Dislikes: 72
# Total Accepted:    36.1K
# Total Submissions: 44.9K
# Testcase Example:  '3'
#
# You have an array arr of length n where arr[i] = (2 * i) + 1 for all valid
# values of i (i.e. 0 <= i < n).
# 
# In one operation, you can select two indices x and y where 0 <= x, y < n and
# subtract 1 from arr[x] and add 1 to arr[y] (i.e. perform arr[x] -=1 and
# arr[y] += 1). The goal is to make all the elements of the array equal. It is
# guaranteed that all the elements of the array can be made equal using some
# operations.
# 
# Given an integer n, the length of the array. Return the minimum number of
# operations needed to make all the elements of arr equal.
# 
# 
# Example 1:
# 
# 
# Input: n = 3
# Output: 2
# Explanation: arr = [1, 3, 5]
# First operation choose x = 2 and y = 0, this leads arr to be [2, 3, 4]
# In the second operation choose x = 2 and y = 0 again, thus arr = [3, 3, 3].
# 
# 
# Example 2:
# 
# 
# Input: n = 6
# Output: 9
# 
# 
# 
# Constraints:
# 
# 
# 1 <= n <= 10^4
# 
#

# @lc code=start
class Solution:
    def minOperations(self, n: int) -> int:
        moves = 0
        if n % 2 == 1:
            mid = n // 2
            pivot = 2 * mid + 1
            for i in range(mid + 1, n):
                moves += (2 * i + 1 - pivot)
        else:
            mid = n // 2
            pivot = ((2 * mid + 1) + (2 * (mid - 1) + 1)) // 2
            moves = 1
            for i in range(mid + 1, n):
                moves += (2 * i + 1 - pivot)

        return moves
# @lc code=end

