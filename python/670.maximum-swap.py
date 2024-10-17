#
# @lc app=leetcode id=670 lang=python3
#
# [670] Maximum Swap
#
# https://leetcode.com/problems/maximum-swap/description/
#
# algorithms
# Medium (49.15%)
# Likes:    3431
# Dislikes: 213
# Total Accepted:    274.9K
# Total Submissions: 559K
# Testcase Example:  '2736'
#
# You are given an integer num. You can swap two digits at most once to get the
# maximum valued number.
#
# Return the maximum valued number you can get.
#
#
# Example 1:
#
#
# Input: num = 2736
# Output: 7236
# Explanation: Swap the number 2 and the number 7.
#
#
# Example 2:
#
#
# Input: num = 9973
# Output: 9973
# Explanation: No swap.
#
#
#
# Constraints:
#
#
# 0 <= num <= 10^8
#
#
#


# @lc code=start
class Solution:
    def maximumSwap(self, num: int) -> int:
        num_str = list(str(num))
        last = {int(x): i for i, x in enumerate(num_str)}

        for i, x in enumerate(num_str):
            for d in range(9, int(x), -1):
                if last.get(d, -1) > i:
                    num_str[i], num_str[last[d]] = num_str[last[d]], num_str[i]

                    return int("".join(num_str))

        return num


# @lc code=end
