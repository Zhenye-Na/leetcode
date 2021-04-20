#
# @lc app=leetcode id=278 lang=python3
#
# [278] First Bad Version
#
# https://leetcode.com/problems/first-bad-version/description/
#
# algorithms
# Easy (37.23%)
# Likes:    2021
# Dislikes: 806
# Total Accepted:    536.1K
# Total Submissions: 1.4M
# Testcase Example:  '5\n4'
#
# You are a product manager and currently leading a team to develop a new
# product. Unfortunately, the latest version of your product fails the quality
# check. Since each version is developed based on the previous version, all the
# versions after a bad version are also bad.
# 
# Suppose you have n versions [1, 2, ..., n] and you want to find out the first
# bad one, which causes all the following ones to be bad.
# 
# You are given an API bool isBadVersion(version) which returns whether version
# is bad. Implement a function to find the first bad version. You should
# minimize the number of calls to the API.
# 
# 
# Example 1:
# 
# 
# Input: n = 5, bad = 4
# Output: 4
# Explanation:
# call isBadVersion(3) -> false
# call isBadVersion(5) -> true
# call isBadVersion(4) -> true
# Then 4 is the first bad version.
# 
# 
# Example 2:
# 
# 
# Input: n = 1, bad = 1
# Output: 1
# 
# 
# 
# Constraints:
# 
# 
# 1 <= bad <= n <= 2^31 - 1
# 
# 
#

# @lc code=start
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left, right = 1, n
        while left < right:
            middle = (left + right) // 2
            # Can not determine where the bad version is yet, need to check left part
            if isBadVersion(middle):
                right = middle
            # Bad version can only exist after the current version
            else:
                left = middle + 1
        if left != n + 1:
            return left
        return -1


# @lc code=end

