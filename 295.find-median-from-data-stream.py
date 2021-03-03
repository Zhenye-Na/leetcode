#
# @lc app=leetcode id=295 lang=python3
#
# [295] Find Median from Data Stream
#
# https://leetcode.com/problems/find-median-from-data-stream/description/
#
# algorithms
# Hard (46.54%)
# Likes:    3818
# Dislikes: 72
# Total Accepted:    275.6K
# Total Submissions: 586.6K
# Testcase Example:  '["MedianFinder","addNum","addNum","findMedian","addNum","findMedian"]\n' +
  '[[],[1],[2],[],[3],[]]'
#
# Median is the middle value in an ordered integer list. If the size of the
# list is even, there is no middle value. So the median is the mean of the two
# middle value.
# For example,
# 
# [2,3,4], the median is 3
# 
# [2,3], the median is (2 + 3) / 2 = 2.5
# 
# Design a data structure that supports the following two operations:
# 
# 
# void addNum(int num) - Add a integer number from the data stream to the data
# structure.
# double findMedian() - Return the median of all elements so far.
# 
# 
# 
# 
# Example:
# 
# 
# addNum(1)
# addNum(2)
# findMedian() -> 1.5
# addNum(3) 
# findMedian() -> 2
# 
# 
# 
# 
# Follow up:
# 
# 
# If all integer numbers from the stream are between 0 and 100, how would you
# optimize it?
# If 99% of all integer numbers from the stream are between 0 and 100, how
# would you optimize it?
# 
# 
#

# @lc code=start
from heapq import heappush, heappop

class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.greater = []
        self.lower = []

    def addNum(self, num: int) -> None:
        if len(self.lower) == 0 or num <= - self.lower[0]:
            heappush(self.lower, - num)
        else:
            heappush(self.greater, num)

        self._balance()


    def findMedian(self) -> float:
        if abs(len(self.greater) - len(self.lower)) == 1:
            return - self.lower[0]
        else:
            return (self.greater[0] - self.lower[0]) / 2

    def _balance(self):
        if len(self.lower) < len(self.greater):
            heappush(self.lower, - heappop(self.greater))
        if len(self.lower) > len(self.greater) + 1:
            heappush(self.greater, - heappop(self.lower))


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
# @lc code=end

