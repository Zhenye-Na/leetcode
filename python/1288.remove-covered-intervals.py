#
# @lc app=leetcode id=1288 lang=python3
#
# [1288] Remove Covered Intervals
#
# https://leetcode.com/problems/remove-covered-intervals/description/
#
# algorithms
# Medium (57.22%)
# Likes:    640
# Dislikes: 26
# Total Accepted:    46.4K
# Total Submissions: 80.7K
# Testcase Example:  '[[1,4],[3,6],[2,8]]'
#
# Given a list of intervals, remove all intervals that are covered by another
# interval in the list.
# 
# Interval [a,b) is covered by interval [c,d) if and only if c <= a and b <=
# d.
# 
# After doing so, return the number of remaining intervals.
# 
# 
# Example 1:
# 
# 
# Input: intervals = [[1,4],[3,6],[2,8]]
# Output: 2
# Explanation: Interval [3,6] is covered by [2,8], therefore it is removed.
# 
# 
# Example 2:
# 
# 
# Input: intervals = [[1,4],[2,3]]
# Output: 1
# 
# 
# Example 3:
# 
# 
# Input: intervals = [[0,10],[5,12]]
# Output: 2
# 
# 
# Example 4:
# 
# 
# Input: intervals = [[3,10],[4,10],[5,11]]
# Output: 2
# 
# 
# Example 5:
# 
# 
# Input: intervals = [[1,2],[1,4],[3,4]]
# Output: 1
# 
# 
# 
# Constraints:
# 
# 
# 1 <= intervals.length <= 1000
# intervals[i].length == 2
# 0 <= intervals[i][0] < intervals[i][1] <= 10^5
# All the intervals are unique.
# 
#

# @lc code=start
class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals or len(intervals) == 0:
            return 0

        length = len(intervals)
        intervals.sort(key=lambda x: (x[0], -x[1]))
        count = 0

        left, right = intervals[0][0], intervals[0][1]
        for i in range(1, length):
            if left <= intervals[i][0] and intervals[i][1] <= right:
                count += 1
            elif right >= intervals[i][0] and right <= intervals[i][1]:
                right = max(right, intervals[i][1])
            else:
                left, right = intervals[i][0], intervals[i][1]

        return length - count


    def removeCoveredIntervals_Solution2(self, intervals: List[List[int]]) -> int:
        if not intervals or len(intervals) == 0:
            return 0

        intervals.sort(key=lambda x: (x[0], -x[1]))
        res = []
        for interval in intervals:
            if not res:
                res.append(interval)
            else:
                if interval[0] >= res[-1][0] and interval[1] <= res[-1][1]:
                    continue
                else:
                    res.append(interval)

        return len(res)
# @lc code=end

