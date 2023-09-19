#
# @lc app=leetcode id=287 lang=python3
#
# [287] Find the Duplicate Number
#
# https://leetcode.com/problems/find-the-duplicate-number/description/
#
# algorithms
# Medium (57.25%)
# Likes:    7041
# Dislikes: 753
# Total Accepted:    486.2K
# Total Submissions: 842K
# Testcase Example:  '[1,3,4,2,2]'
#
# Given an array of integers nums containing n + 1 integers where each integer
# is in the range [1, n] inclusive.
# 
# There is only one repeated number in nums, return this repeated number.
# 
# 
# Example 1:
# Input: nums = [1,3,4,2,2]
# Output: 2
# Example 2:
# Input: nums = [3,1,3,4,2]
# Output: 3
# Example 3:
# Input: nums = [1,1]
# Output: 1
# Example 4:
# Input: nums = [1,1,2]
# Output: 1
# 
# 
# Constraints:
# 
# 
# 2 <= n <= 3 * 10^4
# nums.length == n + 1
# 1 <= nums[i] <= n
# All the integers in nums appear only once except for precisely one integer
# which appears two or more times.
# 
# 
# 
# Follow up:
# 
# 
# How can we prove that at least one duplicate number must exist in nums?
# Can you solve the problem without modifying the array nums?
# Can you solve the problem using only constant, O(1) extra space?
# Can you solve the problem with runtime complexity less than O(n^2)?
# 
# 
#

# @lc code=start
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # inspired by https://www.youtube.com/watch?v=86co28GuZ5U&ab_channel=HuifengGuan
        n = len(nums) - 1
        nums.insert(0, 0)
        for i in range(1, (n + 1) + 1):
            while nums[i] != i and nums[i] != nums[nums[i]] and nums[i] <= n:
                tmp = nums[nums[i]]
                nums[nums[i]] = nums[i]
                nums[i] = tmp

        for i in range(1, (n + 1) + 1):
            if nums[i] != i:
                return nums[i]

        return -1


# O(nlogn) sort
# O(n) two pointers
class Solution_TwoPointers:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()

        left, right = 0, 1
        while right < len(nums):
            if nums[left] == nums[right]:
                return nums[left]

            left += 1
            right += 1


# O(nlogn) sort
# O(logn) binary search
# O(1) Space
class Solution_BinarySearch:
    def findDuplicate(self, nums: List[int]) -> int:
        if not nums or len(nums) == 0:
            return 0

        nums.sort()

        left, right = 0, len(nums) - 1
        while left + 1 < right:
            mid = left + (right - left) // 2
            if self._find_dup(nums, mid):
                return nums[mid]
            elif mid > nums[mid] - 1:
                right = mid
            else:
                left = mid

        if self._find_dup(nums, left):
                return nums[left]
        if self._find_dup(nums, right):
                return nums[right]
    
    def _find_dup(self, nums, idx):
        if idx > 0 and nums[idx] == nums[idx - 1]:
            return True
        if idx < len(nums) - 1 and nums[idx] == nums[idx + 1]:
            return True 
        return False

# O(n^2) Time
# O(1) Space
# Bit Manipulation
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] ^ nums[j] == 0:
                    return nums[i]
# @lc code=end

