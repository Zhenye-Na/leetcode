#
# @lc app=leetcode id=435 lang=python3
#
# [435] Non-overlapping Intervals
#
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
            
        intervals = sorted(intervals, key=lambda x: x[1])
        self.index = 0
        self.result = 1
        
        for i in range(1, len(intervals)):
            if intervals[i][0] >= intervals[self.index][1]:
                self.result += 1
                self.index = i

        return len(intervals) - self.result

