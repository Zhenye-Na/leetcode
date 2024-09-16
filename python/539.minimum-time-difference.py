#
# @lc app=leetcode id=539 lang=python3
#
# [539] Minimum Time Difference
#
# https://leetcode.com/problems/minimum-time-difference/description/
#
# algorithms
# Medium (56.55%)
# Likes:    1974
# Dislikes: 273
# Total Accepted:    173.3K
# Total Submissions: 297.8K
# Testcase Example:  '["23:59","00:00"]'
#
# Given a list of 24-hour clock time points in "HH:MM" format, return the
# minimum minutes difference between any two time-points in the list.
#
# Example 1:
# Input: timePoints = ["23:59","00:00"]
# Output: 1
# Example 2:
# Input: timePoints = ["00:00","23:59","00:00"]
# Output: 0
#
#
# Constraints:
#
#
# 2 <= timePoints.length <= 2 * 10^4
# timePoints[i] is in the format "HH:MM".
#
#
#

# @lc code=start
from datetime import datetime
from typing import List


class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        date_format = "%H:%M"
        timePoints = [datetime.strptime(x, date_format) for x in timePoints]
        timePoints.sort()

        min_diff = float("inf")

        for i in range(1, len(timePoints)):
            diff = (timePoints[i] - timePoints[i - 1]).total_seconds() // 60
            min_diff = min(min_diff, diff)

        first_last_diff = (
            (timePoints[0] - timePoints[-1]).total_seconds() + 24 * 60 * 60
        ) // 60
        min_diff = min(min_diff, first_last_diff)

        return int(min_diff)


# @lc code=end
