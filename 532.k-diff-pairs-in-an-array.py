#
# @lc app=leetcode id=532 lang=python3
#
# [532] K-diff Pairs in an Array
#
# https://leetcode.com/problems/k-diff-pairs-in-an-array/description/
#
# algorithms
# Easy (30.26%)
# Likes:    392
# Dislikes: 888
# Total Accepted:    72.1K
# Total Submissions: 238.3K
# Testcase Example:  '[3,1,4,1,5]\n2'
#
# 
# Given an array of integers and an integer k, you need to find the number of
# unique k-diff pairs in the array. Here a k-diff pair is defined as an integer
# pair (i, j), where i and j are both numbers in the array and their absolute
# difference is k.
# 
# 
# 
# Example 1:
# 
# Input: [3, 1, 4, 1, 5], k = 2
# Output: 2
# Explanation: There are two 2-diff pairs in the array, (1, 3) and (3,
# 5).Although we have two 1s in the input, we should only return the number of
# unique pairs.
# 
# 
# 
# Example 2:
# 
# Input:[1, 2, 3, 4, 5], k = 1
# Output: 4
# Explanation: There are four 1-diff pairs in the array, (1, 2), (2, 3), (3, 4)
# and (4, 5).
# 
# 
# 
# Example 3:
# 
# Input: [1, 3, 1, 5, 4], k = 0
# Output: 1
# Explanation: There is one 0-diff pair in the array, (1, 1).
# 
# 
# 
# Note:
# 
# The pairs (i, j) and (j, i) count as the same pair.
# The length of the array won't exceed 10,000.
# All the integers in the given input belong to the range: [-1e7, 1e7].
# 
# 
#

# @lc code=start
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        nums.sort()

        if k < 0:
            return 0

        results = set([])
        left, right = 0, 1

        while right < len(nums):
            if nums[left] + k < nums[right]:
                left += 1
            elif nums[left] + k > nums[right]:
                right += 1
            else:
                # nums[left] + k == nums[right]
                if left == right:
                    right += 1
                else:
                    results.add((nums[left], nums[right]))
                    left, right = left + 1, right + 1

        return len(results)
# @lc code=end

