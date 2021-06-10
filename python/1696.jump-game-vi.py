#
# @lc app=leetcode id=1696 lang=python3
#
# [1696] Jump Game VI
#
# https://leetcode.com/problems/jump-game-vi/description/
#
# algorithms
# Medium (54.64%)
# Likes:    660
# Dislikes: 38
# Total Accepted:    24.1K
# Total Submissions: 58.1K
# Testcase Example:  '[1,-1,-2,4,-7,3]\n2'
#
# You are given a 0-indexed integer array nums and an integer k.
# 
# You are initially standing at index 0. In one move, you can jump at most k
# steps forward without going outside the boundaries of the array. That is, you
# can jump from index i to any index in the range [i + 1, min(n - 1, i + k)]
# inclusive.
# 
# You want to reach the last index of the array (index n - 1). Your score is
# the sum of all nums[j] for each index j you visited in the array.
# 
# Return the maximum score you can get.
# 
# 
# Example 1:
# 
# 
# Input: nums = [1,-1,-2,4,-7,3], k = 2
# Output: 7
# Explanation: You can choose your jumps forming the subsequence [1,-1,4,3]
# (underlined above). The sum is 7.
# 
# 
# Example 2:
# 
# 
# Input: nums = [10,-5,-2,4,0,3], k = 3
# Output: 17
# Explanation: You can choose your jumps forming the subsequence [10,4,3]
# (underlined above). The sum is 17.
# 
# 
# Example 3:
# 
# 
# Input: nums = [1,-5,-20,4,-1,3,-6,-3], k = 2
# Output: 0
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length, k <= 10^5
# -10^4 <= nums[i] <= 10^4
# 
# 
#

# @lc code=start

# Time Complexity: O(nk)
# Time Limit Exceeded
class Solution_Onk:
    def maxResult(self, nums: List[int], k: int) -> int:
        if not nums or len(nums) == 0:
            return 0
        
        n = len(nums)
        
        if k == n - 1:
            return nums[0] + nums[-1]
        
        # dp initialization
        # f[i] represents maximum score you can get from 0 index to i-th index in nums array
        f = [0 for i in range(n)]
        f[0] = nums[0]
        
        for i in range(1, n):
            start = max(i - k, 0)
            max_score = -sys.maxsize
            for j in range(start, i):
                max_score = max(
                    max_score,
                    f[j] + nums[i]
                )
                
            f[i] = max_score
        
        return f[n - 1]


# Time Complexity: O(nlogk)

from heapq import heappush, heappop

class Solution_Heap:
    def maxResult(self, nums: List[int], k: int) -> int:
        if not nums or len(nums) == 0:
            return 0
        
        n = len(nums)
        
        if k == n - 1:
            return nums[0] + nums[-1]
        
        heap = []
        res = 0

        for i in range(n):
            max_score = 0

            if heap:

                max_score, idx = heap[0]
                while idx + k < i:
                    max_score, idx = heappop(heap)

                # add the valid option back to heap
                heappush(heap, (max_score, idx))

            res = - max_score + nums[i]
            heappush(heap, (- res, i))

        return res
# @lc code=end

