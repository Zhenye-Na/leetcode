#
# @lc app=leetcode id=1282 lang=python3
#
# [1282] Group the People Given the Group Size They Belong To
#
# https://leetcode.com/problems/group-the-people-given-the-group-size-they-belong-to/description/
#
# algorithms
# Medium (84.63%)
# Likes:    1826
# Dislikes: 570
# Total Accepted:    119K
# Total Submissions: 138.2K
# Testcase Example:  '[3,3,3,3,3,1,3]'
#
# There are n people that are split into some unknown number of groups. Each
# person is labeled with a unique ID from 0 to n - 1.
# 
# You are given an integer array groupSizes, where groupSizes[i] is the size of
# the group that person i is in. For example, if groupSizes[1] = 3, then person
# 1 must be in a group of size 3.
# 
# Return a list of groups such that each person i is in a group of size
# groupSizes[i].
# 
# Each person should appear in exactly one group, and every person must be in a
# group. If there are multiple answers, return any of them. It is guaranteed
# that there will be at least one valid solution for the given input.
# 
# 
# Example 1:
# 
# 
# Input: groupSizes = [3,3,3,3,3,1,3]
# Output: [[5],[0,1,2],[3,4,6]]
# Explanation: 
# The first group is [5]. The size is 1, and groupSizes[5] = 1.
# The second group is [0,1,2]. The size is 3, and groupSizes[0] = groupSizes[1]
# = groupSizes[2] = 3.
# The third group is [3,4,6]. The size is 3, and groupSizes[3] = groupSizes[4]
# = groupSizes[6] = 3.
# Other possible solutions are [[2,1,6],[5],[0,4,3]] and
# [[5],[0,6,2],[4,3,1]].
# 
# 
# Example 2:
# 
# 
# Input: groupSizes = [2,1,3,3,3,2]
# Output: [[1],[0,5],[2,3,4]]
# 
# 
# 
# Constraints:
# 
# 
# groupSizes.length == n
# 1 <= n <= 500
# 1 <= groupSizes[i] <= n
# 
# 
#

# @lc code=start
from collections import Counter, defaultdict

class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:

        groups = Counter(groupSizes)

        mapping = defaultdict(list)
        for i, size in enumerate(groupSizes):
            mapping[size].append(i)

        res = []
        for size in groups:
            total_people = groups[size]
            sub_group_num = total_people // size

            # invalid case check
            # if total_people % size != 0:
            #     return []

            for _ in range(sub_group_num):
                group = []
                for i in range(size):
                    group.append(mapping[size].pop())

                res.append(group)

        return res

# [3,3,3,3,3,1,3]
# 3 -> 6
# 1 -> 1
# 7 person


# [2,1,3,3,3,2]
# 6 people
# 2 -> 2
# 1 -> 1
# 3 -> 3

# [2,2,1,2,3,2,2,1,2,3,3]
# 11 people
# 2 -> 6
# 3 -> 3
# 1-> 2

# @lc code=end

