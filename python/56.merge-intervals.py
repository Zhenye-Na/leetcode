#
# @lc app=leetcode id=56 lang=python3
#
# [56] Merge Intervals
#
# https://leetcode.com/problems/merge-intervals/description/
#
# algorithms
# Medium (40.76%)
# Likes:    6639
# Dislikes: 362
# Total Accepted:    825.2K
# Total Submissions: 2M
# Testcase Example:  '[[1,3],[2,6],[8,10],[15,18]]'
#
# Given an array of intervals where intervals[i] = [starti, endi], merge all
# overlapping intervals, and return an array of the non-overlapping intervals
# that cover all the intervals in the input.
# 
# 
# Example 1:
# 
# 
# Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into
# [1,6].
# 
# 
# Example 2:
# 
# 
# Input: intervals = [[1,4],[4,5]]
# Output: [[1,5]]
# Explanation: Intervals [1,4] and [4,5] are considered overlapping.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= intervals.length <= 10^4
# intervals[i].length == 2
# 0 <= starti <= endi <= 10^4
# 
# 
#

# @lc code=start
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals or len(intervals) == 0:
            return []

        sorted_intervals = sorted(intervals, key=lambda x: (x[0], x[1]))
        res = []
        for start, end in sorted_intervals:
            if len(res) == 0 or res[-1][1] < start:
                res.append([start, end])
            res[-1][1] = max(res[-1][1], end)

        return res


    def merge2(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals or len(intervals) == 0:
            return intervals
        
        intervals.sort(key=lambda x: (x[0], x[1]))
        
        merged = []
        for interval in intervals:
            if not merged or merged[-1][-1] < interval[0]:
                merged.append(interval)
            else:
                merged[-1][-1] = max(merged[-1][-1], interval[-1])
                
        return merged
# @lc code=end

