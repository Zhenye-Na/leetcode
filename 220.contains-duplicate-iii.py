#
# @lc app=leetcode id=220 lang=python3
#
# [220] Contains Duplicate III
#
# https://leetcode.com/problems/contains-duplicate-iii/description/
#
# algorithms
# Medium (21.33%)
# Likes:    1520
# Dislikes: 1607
# Total Accepted:    166.3K
# Total Submissions: 779.5K
# Testcase Example:  '[1,2,3,1]\n3\n0'
#
# Given an array of integers, find out whether there are two distinct indices i
# and j in the array such that the absolute difference between nums[i] and
# nums[j] is at most t and the absolute difference between i and j is at most
# k.
# 
# 
# Example 1:
# Input: nums = [1,2,3,1], k = 3, t = 0
# Output: true
# Example 2:
# Input: nums = [1,0,1,1], k = 1, t = 2
# Output: true
# Example 3:
# Input: nums = [1,5,9,1,5,9], k = 2, t = 3
# Output: false
# 
# 
# Constraints:
# 
# 
# 0 <= nums.length <= 2 * 10^4
# -2^31 <= nums[i] <= 2^31 - 1
# 0 <= k <= 10^4
# 0 <= t <= 2^31 - 1
# 
# 
#

# @lc code=start
from sortedcontainers import SortedSet

class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        if not nums or len(nums) == 0:
            return False

        tree_set = SortedSet()
        for i in range(len(nums)):

            ceilling_idx = tree_set.bisect_left(nums[i]) # O(log(k)) – approximate.
            flooring_idx = ceilling_idx - 1

            if ceilling_idx < len(tree_set) and tree_set[ceilling_idx] - nums[i] <= t:
                # ceilling_idx == len(tree_set) -> nums[i] is the largest number in TreeSet
                return True
            
            if flooring_idx >= 0 and nums[i] - tree_set[flooring_idx] <= t:
                # flooring_idx == 0 -> nums[i] is the smallest number in TreeSet
                return True

            tree_set.add(nums[i]) # O(log(k)) – approximate.
            if i >= k: # restrict the size of TreeSet to be `k` (window size)
                tree_set.remove(nums[i - k]) # O(log(k)) – approximate.

           
        return False


# @lc code=end

# Time: O(nlog(min(n, k)))
# Space: O(n)
