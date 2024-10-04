#
# @lc app=leetcode id=2491 lang=python3
#
# [2491] Divide Players Into Teams of Equal Skill
#
# https://leetcode.com/problems/divide-players-into-teams-of-equal-skill/description/
#
# algorithms
# Medium (58.91%)
# Likes:    492
# Dislikes: 12
# Total Accepted:    38.8K
# Total Submissions: 64.3K
# Testcase Example:  '[3,2,5,1,3,4]'
#
# You are given a positive integer array skill of even length n where skill[i]
# denotes the skill of the i^th player. Divide the players into n / 2 teams of
# size 2 such that the total skill of each team is equal.
#
# The chemistry of a team is equal to the product of the skills of the players
# on that team.
#
# Return the sum of the chemistry of all the teams, or return -1 if there is no
# way to divide the players into teams such that the total skill of each team
# is equal.
#
#
# Example 1:
#
#
# Input: skill = [3,2,5,1,3,4]
# Output: 22
# Explanation:
# Divide the players into the following teams: (1, 5), (2, 4), (3, 3), where
# each team has a total skill of 6.
# The sum of the chemistry of all the teams is: 1 * 5 + 2 * 4 + 3 * 3 = 5 + 8 +
# 9 = 22.
#
#
# Example 2:
#
#
# Input: skill = [3,4]
# Output: 12
# Explanation:
# The two players form a team with a total skill of 7.
# The chemistry of the team is 3 * 4 = 12.
#
#
# Example 3:
#
#
# Input: skill = [1,1,2,3]
# Output: -1
# Explanation:
# There is no way to divide the players into teams such that the total skill of
# each team is equal.
#
#
#
# Constraints:
#
#
# 2 <= skill.length <= 10^5
# skill.length is even.
# 1 <= skill[i] <= 1000
#
#
#


# @lc code=start
from typing import List


class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        n = len(skill)
        num_teams = n // 2

        total_skills = sum(skill)
        if total_skills % num_teams != 0:
            return -1

        target_skill = total_skills // num_teams
        skill_set = sorted(skill)
        res = 0
        left, right = 0, len(skill_set) - 1
        while left < right:
            if skill_set[left] + skill_set[right] == target_skill:
                res += skill_set[left] * skill_set[right]
                left += 1
                right -= 1
            else:
                return -1

        return res


# @lc code=end
