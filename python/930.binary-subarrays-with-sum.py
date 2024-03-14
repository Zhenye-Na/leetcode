#
# @lc app=leetcode id=930 lang=python3
#
# [930] Binary Subarrays With Sum
#
# https://leetcode.com/problems/binary-subarrays-with-sum/description/
#
# algorithms
# Medium (54.81%)
# Likes:    2844
# Dislikes: 80
# Total Accepted:    102.6K
# Total Submissions: 181.1K
# Testcase Example:  '[1,0,1,0,1]\n2'
#
# Given a binary array nums and an integer goal, return the number of non-empty
# subarrays with a sum goal.
# 
# A subarray is a contiguous part of the array.
# 
# 
# Example 1:
# 
# 
# Input: nums = [1,0,1,0,1], goal = 2
# Output: 4
# Explanation: The 4 subarrays are bolded and underlined below:
# [1,0,1,0,1]
# [1,0,1,0,1]
# [1,0,1,0,1]
# [1,0,1,0,1]
# 
# 
# Example 2:
# 
# 
# Input: nums = [0,0,0,0,0], goal = 0
# Output: 15
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 3 * 10^4
# nums[i] is either 0 or 1.
# 0 <= goal <= nums.length
# 
#

# @lc code=start
from collections import defaultdict

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        count = 0
        prefix_sum = 0
        prefix_sum_counts = defaultdict(int)

        for num in nums:
            prefix_sum += num

            if prefix_sum == goal:
                count += 1

            if prefix_sum - goal in prefix_sum_counts:
                count += prefix_sum_counts[prefix_sum - goal]
            prefix_sum_counts[prefix_sum] += 1

        return count
# @lc code=end

