#
# @lc app=leetcode id=2104 lang=python3
#
# [2104] Sum of Subarray Ranges
#

# @lc code=start
class Solution_MonotonicStack:
    def subArrayRanges(self, nums: List[int]) -> int:
        res = 0

        stack = []
        min_nums = [-float('inf')] + nums + [-float('inf')]
        for idx, num in enumerate(min_nums):
            if len(stack) == 0:
                stack.append(idx)
            else:
                while stack and min_nums[stack[-1]] > num: # monotonic increasing stack
                    pos = stack.pop()
                    left = stack[-1] if stack else -1
                    res -= min_nums[pos] * (idx - pos) * (pos - left)
                stack.append(idx)


        stack = []
        max_nums = [float('inf')] + nums + [float('inf')]
        for idx, num in enumerate(max_nums):
            if len(stack) == 0:
                stack.append(idx)
            else:
                while stack and max_nums[stack[-1]] < num: # monotonic decreasing stack
                    pos = stack.pop()
                    left = stack[-1] if stack else -1
                    res += max_nums[pos] * (idx - pos) * (pos - left)
                stack.append(idx)

        return res

class Solution_On2:
    def subArrayRanges(self, nums: List[int]) -> int:
        
        n = len(nums)
        total = 0
        for left in range(n):

            min_val, max_val = math.inf, -math.inf
            for right in range(left, n):
                
                min_val = min(min_val, nums[right])
                max_val = max(max_val, nums[right])

                total += (max_val - min_val)

        return total
# @lc code=end

