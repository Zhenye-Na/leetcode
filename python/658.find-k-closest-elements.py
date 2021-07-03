#
# @lc app=leetcode id=658 lang=python3
#
# [658] Find K Closest Elements
#
# https://leetcode.com/problems/find-k-closest-elements/description/
#
# algorithms
# Medium (38.92%)
# Likes:    826
# Dislikes: 171
# Total Accepted:    67.5K
# Total Submissions: 173.4K
# Testcase Example:  '[1,2,3,4,5]\n4\n3'
#
# 
# Given a sorted array, two integers k and x, find the k closest elements to x
# in the array. The result should also be sorted in ascending order.
# If there is a tie, the smaller elements are always preferred.
# 
# 
# Example 1:
# 
# Input: [1,2,3,4,5], k=4, x=3
# Output: [1,2,3,4]
# 
# 
# 
# 
# Example 2:
# 
# Input: [1,2,3,4,5], k=4, x=-1
# Output: [1,2,3,4]
# 
# 
# 
# Note:
# 
# The value k is positive and will always be smaller than the length of the
# sorted array.
# ⁠Length of the given array is positive and will not exceed 10^4
# ⁠Absolute value of elements in the array and x will not exceed 10^4
# 
# 
# 
# 
# 
# 
# UPDATE (2017/9/19):
# The arr parameter had been changed to an array of integers (instead of a list
# of integers). Please reload the code definition to get the latest changes.
# 
#

# @lc code=start
from heapq import heappush, heappop, heappushpop

class Solution_Heap:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        if not arr or len(arr) < k:
            return arr
        
        heap = []
        for num in arr:

            if len(heap) < k:
                heappush(heap, (-abs(num - x), num))
            else:
                # there are k numbers in the heap
                # pop and push if meet requirements
                if -abs(num - x) > heap[0][0]:
                    heappushpop(heap, (-abs(num - x), num))

        return sorted([ele[1] for ele in heap])


import bisect
class Solution_BinarySearch:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        if not arr or len(arr) < k:
            return arr
        
        right = bisect.bisect_left(arr, x)

        if right == 0:
            return arr[:k]
        if right == len(arr):
            return arr[len(arr) - k:]

        left = right - 1
        res = []

        while len(res) < k:
            if left >= 0 and right < len(arr):
                # this if else block could be optimized
                # to remove redundancy
                # but I dont wanna

                # Ideally, just to make sure "right - left + 1 == k"
                if abs(arr[left] - x) < abs(arr[right] - x):
                    res.append(arr[left])
                    left -= 1
                elif abs(arr[left] - x) > abs(arr[right] - x):
                    res.append(arr[right])
                    right += 1
                else:
                    if arr[right] < arr[left]:
                        res.append(arr[right])
                        right += 1
                    else:
                        res.append(arr[left])
                        left -= 1
            elif left >= 0:
                res.append(arr[left])
                left -= 1
            else:
                res.append(arr[right])
                right += 1

        return sorted(res)
# @lc code=end

