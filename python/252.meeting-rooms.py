# 252. Meeting Rooms

# Description
# Given an array of meeting time intervals consisting of start and end times
# [[s1,e1],[s2,e2],...] (si < ei),
# determine if a person could attend all meetings.

# (0,8),(8,10) is not conflict at 8


# Example

# Example1

# Input: intervals = [(0,30),(5,10),(15,20)]
# Output: false
# Explanation: 
# (0,30), (5,10) and (0,30),(15,20) will conflict

# Example2

# Input: intervals = [(5,8),(9,15)]
# Output: true
# Explanation: 
# Two times will not conflict 

"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: if a person could attend all meetings
    """
    def canAttendMeetings(self, intervals):
        # Write your code here
        time_points = []
        for interval in intervals:
            time_points.append((interval.start, 1))
            time_points.append((interval.end, -1))

        time_points.sort()
        delta = 0
        for tp in time_points:
            delta += tp[1]
            if delta > 1:
                return False

        return True



