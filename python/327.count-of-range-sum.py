#
# @lc app=leetcode id=327 lang=python3
#
# [327] Count of Range Sum
#
# https://leetcode.com/problems/count-of-range-sum/description/
#
# algorithms
# Hard (35.94%)
# Likes:    995
# Dislikes: 116
# Total Accepted:    48.9K
# Total Submissions: 135.4K
# Testcase Example:  '[-2,5,-1]\n-2\n2'
#
# Given an integer array nums and two integers lower and upper, return the
# number of range sums that lie in [lower, upper] inclusive.
# 
# Range sum S(i, j) is defined as the sum of the elements in nums between
# indices i and j inclusive, where i <= j.
# 
# 
# Example 1:
# 
# 
# Input: nums = [-2,5,-1], lower = -2, upper = 2
# Output: 3
# Explanation: The three ranges are: [0,0], [2,2], and [0,2] and their
# respective sums are: -2, -1, 2.
# 
# 
# Example 2:
# 
# 
# Input: nums = [0], lower = 0, upper = 0
# Output: 1
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 10^4
# -2^31 <= nums[i] <= 2^31 - 1
# -3 * 10^4 <= lower <= upper <= 3 * 10^4
# 
# 
# 
# Follow up: A naive algorithm of O(n^2) is trivial, Could you do better than
# that?
#

# @lc code=start
class Solution:

    def __init__(self):
        self.prefix_sum = [0]
        self.count = 0

    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        running_sum = 0
        for i in range(len(nums)):
            running_sum += nums[i]
            self.prefix_sum.append(running_sum)

        self.helper(0, len(nums), lower, upper)
        return self.count


    def helper(self, start, end, lower, upper):
        # sum(i, j) in [lower, upper]
        # prefix_sum[j] - prefix_sum[i] >= lower
        # prefix_sum[j] - prefix_sum[i] <= upper
        # prefix_sum[j] >= prefix_sum[i] + lower
        # prefix_sum[j] <= prefix_sum[i] + upper

        if start >= end:
            return

        mid = start + (end - start) // 2
        self.helper(start, mid, lower, upper)
        self.helper(mid + 1, end, lower, upper)

        for i in range(start, mid + 1):
            left = bisect_left(self.prefix_sum[mid + 1: end + 1], self.prefix_sum[i] + lower)
            right = bisect_right(self.prefix_sum[mid + 1: end + 1], self.prefix_sum[i] + upper)
            self.count += right - left

        # merge sort
        i, j = start, mid + 1
        tmp = []
        while i <= mid and j <= end:
            if self.prefix_sum[i] <= self.prefix_sum[j]:
                tmp.append(self.prefix_sum[i])
                i += 1
            else:
                tmp.append(self.prefix_sum[j])
                j += 1

        if i <= mid:
            tmp.extend(self.prefix_sum[i:])
        if j <= end:
            tmp.extend(self.prefix_sum[j:])
        
        for i in range(end - start + 1):
            self.prefix_sum[start + i] = tmp[i]

# @lc code=end

