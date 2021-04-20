#
# @lc app=leetcode id=1289 lang=python3
#
# [1289] Minimum Falling Path Sum II
#
# https://leetcode.com/problems/minimum-falling-path-sum-ii/description/
#
# algorithms
# Hard (62.37%)
# Likes:    355
# Dislikes: 37
# Total Accepted:    16K
# Total Submissions: 25.5K
# Testcase Example:  '[[1,2,3],[4,5,6],[7,8,9]]'
#
# Given a square grid of integers arr, a falling path with non-zero shifts is a
# choice of exactly one element from each row of arr, such that no two elements
# chosen in adjacent rows are in the same column.
# 
# Return the minimum sum of a falling path with non-zero shifts.
# 
# 
# Example 1:
# 
# 
# Input: arr = [[1,2,3],[4,5,6],[7,8,9]]
# Output: 13
# Explanation: 
# The possible falling paths are:
# [1,5,9], [1,5,7], [1,6,7], [1,6,8],
# [2,4,8], [2,4,9], [2,6,7], [2,6,8],
# [3,4,8], [3,4,9], [3,5,7], [3,5,9]
# The falling path with the smallest sum is [1,5,7], so the answer is 13.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= arr.length == arr[i].length <= 200
# -99 <= arr[i][j] <= 99
# 
# 
#

# @lc code=start
class Solution:
    def minFallingPathSum(self, arr: List[List[int]]) -> int:
        m, n = len(arr), len(arr[0])
        if m == 1:
            return arr[0][0]

        # initialization
        total = [[arr[i][j] for j in range(n)] for i in range(m)]

        total_max = sys.maxsize
        
        for i in range(1, m):
            for j in range(n):
                tmp = total_max
                for k in range(n):
                    if k != j:
                        tmp = min(tmp, total[i - 1][k] + arr[i][j])

                total[i][j] = tmp

        return min(total[-1])

# @lc code=end

