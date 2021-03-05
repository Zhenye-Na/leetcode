# 253. Meeting Rooms

# Description
# Given an array of meeting time intervals consisting of start and end times
# [[s1,e1],[s2,e2],...] (si < ei),
# find the minimum number of conference rooms required.


# Example

# Example1

# Input: intervals = [(0,30),(5,10),(15,20)]
# Output: 2
# Explanation:
# We need two meeting rooms
# room1: (0,30)
# room2: (5,10),(15,20)

# Example2

# Input: intervals = [(2,7)]
# Output: 1
# Explanation: 
# Only need one meeting room

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
    @return: the minimum number of conference rooms required
    """
    def minMeetingRooms(self, intervals):
        # Write your code here
        time_points = []
        for interval in intervals:
            time_points.append((interval.start, 1))
            time_points.append((interval.end, -1))

        time_points.sort()
        max_room, curr_room = 0, 0
        for _, delta in time_points:
            curr_room += delta
            max_room = max(max_room, curr_room)

        return max_room