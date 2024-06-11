#
# @lc app=leetcode id=1122 lang=python3
#
# [1122] Relative Sort Array
#
# https://leetcode.com/problems/relative-sort-array/description/
#
# algorithms
# Easy (68.65%)
# Likes:    3089
# Dislikes: 182
# Total Accepted:    317.3K
# Total Submissions: 426K
# Testcase Example:  '[2,3,1,3,2,4,6,7,9,2,19]\n[2,1,4,3,9,6]'
#
# Given two arrays arr1 and arr2, the elements of arr2 are distinct, and all
# elements in arr2 are also in arr1.
# 
# Sort the elements of arr1 such that the relative ordering of items in arr1
# are the same as in arr2. Elements that do not appear in arr2 should be placed
# at the end of arr1 in ascending order.
# 
# 
# Example 1:
# 
# 
# Input: arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]
# Output: [2,2,2,1,4,3,3,9,6,7,19]
# 
# 
# Example 2:
# 
# 
# Input: arr1 = [28,6,22,8,44,17], arr2 = [22,28,8,6]
# Output: [22,28,8,6,17,44]
# 
# 
# 
# Constraints:
# 
# 
# 1 <= arr1.length, arr2.length <= 1000
# 0 <= arr1[i], arr2[i] <= 1000
# All the elements of arr2 are distinct.
# Each arr2[i] is in arr1.
# 
# 
#

# @lc code=start
from collections import Counter

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        count = Counter(arr1)

        sorted_arr1 = []
        for num in arr2:
            sorted_arr1 += [num for _ in range(count[num])]
            del count[num]

        extra_nums = []
        for num in count:
            extra_nums += [num for _ in range(count[num])]
        
        extra_nums.sort()

        return sorted_arr1 + extra_nums


# Solution 2
from functools import cmp_to_key

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        position = {}
        for idx, num in enumerate(arr2):
            position[num] = idx

        def cmp_items(a, b):
            if a in position and b in position:
                if position[a] > position[b]:
                    return 1
                elif position[a] == position[b]:
                    return 0
                else:
                    return -1

            if a not in position and b not in position:
                if a > b:
                    return 1
                elif a == b:
                    return 0
                else:
                    return -1

            if a not in position:
                return 1
            else:
                return -1

        cmp_items_py3 = cmp_to_key(cmp_items)

        arr1.sort(key = cmp_items_py3)

        return arr1
# @lc code=end

