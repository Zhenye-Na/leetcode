#
# @lc app=leetcode id=560 lang=python3
#
# [560] Subarray Sum Equals K
#
# https://leetcode.com/problems/subarray-sum-equals-k/description/
#
# algorithms
# Medium (43.69%)
# Likes:    8130
# Dislikes: 273
# Total Accepted:    517.6K
# Total Submissions: 1.2M
# Testcase Example:  '[1,1,1]\n2'
#
# Given an array of integers nums and an integer k, return the total number of
# continuous subarrays whose sum equals to k.
# 
# 
# Example 1:
# Input: nums = [1,1,1], k = 2
# Output: 2
# Example 2:
# Input: nums = [1,2,3], k = 3
# Output: 2
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 2 * 10^4
# -1000 <= nums[i] <= 1000
# -10^7 <= k <= 10^7
# 
# 
#

# @lc code=start
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum = [0]
        for num in nums:
            prefix_sum.append(prefix_sum[-1] + num)

        prefix_sum_count = {}
        res = 0

        for i in range(len(prefix_sum)):
            if prefix_sum[i] - k in prefix_sum_count:
                res += prefix_sum_count[prefix_sum[i] - k]
            prefix_sum_count[prefix_sum[i]] = prefix_sum_count.get(prefix_sum[i], 0) + 1

        return res
# @lc code=end

