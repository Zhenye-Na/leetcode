# Max Consecutive Ones II

# Description

# Given a binary array, find the maximum number of consecutive 1s in this array
# if you can flip at most one 0.

# The input array will only contain 0 and 1.
# The length of input array is a positive integer and will not exceed 10,000.

# Example

# Example 1:
#     Input:  nums = [1,0,1,1,0]
#     Output:  4
    
#     Explanation:
#     Flip the first zero will get the the maximum number of consecutive 1s.
#     After flipping, the maximum number of consecutive 1s is 4.

# Example 2:
#     Input: nums = [1,0,1,0,1]
#     Output:  3
    
#     Explanation:
#     Flip each zero will get the the maximum number of consecutive 1s.
#     After flipping, the maximum number of consecutive 1s is 3.


class Solution:
    """
    @param nums: a list of integer
    @return: return a integer, denote the maximum number of consecutive 1s
    """
    def findMaxConsecutiveOnes(self, nums):
        # write your code here
        if not nums or len(nums) == 0:
            return 0

        n = len(nums)

        # initialization
        # f[i][0] do not flip the current number, longest end with nums[i]
        # f[i][1] flip the current number, longest end with nums[i]
        f = [[0 for _ in range(2)] for _ in range(n)]
        if nums[0] == 1:
            f[0][0], f[0][1] = 1, 1
        else:
            f[0][0], f[0][1] = 0, 1

        for i in range(1, n):
            if nums[i] == 1:
                f[i][0] = f[i - 1][0] + 1
                f[i][1] = f[i - 1][1] + 1
            else:
                f[i][1] = f[i - 1][0] + 1
                f[i][0] = 0

        return max([max(_f) for _f in f])

