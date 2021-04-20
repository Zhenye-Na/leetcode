#
# @lc app=leetcode id=274 lang=python3
#
# [274] H-Index
#
# https://leetcode.com/problems/h-index/description/
#
# algorithms
# Medium (34.93%)
# Likes:    450
# Dislikes: 776
# Total Accepted:    132.4K
# Total Submissions: 379.1K
# Testcase Example:  '[3,0,6,1,5]'
#
# Given an array of citations (each citation is a non-negative integer) of a
# researcher, write a function to compute the researcher's h-index.
# 
# According to the definition of h-index on Wikipedia: "A scientist has index h
# if h of his/her N papers have at least h citations each, and the other N − h
# papers have no more than h citations each."
# 
# Example:
# 
# 
# Input: citations = [3,0,6,1,5]
# Output: 3 
# Explanation: [3,0,6,1,5] means the researcher has 5 papers in total and each
# of them had 
# ⁠            received 3, 0, 6, 1, 5 citations respectively. 
# Since the researcher has 3 papers with at least 3 citations each and the
# remaining 
# two with no more than 3 citations each, her h-index is 3.
# 
# Note: If there are several possible values for h, the maximum one is taken as
# the h-index.
# 
#

# @lc code=start
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        # Binary Search
        if not citations or len(citations) == 0:
            return 0

        citations.sort()
        lo, hi = 0, len(citations)
        while lo + 1 < hi:
            mid = lo + (hi - lo) // 2
            if self.isHIndex(citations, mid):
                lo = mid
            else:
                hi = mid

        if self.isHIndex(citations, hi):
            return hi
        return lo


    def isHIndex(self, citations, mid):
        count = 0
        for citation in citations:
            if citation >= mid:
                count += 1

        return count >= mid
# @lc code=end
