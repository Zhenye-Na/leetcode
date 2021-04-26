#
# @lc app=leetcode id=696 lang=python3
#
# [696] Count Binary Substrings
#
# https://leetcode.com/problems/count-binary-substrings/description/
#
# algorithms
# Easy (57.29%)
# Likes:    1472
# Dislikes: 251
# Total Accepted:    70.4K
# Total Submissions: 116.8K
# Testcase Example:  '"00110"'
#
# Give a string s, count the number of non-empty (contiguous) substrings that
# have the same number of 0's and 1's, and all the 0's and all the 1's in these
# substrings are grouped consecutively. 
# 
# Substrings that occur multiple times are counted the number of times they
# occur.
# 
# Example 1:
# 
# Input: "00110011"
# Output: 6
# Explanation: There are 6 substrings that have equal number of consecutive 1's
# and 0's: "0011", "01", "1100", "10", "0011", and "01".
# Notice that some of these substrings repeat and are counted the number of
# times they occur.
# Also, "00110011" is not a valid substring because all the 0's (and 1's) are
# not grouped together.
# 
# 
# 
# Example 2:
# 
# Input: "10101"
# Output: 4
# Explanation: There are 4 substrings: "10", "01", "10", "01" that have equal
# number of consecutive 1's and 0's.
# 
# 
# 
# Note:
# s.length will be between 1 and 50,000.
# s will only consist of "0" or "1" characters.
# 
#

# @lc code=start
class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        if not s or len(s) <= 1:
            return 0

        length = len(s)
        i, j = 0, 1

        count = 0
        while i < length and j < length:
            if s[i:j + 1] == "01" or s[i:j + 1] == "10":
                prefix, suffix = s[i], s[j]
                m, n = i, j
                while m >= 0 and n < length and prefix == s[m] and suffix == s[n]:
                    m -= 1
                    n += 1
                count += (n - m - 1) // 2

            i += 1
            j += 1

        return count
# @lc code=end

