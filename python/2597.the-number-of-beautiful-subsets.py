#
# @lc app=leetcode id=2597 lang=python3
#
# [2597] The Number of Beautiful Subsets
#
# https://leetcode.com/problems/the-number-of-beautiful-subsets/description/
#
# algorithms
# Medium (30.04%)
# Likes:    688
# Dislikes: 127
# Total Accepted:    40.5K
# Total Submissions: 98.9K
# Testcase Example:  '[2,4,6]\n2'
#
# You are given an array nums of positive integers and a positive integer k.
# 
# A subset of nums is beautiful if it does not contain two integers with an
# absolute difference equal to k.
# 
# Return the number of non-empty beautiful subsets of the array nums.
# 
# A subset of nums is an array that can be obtained by deleting some (possibly
# none) elements from nums. Two subsets are different if and only if the chosen
# indices to delete are different.
# 
# 
# Example 1:
# 
# 
# Input: nums = [2,4,6], k = 2
# Output: 4
# Explanation: The beautiful subsets of the array nums are: [2], [4], [6], [2,
# 6].
# It can be proved that there are only 4 beautiful subsets in the array
# [2,4,6].
# 
# 
# Example 2:
# 
# 
# Input: nums = [1], k = 1
# Output: 1
# Explanation: The beautiful subset of the array nums is [1].
# It can be proved that there is only 1 beautiful subset in the array [1].
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 20
# 1 <= nums[i], k <= 1000
# 
# 
#

# @lc code=start
class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        self.memo = {}
        return self.dfs(nums, k, 0, ())

    def dfs(self, nums: List[int], k: int, index: int, current_subset: Tuple[int, ...]) -> int:
        # Use a sorted tuple of the current subset as the memoization key
        subset_key = tuple(sorted(current_subset))
        
        # Check if the result for this state is already computed
        if (index, subset_key) in self.memo:
            return self.memo[(index, subset_key)]
        
        # Base case: if we've processed all elements
        if index == len(nums):
            return 0
        
        # Option 1: Exclude the current element and proceed
        total_count = self.dfs(nums, k, index + 1, current_subset)
        
        # Option 2: Include the current element if it maintains the "beautiful" condition
        can_include = True
        for num in current_subset:
            if abs(num - nums[index]) == k:
                can_include = False
                break
        
        if can_include:
            new_subset = current_subset + (nums[index],)
            total_count += 1 + self.dfs(nums, k, index + 1, new_subset)
        
        # Store the result in the memo dictionary
        self.memo[(index, subset_key)] = total_count
        return total_count
# @lc code=end

