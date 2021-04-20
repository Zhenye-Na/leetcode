#
# @lc app=leetcode id=307 lang=python3
#
# [307] Range Sum Query - Mutable
#
# https://leetcode.com/problems/range-sum-query-mutable/description/
#
# algorithms
# Medium (36.56%)
# Likes:    1734
# Dislikes: 103
# Total Accepted:    131.5K
# Total Submissions: 357.2K
# Testcase Example:  '["NumArray","sumRange","update","sumRange"]\n[[[1,3,5]],[0,2],[1,2],[0,2]]'
#
# Given an array nums and two types of queries where you should update the
# value of an index in the array, and retrieve the sum of a range in the
# array.
# 
# Implement the NumArray class:
# 
# 
# NumArray(int[] nums) initializes the object with the integer array nums.
# void update(int index, int val) updates the value of nums[index] to be
# val.
# int sumRange(int left, int right) returns the sum of the subarray nums[left,
# right] (i.e., nums[left] + nums[left + 1], ..., nums[right]).
# 
# 
# 
# Example 1:
# 
# 
# Input
# ["NumArray", "sumRange", "update", "sumRange"]
# [[[1, 3, 5]], [0, 2], [1, 2], [0, 2]]
# Output
# [null, 9, null, 8]
# 
# Explanation
# NumArray numArray = new NumArray([1, 3, 5]);
# numArray.sumRange(0, 2); // return 9 = sum([1,3,5])
# numArray.update(1, 2);   // nums = [1,2,5]
# numArray.sumRange(0, 2); // return 8 = sum([1,2,5])
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 3 * 10^4
# -100 <= nums[i] <= 100
# 0 <= index < nums.length
# -100 <= val <= 100
# 0 <= left <= right < nums.length
# At most 3 * 10^4 calls will be made to update and sumRange.
# 
# 
#

# @lc code=start

# Binary Indexed Tree
#   https://www.youtube.com/watch?v=CWDQJGaN1gY&ab_channel=TusharRoy-CodingMadeSimple

# O(nlogn) time to construct Binary Indexed Tree
# O(logn) to compute range summation
class NumArray:

    def __init__(self, nums: List[int]):
        self.binary_indexed_tree = [0 for _ in range(len(nums) + 1)]
        for i in range(len(nums)):
            self.update(i, nums[i], True)
        self.nums = nums


    def update(self, idx: int, val: int, init=False) -> None:
        if not init:
            val, self.nums[idx] = val - self.nums[idx], val

        idx += 1
        while idx < len(self.binary_indexed_tree):
            self.binary_indexed_tree[idx] += val
            idx = self._get_next(idx)


    def sumRange(self, left: int, right: int) -> int:
        left_sum, right_sum = self._get_sum(left - 1), self._get_sum(right)
        return right_sum - left_sum


    def _get_sum(self, idx):
        idx += 1
        curr_sum = 0
        while idx > 0:
            curr_sum += self.binary_indexed_tree[idx]
            idx = self._get_parent(idx)

        return curr_sum


    def _get_next(self, idx):
        return idx + (idx & -idx)


    def _get_parent(self, idx):
        return idx - (idx & -idx)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)
# @lc code=end

