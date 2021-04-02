#
# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#
# https://leetcode.com/problems/top-k-frequent-elements/description/
#
# algorithms
# Medium (62.25%)
# Likes:    4564
# Dislikes: 260
# Total Accepted:    550.4K
# Total Submissions: 881.4K
# Testcase Example:  '[1,1,1,2,2,3]\n2'
#
# Given a non-empty array of integers, return the k most frequent elements.
# 
# Example 1:
# 
# 
# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]
# 
# 
# 
# Example 2:
# 
# 
# Input: nums = [1], k = 1
# Output: [1]
# 
# 
# Note: 
# 
# 
# You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
# Your algorithm's time complexity must be better than O(n log n), where n is
# the array's size.
# It's guaranteed that the answer is unique, in other words the set of the top
# k frequent elements is unique.
# You can return the answer in any order.
# 
# 
#

# @lc code=start
from heapq import heappush, heappop, heappushpop
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if not nums or len(nums) == 0:
            return []

        counts = Counter(nums)
        freq = [(counts[key], key) for key in counts]

        heap = []
        for f, num in freq:
            
            if len(heap) < k:
                heappush(heap, (f, num))
            else:
                if f > heap[0][0]:
                    heappushpop(heap, (f, num))

        res = []
        while heap:
            res.append(heappop(heap)[1])
        return res



class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if not nums or len(nums) == 0:
            return []

        freq = Counter(nums)
        heap = []

        for num in freq:
            if len(heap) < k:
                heappush(heap, (freq[num], num))
            else:
                if freq[num] > heap[0][0]:
                    heapreplace(heap, (freq[num], num))

        # size of heap will be k
        res = [pair[1] for pair in heap]
        return res
# @lc code=end


# Time: O(nlog(k)) where n represents the number of unique number, worst case is n
# Space: O(n)

