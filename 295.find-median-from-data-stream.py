#
# @lc app=leetcode id=295 lang=python3
#
# [295] Find Median from Data Stream
#

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

