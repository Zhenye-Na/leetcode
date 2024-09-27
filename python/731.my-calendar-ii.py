#
# @lc app=leetcode id=731 lang=python3
#
# [731] My Calendar II
#
# https://leetcode.com/problems/my-calendar-ii/description/
#
# algorithms
# Medium (55.22%)
# Likes:    1864
# Dislikes: 157
# Total Accepted:    118.1K
# Total Submissions: 206.7K
# Testcase Example:  '["MyCalendarTwo","book","book","book","book","book","book"]\n' +
#  '[[],[10,20],[50,60],[10,40],[5,15],[5,10],[25,55]]'
#
# You are implementing a program to use as your calendar. We can add a new
# event if adding the event will not cause a triple booking.
#
# A triple booking happens when three events have some non-empty intersection
# (i.e., some moment is common to all the three events.).
#
# The event can be represented as a pair of integers start and end that
# represents a booking on the half-open interval [start, end), the range of
# real numbers x such that start <= x < end.
#
# Implement the MyCalendarTwo class:
#
#
# MyCalendarTwo() Initializes the calendar object.
# boolean book(int start, int end) Returns true if the event can be added to
# the calendar successfully without causing a triple booking. Otherwise, return
# false and do not add the event to the calendar.
#
#
#
# Example 1:
#
#
# Input
# ["MyCalendarTwo", "book", "book", "book", "book", "book", "book"]
# [[], [10, 20], [50, 60], [10, 40], [5, 15], [5, 10], [25, 55]]
# Output
# [null, true, true, true, false, true, true]
#
# Explanation
# MyCalendarTwo myCalendarTwo = new MyCalendarTwo();
# myCalendarTwo.book(10, 20); // return True, The event can be booked.
# myCalendarTwo.book(50, 60); // return True, The event can be booked.
# myCalendarTwo.book(10, 40); // return True, The event can be double booked.
# myCalendarTwo.book(5, 15);  // return False, The event cannot be booked,
# because it would result in a triple booking.
# myCalendarTwo.book(5, 10); // return True, The event can be booked, as it
# does not use time 10 which is already double booked.
# myCalendarTwo.book(25, 55); // return True, The event can be booked, as the
# time in [25, 40) will be double booked with the third event, the time [40,
# 50) will be single booked, and the time [50, 55) will be double booked with
# the second event.
#
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
class MyCalendarTwo:

    def __init__(self):
        self.bookings = []
        self.overlap_bookings = []

    def book(self, start: int, end: int) -> bool:
        # Check if the new booking overlaps with any double-booked booking.
        for booking in self.overlap_bookings:
            if self.does_overlap(booking[0], booking[1], start, end):
                return False

        # Add any new double overlaps that the current booking creates.
        for booking in self.bookings:
            if self.does_overlap(booking[0], booking[1], start, end):
                self.overlap_bookings.append(
                    self.get_overlapped(booking[0], booking[1], start, end)
                )

        # Add the new booking to the list of bookings.
        self.bookings.append((start, end))
        return True

    # Return True if the booking [start1, end1) & [start2, end2) overlaps.
    def does_overlap(self, start1: int, end1: int, start2: int, end2: int) -> bool:
        return max(start1, start2) < min(end1, end2)

    # Return the overlapping booking between [start1, end1) & [start2, end2).
    def get_overlapped(self, start1: int, end1: int, start2: int, end2: int) -> tuple:
        return max(start1, start2), min(end1, end2)


class MyCalendarTwo:

    def __init__(self):
        self.bookings = []

    def book(self, start: int, end: int) -> bool:
        event = (start, end)
        self.bookings.append(event)

        count = 0
        events = []
        for booking in self.bookings:
            events.append((booking[0], 1))
            events.append((booking[1], -1))
        events.sort(key=lambda x: (x[0], x[1]))

        for _, delta in events:
            count += delta
            if count == 3:
                self.bookings.pop()
                return False

        return True


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)
# @lc code=end
