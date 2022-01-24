#
# @lc app=leetcode id=1291 lang=python3
#
# [1291] Sequential Digits
#
# https://leetcode.com/problems/sequential-digits/description/
#
# algorithms
# Medium (57.44%)
# Likes:    1422
# Dislikes: 94
# Total Accepted:    69.5K
# Total Submissions: 114.2K
# Testcase Example:  '100\n300'
#
# An integer has sequential digits if and only if each digit in the number is
# one more than the previous digit.
# 
# Return a sorted list of all the integers in the range [low, high] inclusive
# that have sequential digits.
# 
# 
# Example 1:
# Input: low = 100, high = 300
# Output: [123,234]
# Example 2:
# Input: low = 1000, high = 13000
# Output: [1234,2345,3456,4567,5678,6789,12345]
# 
# 
# Constraints:
# 
# 
# 10 <= low <= high <= 10^9
# 
# 
#

# @lc code=start
class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        num_low, num_high = len(str(low)), len(str(high))
        res = []
        all_digits = "123456789"

        for num_digits in range(num_low, num_high + 1):
            for start in range(10 - num_digits):
                curr = all_digits[start:start + num_digits]
                if low <= int(curr) <= high:
                    res.append(curr)

        return res
# @lc code=end

