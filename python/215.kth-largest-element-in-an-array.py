#
# @lc app=leetcode id=215 lang=python3
#
# [215] Kth Largest Element in an Array
#
# https://leetcode.com/problems/kth-largest-element-in-an-array/description/
#
# algorithms
# Medium (58.10%)
# Likes:    5224
# Dislikes: 336
# Total Accepted:    841.8K
# Total Submissions: 1.4M
# Testcase Example:  '[3,2,1,5,6,4]\n2'
#
# Find the kth largest element in an unsorted array. Note that it is the kth
# largest element in the sorted order, not the kth distinct element.
# 
# Example 1:
# 
# 
# Input: [3,2,1,5,6,4] and k = 2
# Output: 5
# 
# 
# Example 2:
# 
# 
# Input: [3,2,3,1,2,4,5,5,6] and k = 4
# Output: 4
# 
# Note: 
# You may assume k is always valid, 1 ≤ k ≤ array's length.
# 
#

# @lc code=start
#
# Time Complexity: O(nlog(k))
# Space Complexity: O(k)
from heapq import heappush, heapreplace, nlargest

class Solution_Heap:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if not nums or len(nums) < k:
            return 0

        heap = []
        for num in nums:
            if len(heap) < k:
                heappush(heap, (num))
            else:
                if num > heap[0]:
                    heapreplace(heap, (num))

        return nlargest(k, heap)[-1]


# Time Complexity: O(n)
# Space Complexity: O(1)
class Solution_QuickSelect:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if not nums or len(nums) < k:
            return 0

        return self._quick_select(nums, 0, len(nums) - 1, k)

    def _quick_select(self, nums, start_index, end_index, k):

        left, right = start_index, end_index
        pivot = nums[(left + right) // 2]

        while left <= right:
            while left <= right and nums[left] > pivot:
                left += 1

            while left <= right and nums[right] < pivot:
                right -= 1

            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        if (start_index + k) - 1 <= right:
            return self._quick_select(nums, start_index, right, k)

        if (start_index + k) - 1 >= left:
            return self._quick_select(nums, left, end_index, k - (left - start_index))

        return nums[right + 1]
# @lc code=end

