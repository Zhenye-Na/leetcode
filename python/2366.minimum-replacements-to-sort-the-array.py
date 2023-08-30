#
# @lc app=leetcode id=2366 lang=python3
#
# [2366] Minimum Replacements to Sort the Array
#
# @lc code=start
class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:

        if not nums or len(nums) == 0:
            return 0

        ops = 0
        last_num = nums[-1]
        l = len(nums) - 2
        while l >= 0:
            if nums[l] <= last_num:
                last_num = nums[l]
            else:
                # nums[l] > nums[r]
                k = nums[l] // last_num
                d = nums[l] % last_num

                # we dont need any further adjustment
                if d == 0:
                    ops += k - 1
                    l -= 1
                    continue

                # calculate value
                p = (last_num - d) // ( k + 1)
                d2 = d + p * k
                last_num -= p

                # check if we need to do adjustment
                if d2 < last_num:
                    d2 = (d2 + (k - 1) * last_num) // k

                last_num = d2
                ops += k

            l -= 1

        return ops
# @lc code=end


