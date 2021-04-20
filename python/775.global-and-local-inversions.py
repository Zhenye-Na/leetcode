#
# @lc app=leetcode id=775 lang=python3
#
# [775] Global and Local Inversions
#
# https://leetcode.com/problems/global-and-local-inversions/description/
#
# algorithms
# Medium (42.50%)
# Likes:    696
# Dislikes: 236
# Total Accepted:    40K
# Total Submissions: 88.1K
# Testcase Example:  '[0]'
#
# We have some permutation A of [0, 1, ..., N - 1], where N is the length of
# A.
# 
# The number of (global) inversions is the number of i < j with 0 <= i < j < N
# and A[i] > A[j].
# 
# The number of local inversions is the number of i with 0 <= i < N and A[i] >
# A[i+1].
# 
# Return true if and only if the number of global inversions is equal to the
# number of local inversions.
# 
# Example 1:
# 
# 
# Input: A = [1,0,2]
# Output: true
# Explanation: There is 1 global inversion, and 1 local inversion.
# 
# 
# Example 2:
# 
# 
# Input: A = [1,2,0]
# Output: false
# Explanation: There are 2 global inversions, and 1 local inversion.
# 
# 
# Note:
# 
# 
# A will be a permutation of [0, 1, ..., A.length - 1].
# A will have length in range [1, 5000].
# The time limit for this problem has been reduced.
# 
# 
#

# @lc code=start
class Solution:
    def isIdealPermutation(self, A: List[int]) -> bool:
        max_num = -1
        for i in range(len(A) - 2):
            max_num = max(max_num, A[i])
            if max_num > A[i + 2]:
                return False
        return True
# @lc code=end

