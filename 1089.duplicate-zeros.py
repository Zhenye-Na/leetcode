#
# @lc app=leetcode id=1089 lang=python3
#
# [1089] Duplicate Zeros
#

"""
Given a fixed length array arr of integers, duplicate each occurrence of zero, shifting the remaining elements to the right.

Note that elements beyond the length of the original array are not written.

Do the above modifications to the input array in place, do not return anything from your function.


Example 1:

Input: [1,0,2,3,0,4,5,0]
Output: null
Explanation: After calling your function, the input array is modified to: [1,0,0,2,3,0,0,4]


Example 2:

Input: [1,2,3]
Output: null
Explanation: After calling your function, the input array is modified to: [1,2,3]


Note:

1 <= arr.length <= 10000
0 <= arr[i] <= 9
"""

class Solution(object):
    def duplicateZeros(self, arr):
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """
        if not arr or len(arr) == 0:
            return

        dup = None
        for i in range(len(arr)):
            if dup:
                dup = False
                continue
            
            if arr[i] == 0:
                arr.insert(i, 0)
                dup = True
                arr.pop()
