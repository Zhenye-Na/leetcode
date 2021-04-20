# 163 Missing Ranges

# Given a sorted integer array where the range of elements are in the
# inclusive range [lower, upper], return its missing ranges.


# Example 1

# Input:
# nums = [0, 1, 3, 50, 75], lower = 0 and upper = 99
# Output:
# ["2", "4->49", "51->74", "76->99"]
# Explanation:
# in range[0,99],the missing range includes:range[2,2],range[4,49],range[51,74] and range[76,99]


# Example 2

# Input:
# nums = [0, 1, 2, 3, 7], lower = 0 and upper = 7
# Output:
# ["4->6"]
# Explanation:
# in range[0,7],the missing range include range[4,6]


from collections import deque

class Solution:
    """
    @param: nums: a sorted integer array
    @param: lower: An integer
    @param: upper: An integer
    @return: a list of its missing ranges
    """
    def findMissingRanges(self, nums, lower, upper):
        # write your code here
        if not nums or len(nums) == 0:
            return ["->".join([str(lower), str(upper)])] if lower != upper else [str(lower)]

        if nums[0] > lower:
            nums = [lower - 1] + nums
        else:
            nums = deque(nums)
            while nums and nums[0] < lower:
                nums.popleft()
            nums = [lower - 1] + list(nums)

        if nums[-1] < upper:
            nums.append(upper + 1)

        res = []
        for i in range(1, len(nums)):
            if nums[i - 1] == nums[i]:
                continue

            if nums[i - 1] + 1 != nums[i]:
                curr_range = [str(nums[i - 1] + 1), str(nums[i] - 1)] if nums[i - 1] + 1 != nums[i] - 1 else [str(nums[i - 1] + 1)]
                if len(curr_range) > 1:
                    res.append("->".join(curr_range))
                else:
                    res.append(str(nums[i - 1] + 1))

        return res
