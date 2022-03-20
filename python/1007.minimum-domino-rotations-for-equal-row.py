#
# @lc app=leetcode id=1007 lang=python3
#
# [1007] Minimum Domino Rotations For Equal Row
#
# https://leetcode.com/problems/minimum-domino-rotations-for-equal-row/description/
#
# algorithms
# Medium (50.94%)
# Likes:    1827
# Dislikes: 215
# Total Accepted:    149.4K
# Total Submissions: 291.3K
# Testcase Example:  '[2,1,2,4,2,2]\n[5,2,6,2,3,2]'
#
# In a row of dominoes, tops[i] and bottoms[i] represent the top and bottom
# halves of the i^th domino. (A domino is a tile with two numbers from 1 to 6 -
# one on each half of the tile.)
# 
# We may rotate the i^th domino, so that tops[i] and bottoms[i] swap values.
# 
# Return the minimum number of rotations so that all the values in tops are the
# same, or all the values in bottoms are the same.
# 
# If it cannot be done, return -1.
# 
# 
# Example 1:
# 
# 
# Input: tops = [2,1,2,4,2,2], bottoms = [5,2,6,2,3,2]
# Output: 2
# Explanation: 
# The first figure represents the dominoes as given by tops and bottoms: before
# we do any rotations.
# If we rotate the second and fourth dominoes, we can make every value in the
# top row equal to 2, as indicated by the second figure.
# 
# 
# Example 2:
# 
# 
# Input: tops = [3,5,1,2,3], bottoms = [3,6,3,3,4]
# Output: -1
# Explanation: 
# In this case, it is not possible to rotate the dominoes to make one row of
# values equal.
# 
# 
# 
# Constraints:
# 
# 
# 2 <= tops.length <= 2 * 10^4
# bottoms.length == tops.length
# 1 <= tops[i], bottoms[i] <= 6
# 
# 
#

# @lc code=start
class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        return min(
            self._get_min_moves(tops, bottoms),
            self._get_min_moves(bottoms, tops),
        )


    def _get_min_moves(self, main_array, other_array):
        counters = collections.Counter(main_array).most_common()
        min_swaps = len(main_array)

        for value, occurrences in counters:
            curr_swap = 0
            is_able = True
            for i in range(len(main_array)):
                if main_array[i] == value:
                    continue
                else:
                    if other_array[i] != value:
                        is_able = False
                        break
                    else:
                        curr_swap += 1
            if is_able:
                min_swaps = min(min_swaps, curr_swap)

        return -1 if min_swaps == len(main_array) else min_swaps

# Runtime: 1140 ms
# Memory Usage: 15.2 MB
# @lc code=end

