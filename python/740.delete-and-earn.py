#
# @lc app=leetcode id=740 lang=python3
#
# [740] Delete and Earn
#
# https://leetcode.com/problems/delete-and-earn/description/
#
# algorithms
# Medium (51.85%)
# Likes:    3809
# Dislikes: 229
# Total Accepted:    139.9K
# Total Submissions: 250.4K
# Testcase Example:  '[3,4,2]'
#
# You are given an integer array nums. You want to maximize the number of
# points you get by performing the following operation any number of
# times:
# 
# 
# Pick any nums[i] and delete it to earn nums[i] points. Afterwards, you must
# delete every element equal to nums[i] - 1 and every element equal to nums[i]
# + 1.
# 
# 
# Return the maximum number of points you can earn by applying the above
# operation some number of times.
# 
# 
# Example 1:
# 
# 
# Input: nums = [3,4,2]
# Output: 6
# Explanation: You can perform the following operations:
# - Delete 4 to earn 4 points. Consequently, 3 is also deleted. nums = [2].
# - Delete 2 to earn 2 points. nums = [].
# You earn a total of 6 points.
# 
# 
# Example 2:
# 
# 
# Input: nums = [2,2,3,3,3,4]
# Output: 9
# Explanation: You can perform the following operations:
# - Delete a 3 to earn 3 points. All 2's and 4's are also deleted. nums =
# [3,3].
# - Delete a 3 again to earn 3 points. nums = [3].
# - Delete a 3 once more to earn 3 points. nums = [].
# You earn a total of 9 points.
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 2 * 10^4
# 1 <= nums[i] <= 10^4
# 
# 
#

# @lc code=start
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        counts = sorted(collections.Counter(nums).items())
        f = [[0, 0] for _ in range(len(counts))]

        # 0 - selected
        # 1 - not selected
        f[0][0] = counts[0][0] * counts[0][1]

        for i in range(1, len(f)):
            if counts[i][0] == counts[i - 1][0] + 1:
                f[i][1] = f[i - 1][0]
                f[i][0] = max(f[i - 2]) + counts[i][0] * counts[i][1]
            else:
                f[i][0] = max(f[i - 1]) + counts[i][0] * counts[i][1]
                f[i][1] = max(f[i - 1])

        return max(f[-1])
# @lc code=end

