#
# @lc app=leetcode id=334 lang=python3
#
# [334] Increasing Triplet Subsequence
#
# https://leetcode.com/problems/increasing-triplet-subsequence/description/
#
# algorithms
# Medium (40.62%)
# Likes:    2365
# Dislikes: 164
# Total Accepted:    197.1K
# Total Submissions: 482.7K
# Testcase Example:  '[1,2,3,4,5]'
#
# Given an integer array nums, return true if there exists a triple of indices
# (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k]. If no such
# indices exists, return false.
# 
# 
# Example 1:
# 
# 
# Input: nums = [1,2,3,4,5]
# Output: true
# Explanation: Any triplet where i < j < k is valid.
# 
# 
# Example 2:
# 
# 
# Input: nums = [5,4,3,2,1]
# Output: false
# Explanation: No triplet exists.
# 
# 
# Example 3:
# 
# 
# Input: nums = [2,1,5,0,4,6]
# Output: true
# Explanation: The triplet (3, 4, 5) is valid because nums[3] == 0 < nums[4] ==
# 4 < nums[5] == 6.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 10^5
# -2^31 <= nums[i] <= 2^31 - 1
# 
# 
# 
# Follow up: Could you implement a solution that runs in O(n) time complexity
# and O(1) space complexity?
#

# @lc code=start

# Time O(n): 52 ms
# Space O(n): 15.1 MB
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if not nums or len(nums) == 0:
            return False

        f, b = [nums[0]], [nums[-1]]
        n = len(nums)

        for i in range(1, n):
            f.append(min(f[-1], nums[i]))

        for j in range(n - 1, -1, -1):
            b.append(max(b[-1], nums[j]))

        # f = x x x x .. x
        # b = y y y y .. y

        for i in range(1, n - 1):
            if f[i] < nums[i] < b[n - i - 1]:
                return True

        return False


# Time O(n^2): 9868 ms
# Space O(n): 16.2 MB
class Solution_DP:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if not nums or len(nums) == 0:
            return False

        sorted_nums = sorted(
            [(num, i) for i, num in enumerate(nums)],
            key=lambda x : (x[0], x[1])
        )

        f = [1 for _ in range(len(nums))]

        # longest increasing subsequence
        for i in range(1, len(sorted_nums)):
            for j in range(0, i):
                if sorted_nums[i][0] > sorted_nums[j][0] and sorted_nums[i][1] > sorted_nums[j][1]:
                    f[i] = max(f[j] + 1, f[i])
            if f[i] >= 3:
                return True

        return False
# @lc code=end

