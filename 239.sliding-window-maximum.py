#
# @lc app=leetcode id=239 lang=python3
#
# [239] Sliding Window Maximum
#
# https://leetcode.com/problems/sliding-window-maximum/description/
#
# algorithms
# Hard (44.56%)
# Likes:    5308
# Dislikes: 219
# Total Accepted:    373.2K
# Total Submissions: 835.8K
# Testcase Example:  '[1,3,-1,-3,5,3,6,7]\n3'
#
# You are given an array of integers nums, there is a sliding window of size k
# which is moving from the very left of the array to the very right. You can
# only see the k numbers in the window. Each time the sliding window moves
# right by one position.
# 
# Return the max sliding window.
# 
# 
# Example 1:
# 
# 
# Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
# Output: [3,3,5,5,6,7]
# Explanation: 
# Window position                Max
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
# ⁠1 [3  -1  -3] 5  3  6  7       3
# ⁠1  3 [-1  -3  5] 3  6  7       5
# ⁠1  3  -1 [-3  5  3] 6  7       5
# ⁠1  3  -1  -3 [5  3  6] 7       6
# ⁠1  3  -1  -3  5 [3  6  7]      7
# 
# 
# Example 2:
# 
# 
# Input: nums = [1], k = 1
# Output: [1]
# 
# 
# Example 3:
# 
# 
# Input: nums = [1,-1], k = 1
# Output: [1,-1]
# 
# 
# Example 4:
# 
# 
# Input: nums = [9,11], k = 2
# Output: [11]
# 
# 
# Example 5:
# 
# 
# Input: nums = [4,-2], k = 2
# Output: [4]
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 10^5
# -10^4 <= nums[i] <= 10^4
# 1 <= k <= nums.length
# 
# 
#

# @lc code=start
from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        max_queue = deque([])
        res = []
        for i in range(len(nums)):

            while len(max_queue) > 0 and nums[max_queue[-1]] <= nums[i]:
                # pop the smaller number, since these number will never be the maximum
                max_queue.pop()

            max_queue.append(i)

            if i >= k - 1:
                # add max to result
                res.append(nums[max_queue[0]])

            if i >= max_queue[0] + k - 1:
                # current max is out of range, need to be removed from window
                max_queue.popleft()

        return res

# @lc code=end

