#
# @lc app=leetcode id=799 lang=python3
#
# [799] Champagne Tower
#
# https://leetcode.com/problems/champagne-tower/description/
#
# algorithms
# Medium (44.28%)
# Likes:    1298
# Dislikes: 76
# Total Accepted:    44.9K
# Total Submissions: 96.7K
# Testcase Example:  '1\n1\n1'
#
# We stack glasses in a pyramid, where the first row has 1 glass, the second
# row has 2 glasses, and so on until the 100^th row.  Each glass holds one cup
# of champagne.
# 
# Then, some champagne is poured into the first glass at the top.  When the
# topmost glass is full, any excess liquid poured will fall equally to the
# glass immediately to the left and right of it.  When those glasses become
# full, any excess champagne will fall equally to the left and right of those
# glasses, and so on.  (A glass at the bottom row has its excess champagne fall
# on the floor.)
# 
# For example, after one cup of champagne is poured, the top most glass is
# full.  After two cups of champagne are poured, the two glasses on the second
# row are half full.  After three cups of champagne are poured, those two cups
# become full - there are 3 full glasses total now.  After four cups of
# champagne are poured, the third row has the middle glass half full, and the
# two outside glasses are a quarter full, as pictured below.
# 
# 
# 
# Now after pouring some non-negative integer cups of champagne, return how
# full the j^th glass in the i^th row is (both i and j are 0-indexed.)
# 
# 
# Example 1:
# 
# 
# Input: poured = 1, query_row = 1, query_glass = 1
# Output: 0.00000
# Explanation: We poured 1 cup of champange to the top glass of the tower
# (which is indexed as (0, 0)). There will be no excess liquid so all the
# glasses under the top glass will remain empty.
# 
# 
# Example 2:
# 
# 
# Input: poured = 2, query_row = 1, query_glass = 1
# Output: 0.50000
# Explanation: We poured 2 cups of champange to the top glass of the tower
# (which is indexed as (0, 0)). There is one cup of excess liquid. The glass
# indexed as (1, 0) and the glass indexed as (1, 1) will share the excess
# liquid equally, and each will get half cup of champange.
# 
# 
# Example 3:
# 
# 
# Input: poured = 100000009, query_row = 33, query_glass = 17
# Output: 1.00000
# 
# 
# 
# Constraints:
# 
# 
# 0 <= poured <= 10^9
# 0 <= query_glass <= query_row < 100
# 
#

# @lc code=start
class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:

        # dp[i][j] represents the % of fullness of ith row, jth glass
        # left[i][j] represents how much wine is left in ith row, jth glass
        dp, left = [], []
        for row in range(query_row + 1):
            dp.append([0 for _ in range(row + 1)])
            left.append([0 for _ in range(row + 1)])

        dp[0][0] = 1 if poured >= 1 else 0
        left[0][0] = 0 if poured <= 1 else poured - 1

        for i in range(1, query_row + 1):
            dp[i][0] = 1 if left[i - 1][0] / 2 >= 1 else left[i - 1][0] / 2
            left[i][0] = 0 if dp[i][0] < 1 else left[i - 1][0] / 2 - 1

        for i in range(1, query_row + 1):
            dp[i][i] = 1 if left[i - 1][i - 1] / 2 >= 1 else left[i - 1][i - 1] / 2
            left[i][i] = 0 if dp[i][i] < 1 else left[i - 1][i - 1] / 2 - 1

        for i in range(1, query_row + 1):
            for j in range(1, len(dp[i]) - 1):
                total = left[i - 1][j - 1] / 2 + left[i - 1][j] / 2

                dp[i][j] = 1 if total >= 1 else total
                left[i][j] = total - 1 if total >= 1 else 0

        return dp[query_row][query_glass]

class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        f = [[0 for _ in range(n + 2)] for _ in range(1, n + 2)]
        delta = [[0 for _ in range(n + 2)] for _ in range(1, n + 2)]

        f[0][0] = 1 if poured >= 1 else poured
        delta[0][0] = (poured - f[0][0]) / 2

        for i in range(1, n + 1):
            for j in range(i + 1):
                if j == 0:
                    f[i][j] = 1 if delta[i - 1][j] >= 1 else delta[i - 1][j]
                    delta[i][j] = (delta[i - 1][j] - f[i][j]) / 2
                else:
                    f[i][j] = 1 if delta[i - 1][j] + delta[i - 1][j - 1] >= 1 else delta[i - 1][j] + delta[i - 1][j - 1]
                    delta[i][j] = (delta[i - 1][j] + delta[i - 1][j - 1] - f[i][j]) / 2

        return f[n][m] if f[n][m] <= 1 else 1
# @lc code=end

