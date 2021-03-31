# Wiggle Sort

# Description

# Given an unsorted array nums, reorder it in-place such that

# nums[0] <= nums[1] >= nums[2] <= nums[3]....
# Please complete the problem in-place.

# Example

# Example 1:

# Input: [3, 5, 2, 1, 6, 4]
# Output: [1, 6, 2, 5, 3, 4]
# Explanation: This question may have multiple answers, and [2, 6, 1, 5, 3, 4] is also ok.

# Example 2:

# Input: [1, 2, 3, 4]
# Output: [1, 4, 2, 3]

class Solution:
    """
    @param: nums: A list of integers
    @return: nothing
    """
    def wiggleSort(self, nums):
        # write your code here
        n = len(nums)

        for i in range(n - 1):
            if i % 2 == 0 and nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
            if i % 2 != 0 and nums[i] < nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]

