# [325] Maximum Size Subarray Sum Equals k

# Description

# Given an array nums and a target value k, find the maximum length of a
# subarray that sums to k. If there isn't one, return 0 instead.

# The sum of the entire nums array is guaranteed to fit within the 32-bit
# signed integer range.

# Example

# Example 1

# Input:  nums = [1, -1, 5, -2, 3], k = 3
# Output: 4
# Explanation:
# because the subarray [1, -1, 5, -2] sums to 3 and is the longest.


# Example 2

# Input: nums = [-2, -1, 2, 1], k = 1
# Output: 2
# Explanation:
# because the subarray [-1, 2] sums to 1 and is the longest.


# Challenge
# Can you do it in O(n) time?





class Solution:
    """
    @param nums: an array
    @param k: a target value
    @return: the maximum length of a subarray that sums to k
    """
    def maxSubArrayLen(self, nums, k):
        # Write your code here
        if not nums or len(nums) == 0:
            return 0
        
        max_len = 0
        mapping = {0: -1}
        prefix_sum = 0
        for i in range(len(nums)):
            prefix_sum += nums[i]
            if prefix_sum - k in mapping:
                max_len = max(
                    max_len,
                    i - mapping.get(prefix_sum - k)
                )

            if prefix_sum not in mapping:
                mapping[prefix_sum] = i

        return max_len





from collections import defaultdict

class Solution:
    """
    @param nums: an array
    @param k: a target value
    @return: the maximum length of a subarray that sums to k
    """
    def maxSubArrayLen(self, nums, k):
        # Write your code here
        if not nums or len(nums) == 0:
            return 0
        
        prefix_sum = [0]
        for num in nums:
            curr_sum = num + prefix_sum[-1]
            prefix_sum.append(curr_sum)

        mapping = defaultdict(list)
        for idx, pre in enumerate(prefix_sum):
            mapping[pre].append(idx)

        max_len = 0

        for idx, p_sum in enumerate(prefix_sum):
            if p_sum + k not in mapping:
                continue

            j = mapping[p_sum + k][-1]
            curr_len = j - idx
            max_len = max(max_len, curr_len)

        return max_len


