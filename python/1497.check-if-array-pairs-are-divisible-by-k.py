#
# @lc app=leetcode id=1497 lang=python3
#
# [1497] Check If Array Pairs Are Divisible by k
#
# https://leetcode.com/problems/check-if-array-pairs-are-divisible-by-k/description/
#
# algorithms
# Medium (38.59%)
# Likes:    1827
# Dislikes: 104
# Total Accepted:    66.7K
# Total Submissions: 164.3K
# Testcase Example:  '[1,2,3,4,5,10,6,7,8,9]\n5'
#
# Given an array of integers arr of even length n and an integer k.
#
# We want to divide the array into exactly n / 2 pairs such that the sum of
# each pair is divisible by k.
#
# Return true If you can find a way to do that or false otherwise.
#
#
# Example 1:
#
#
# Input: arr = [1,2,3,4,5,10,6,7,8,9], k = 5
# Output: true
# Explanation: Pairs are (1,9),(2,8),(3,7),(4,6) and (5,10).
#
#
# Example 2:
#
#
# Input: arr = [1,2,3,4,5,6], k = 7
# Output: true
# Explanation: Pairs are (1,6),(2,5) and(3,4).
#
#
# Example 3:
#
#
# Input: arr = [1,2,3,4,5,6], k = 10
# Output: false
# Explanation: You can try all possible pairs to see that there is no way to
# divide arr into 3 pairs each with sum divisible by 10.
#
#
#
# Constraints:
#
#
# arr.length == n
# 1 <= n <= 10^5
# n is even.
# -10^9 <= arr[i] <= 10^9
# 1 <= k <= 10^5
#
#
#

# @lc code=start
from collections import defaultdict
from typing import List


class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        _, rem = divmod(sum(arr), k)
        if rem != 0:
            return False

        collection = defaultdict(int)
        for num in arr:
            remainder = num % k
            if remainder < 0:
                remainder += k
            collection[remainder] += 1

        num_pairs = 0

        if collection[0] % 2 != 0:
            return False
        num_pairs += collection[0] // 2

        for i in range(1, k // 2 + 1):
            opposite = k - i
            if i == opposite:
                if collection[i] % 2 != 0:
                    return False
                num_pairs += collection[i] // 2
            else:
                if collection[i] != collection[opposite]:
                    return False
                num_pairs += collection[i]

        return True


# @lc code=end
