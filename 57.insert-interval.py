#
# @lc app=leetcode id=57 lang=python3
#
# [57] Insert Interval
#
# https://leetcode.com/problems/insert-interval/description/
#
# algorithms
# Medium (34.90%)
# Likes:    2637
# Dislikes: 236
# Total Accepted:    332.1K
# Total Submissions: 945.9K
# Testcase Example:  '[[1,3],[6,9]]\n[2,5]'
#
# Given a set of non-overlapping intervals, insert a new interval into the
# intervals (merge if necessary).
# 
# You may assume that the intervals were initially sorted according to their
# start times.
# 
# 
# Example 1:
# 
# 
# Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
# Output: [[1,5],[6,9]]
# 
# 
# Example 2:
# 
# 
# Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
# Output: [[1,2],[3,10],[12,16]]
# Explanation: Because the new interval [4,8] overlaps with
# [3,5],[6,7],[8,10].
# 
# Example 3:
# 
# 
# Input: intervals = [], newInterval = [5,7]
# Output: [[5,7]]
# 
# 
# Example 4:
# 
# 
# Input: intervals = [[1,5]], newInterval = [2,3]
# Output: [[1,5]]
# 
# 
# Example 5:
# 
# 
# Input: intervals = [[1,5]], newInterval = [2,7]
# Output: [[1,7]]
# 
# 
# 
# Constraints:
# 
# 
# 0 <= intervals.length <= 10^4
# intervals[i].length == 2
# 0 <= intervals[i][0] <= intervals[i][1] <= 10^5
# intervals is sorted by intervals[i][0] in ascending order.
# newInterval.length == 2
# 0 <= newInterval[0] <= newInterval[1] <= 10^5
# 
# 
#

# @lc code=start
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        return self._merge(intervals)

    def _merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals or len(intervals) == 0:
            return []

        sorted_intervals = sorted(intervals, key=lambda x: (x[0], x[1]))
        res = []
        for start, end in sorted_intervals:
            if len(res) == 0 or res[-1][1] < start:
                res.append([start, end])
            res[-1][1] = max(res[-1][1], end)

        return res
# @lc code=end

