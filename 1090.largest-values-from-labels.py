#
# @lc app=leetcode id=1090 lang=python3
#
# [1090] Largest Values From Labels
#
# https://leetcode.com/problems/largest-values-from-labels/description/
#
# algorithms
# Medium (60.03%)
# Likes:    173
# Dislikes: 421
# Total Accepted:    19.4K
# Total Submissions: 32.2K
# Testcase Example:  '[5,4,3,2,1]\n[1,1,2,2,3]\n3\n1'
#
# We have a set of items: the i-th item has value values[i] and label
# labels[i].
# 
# Then, we choose a subset S of these items, such that:
# 
# 
# |S| <= num_wanted
# For every label L, the number of items in S with label L is <= use_limit.
# 
# 
# Return the largest possible sum of the subset S.
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: values = [5,4,3,2,1], labels = [1,1,2,2,3], num_wanted = 3, use_limit
# = 1
# Output: 9
# Explanation: The subset chosen is the first, third, and fifth item.
# 
# 
# 
# Example 2:
# 
# 
# Input: values = [5,4,3,2,1], labels = [1,3,3,3,2], num_wanted = 3, use_limit
# = 2
# Output: 12
# Explanation: The subset chosen is the first, second, and third item.
# 
# 
# 
# Example 3:
# 
# 
# Input: values = [9,8,8,7,6], labels = [0,0,0,1,1], num_wanted = 3, use_limit
# = 1
# Output: 16
# Explanation: The subset chosen is the first and fourth item.
# 
# 
# 
# Example 4:
# 
# 
# Input: values = [9,8,8,7,6], labels = [0,0,0,1,1], num_wanted = 3, use_limit
# = 2
# Output: 24
# Explanation: The subset chosen is the first, second, and fourth item.
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= values.length == labels.length <= 20000
# 0 <= values[i], labels[i] <= 20000
# 1 <= num_wanted, use_limit <= values.length
# 
# 
# 
# 
# 
#

# @lc code=start
import heapq
from collections import defaultdict

class Solution(object):
    def largestValsFromLabels(self, values, labels, num_wanted, use_limit):
        """
        :type values: List[int]
        :type labels: List[int]
        :type num_wanted: int
        :type use_limit: int
        :rtype: int
        """
        if not values or not labels or len(values) == 0 or len(labels) == 0:
            return 0

        total = 0
        heap = []
        for i in range(len(values)):
            heapq.heappush(heap, (- values[i], labels[i]))

        history = defaultdict(int)
        num_elem = 0
        while heap:
            elem, label = heap[0]
            elem = - elem
            num = history.get(label, 0)

            if num < use_limit and num_elem < num_wanted:
                history[label] += 1
                num_elem += 1
                total = max(total, total + elem)

            heapq.heappop(heap)
            
            if num_elem > num_wanted:
                break
            
        return total
# @lc code=end

