#
# @lc app=leetcode id=729 lang=python3
#
# [729] My Calendar I
#
# https://leetcode.com/problems/my-calendar-i/description/
#
# algorithms
# Medium (54.10%)
# Likes:    1389
# Dislikes: 50
# Total Accepted:    113.2K
# Total Submissions: 209.2K
# Testcase Example:  '["MyCalendar","book","book","book"]\n[[],[10,20],[15,25],[20,30]]'
#
# You are implementing a program to use as your calendar. We can add a new
# event if adding the event will not cause a double booking.
# 
# A double booking happens when two events have some non-empty intersection
# (i.e., some moment is common to both events.).
# 
# The event can be represented as a pair of integers start and end that
# represents a booking on the half-open interval [start, end), the range of
# real numbers x such that start <= x < end.
# 
# Implement the MyCalendar class:
# 
# 
# MyCalendar() Initializes the calendar object.
# boolean book(int start, int end) Returns true if the event can be added to
# the calendar successfully without causing a double booking. Otherwise, return
# false and do not add the event to the calendar.
# 
# 
# 
# Example 1:
# 
# 
# Input
# ["MyCalendar", "book", "book", "book"]
# [[], [10, 20], [15, 25], [20, 30]]
# Output
# [null, true, false, true]
# 
# Explanation
# MyCalendar myCalendar = new MyCalendar();
# myCalendar.book(10, 20); // return True
# myCalendar.book(15, 25); // return False, It can not be booked because time
# 15 is already booked by another event.
# myCalendar.book(20, 30); // return True, The event can be booked, as the
# first event takes every time less than 20, but not including 20.
# 
# 
# Constraints:
# 
# 
# 0 <= start < end <= 10^9
# At most 1000 calls will be made to book.
# 
# 
#

# @lc code=start
class MyCalendar:

    def __init__(self):
        self.time_ranges = []


    def book(self, start: int, end: int) -> bool:
        is_overlapped = self.bianry_search(start, end)
        if not is_overlapped:
            return False

        self.time_ranges.append([start, end])
        return True


    def bianry_search(self, start, end):
        if not self.time_ranges or len(self.time_ranges) == 0:
            return True

        self.time_ranges = sorted(self.time_ranges, key=lambda x : (x[0], x[1]))

        lower_bound = bisect.bisect_left([self.time_ranges[i][0] for i in range(len(self.time_ranges))], start)

        if lower_bound != 0 and self.time_ranges[lower_bound - 1][1] > start:
            return False

        if lower_bound < len(self.time_ranges) and self.time_ranges[lower_bound][0] < end:
            return False

        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
# @lc code=end

