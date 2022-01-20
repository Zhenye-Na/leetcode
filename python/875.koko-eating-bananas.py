#
# @lc app=leetcode id=875 lang=python3
#
# [875] Koko Eating Bananas
#
# https://leetcode.com/problems/koko-eating-bananas/description/
#
# algorithms
# Medium (53.87%)
# Likes:    2776
# Dislikes: 141
# Total Accepted:    122.2K
# Total Submissions: 223.9K
# Testcase Example:  '[3,6,7,11]\n8'
#
# Koko loves to eat bananas. There are n piles of bananas, the i^th pile has
# piles[i] bananas. The guards have gone and will come back in h hours.
# 
# Koko can decide her bananas-per-hour eating speed of k. Each hour, she
# chooses some pile of bananas and eats k bananas from that pile. If the pile
# has less than k bananas, she eats all of them instead and will not eat any
# more bananas during this hour.
# 
# Koko likes to eat slowly but still wants to finish eating all the bananas
# before the guards return.
# 
# Return the minimum integer k such that she can eat all the bananas within h
# hours.
# 
# 
# Example 1:
# 
# 
# Input: piles = [3,6,7,11], h = 8
# Output: 4
# 
# 
# Example 2:
# 
# 
# Input: piles = [30,11,23,4,20], h = 5
# Output: 30
# 
# 
# Example 3:
# 
# 
# Input: piles = [30,11,23,4,20], h = 6
# Output: 23
# 
# 
# 
# Constraints:
# 
# 
# 1 <= piles.length <= 10^4
# piles.length <= h <= 10^9
# 1 <= piles[i] <= 10^9
# 
# 
#

# @lc code=start
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if not piles or len(piles) == 0:
            return 0

        low, high = 1, max(piles)
        while low + 1 < high:
            mid = (low + high) // 2
            if self._get_finish_duration(piles, mid) <= h:
                high = mid
            else:
                low = mid
        
        if self._get_finish_duration(piles, low) <= h:
            return low
        return high

    def _get_finish_duration(self, piles, k):
        duration = 0
        for pile in piles:
            duration += math.ceil(pile / k)

        return duration
# @lc code=end

