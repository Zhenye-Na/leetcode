#
# @lc app=leetcode id=315 lang=python3
#
# [315] Count of Smaller Numbers After Self
#
# https://leetcode.com/problems/count-of-smaller-numbers-after-self/description/
#
# algorithms
# Hard (42.62%)
# Likes:    3220
# Dislikes: 101
# Total Accepted:    161.8K
# Total Submissions: 381K
# Testcase Example:  '[5,2,6,1]'
#
# You are given an integer array nums and you have to return a new counts
# array. The counts array has the property where counts[i] is the number of
# smaller elements to the right of nums[i].
# 
# 
# Example 1:
# 
# 
# Input: nums = [5,2,6,1]
# Output: [2,1,1,0]
# Explanation:
# To the right of 5 there are 2 smaller elements (2 and 1).
# To the right of 2 there is only 1 smaller element (1).
# To the right of 6 there is 1 smaller element (1).
# To the right of 1 there is 0 smaller element.
# 
# 
# Example 2:
# 
# 
# Input: nums = [-1]
# Output: [0]
# 
# 
# Example 3:
# 
# 
# Input: nums = [-1,-1]
# Output: [0,0]
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 10^5
# -10^4 <= nums[i] <= 10^4
# 
# 
#

# @lc code=start

# Brute Force
#   Time O(n2)
#   Space O(n)


class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:

        counts = []
        sorted_nums = []

        for number in reversed(nums):
            count = self._search_insert_position(sorted_nums, number)
            counts.append(count)

            sorted_nums.insert(count, number)

        return counts[::-1]

    def _search_insert_position(self, sorted_nums, target):
        # return the last position nums[i] < target, nums[i + 1] >= target
        # return 0 if target is the smallest or sorted_nums is empty
        if not sorted_nums or len(sorted_nums) == 0:
            return 0

        start, end = 0, len(sorted_nums) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if sorted_nums[mid] == target:
                end = mid
            elif sorted_nums[mid] < target:
                start = mid
            else:
                # sorted_nums[mid][1] > target:
                end = mid

        if sorted_nums[end] < target:
            return end + 1

        if sorted_nums[start] < target:
            return start + 1

        return 0
# @lc code=end

