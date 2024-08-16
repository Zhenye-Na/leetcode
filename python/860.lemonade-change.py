#
# @lc app=leetcode id=860 lang=python3
#
# [860] Lemonade Change
#
# https://leetcode.com/problems/lemonade-change/description/
#
# algorithms
# Easy (53.02%)
# Likes:    2506
# Dislikes: 169
# Total Accepted:    238.3K
# Total Submissions: 432.5K
# Testcase Example:  '[5,5,5,10,20]'
#
# At a lemonade stand, each lemonade costs $5. Customers are standing in a
# queue to buy from you and order one at a time (in the order specified by
# bills). Each customer will only buy one lemonade and pay with either a $5,
# $10, or $20 bill. You must provide the correct change to each customer so
# that the net transaction is that the customer pays $5.
#
# Note that you do not have any change in hand at first.
#
# Given an integer array bills where bills[i] is the bill the i^th customer
# pays, return true if you can provide every customer with the correct change,
# or false otherwise.
#
#
# Example 1:
#
#
# Input: bills = [5,5,5,10,20]
# Output: true
# Explanation:
# From the first 3 customers, we collect three $5 bills in order.
# From the fourth customer, we collect a $10 bill and give back a $5.
# From the fifth customer, we give a $10 bill and a $5 bill.
# Since all customers got correct change, we output true.
#
#
# Example 2:
#
#
# Input: bills = [5,5,10,10,20]
# Output: false
# Explanation:
# From the first two customers in order, we collect two $5 bills.
# For the next two customers in order, we collect a $10 bill and give back a $5
# bill.
# For the last customer, we can not give the change of $15 back because we only
# have two $10 bills.
# Since not every customer received the correct change, the answer is
# false.
#
#
#
# Constraints:
#
#
# 1 <= bills.length <= 10^5
# bills[i] is either 5, 10, or 20.
#
#
#


# @lc code=start
from collections import defaultdict
from typing import List


class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        if bills is None or len(bills) == 0:
            return True

        if bills[0] != 5:
            return False

        changes = defaultdict(int)
        changes[5] = 1
        changes[10] = 0
        for bill in bills[1:]:
            if bill == 5:
                changes[5] += 1
            else:

                diff = bill - 5
                next_bill, changes = self._return_changes(diff, changes)
                if next_bill:
                    changes[bill] += 1
                else:
                    return False

        return True

    def _return_changes(self, diff, changes):

        num_of_ten = diff // 10

        if num_of_ten <= changes[10]:
            diff = diff - num_of_ten * 10
            changes[10] -= num_of_ten
        else:
            diff = diff - changes[10] * 10
            changes[10] = 0

        num_of_five = diff // 5
        if num_of_five <= changes[5]:
            diff = diff - num_of_five * 5
            changes[5] -= num_of_five
        else:
            diff = diff - changes[5] * 5
            changes[5] = 0

        if diff != 0:
            return False, None

        return True, changes


# @lc code=end
