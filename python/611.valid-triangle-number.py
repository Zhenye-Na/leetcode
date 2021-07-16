#
# @lc app=leetcode id=611 lang=python3
#
# [611] Valid Triangle Number
#
# https://leetcode.com/problems/valid-triangle-number/description/
#
# algorithms
# Medium (49.73%)
# Likes:    1857
# Dislikes: 129
# Total Accepted:    109.5K
# Total Submissions: 222.7K
# Testcase Example:  '[2,2,3,4]'
#
# Given an integer array nums, return the number of triplets chosen from the
# array that can make triangles if we take them as side lengths of a
# triangle.
# 
# 
# Example 1:
# 
# 
# Input: nums = [2,2,3,4]
# Output: 3
# Explanation: Valid combinations are: 
# 2,3,4 (using the first 2)
# 2,3,4 (using the second 2)
# 2,2,3
# 
# 
# Example 2:
# 
# 
# Input: nums = [4,2,3,4]
# Output: 4
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 1000
# 0 <= nums[i] <= 1000
# 
# 
#

# @lc code=start
class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        if not nums or len(nums) <= 2:
            return 0

        nums.sort()
        count = 0
        
        for i in range(len(nums) - 1, 1, -1):
            delta = self.two_sum_greater(nums, 0, i - 1, nums[i])
            count += delta
        
        return count
        
    def two_sum_greater(self, nums, start, end, target):
        delta = 0
        while start <= end:
            if nums[start] + nums[end] > target:
                delta += end - start
                end -= 1
            else:
                start += 1

        return delta


    # solve using DFS, print out all possible combination
    def triangleNumber_DFS(self, nums: List[int]) -> int:
        if not nums or len(nums) < 3:
            return 0
        
        self.ret = 0
        self.tmp = []
        self.used = [False for _ in range(len(nums))]
        nums.sort()
        self._dfs(nums, 0, [])
        
        # print(self.tmp)

        return self.ret

    def _dfs(self, nums, start, curr):
        if len(curr) > 3:
            return
        
        if len(curr) == 3:
            if curr[0] + curr[1] > curr[2]:
                self.ret += 1
                self.tmp.append(curr[:])
                return
        
        
        for i in range(start, len(nums)):
        
            self.used[i] = True
            curr.append(nums[i])
            self._dfs(nums, i + 1, curr)
            curr.pop()
            self.used[i] = False
# @lc code=end

