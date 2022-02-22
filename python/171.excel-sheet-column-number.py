#
# @lc app=leetcode id=171 lang=python3
#
# [171] Excel Sheet Column Number
#
# https://leetcode.com/problems/excel-sheet-column-number/description/
#
# algorithms
# Easy (57.86%)
# Likes:    2586
# Dislikes: 244
# Total Accepted:    450.9K
# Total Submissions: 758.3K
# Testcase Example:  '"A"'
#
# Given a string columnTitle that represents the column title as appear in an
# Excel sheet, return its corresponding column number.
# 
# For example:
# 
# 
# A -> 1
# B -> 2
# C -> 3
# ...
# Z -> 26
# AA -> 27
# AB -> 28 
# ...
# 
# 
# 
# Example 1:
# 
# 
# Input: columnTitle = "A"
# Output: 1
# 
# 
# Example 2:
# 
# 
# Input: columnTitle = "AB"
# Output: 28
# 
# 
# Example 3:
# 
# 
# Input: columnTitle = "ZY"
# Output: 701
# 
# 
# 
# Constraints:
# 
# 
# 1 <= columnTitle.length <= 7
# columnTitle consists only of uppercase English letters.
# columnTitle is in the range ["A", "FXSHRXW"].
# 
# 
#

# @lc code=start
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        res = 0
        for col in columnTitle:
            res = res * 26 + (ord(col) - ord("A") + 1)
        return res
# @lc code=end

