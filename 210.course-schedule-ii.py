#
# @lc app=leetcode id=210 lang=python3
#
# [210] Course Schedule II
#
# https://leetcode.com/problems/course-schedule-ii/description/
#
# algorithms
# Medium (42.34%)
# Likes:    3384
# Dislikes: 161
# Total Accepted:    370.4K
# Total Submissions: 868.4K
# Testcase Example:  '2\n[[1,0]]'
#
# There are a total of n courses you have to take labelled from 0 to n - 1.
# 
# Some courses may have prerequisites, for example, if prerequisites[i] = [ai,
# bi] this means you must take the course bi before the course ai.
# 
# Given the total number of courses numCourses and a list of the prerequisite
# pairs, return the ordering of courses you should take to finish all courses.
# 
# If there are many valid answers, return any of them. If it is impossible to
# finish all courses, return an empty array.
# 
# 
# Example 1:
# 
# 
# Input: numCourses = 2, prerequisites = [[1,0]]
# Output: [0,1]
# Explanation: There are a total of 2 courses to take. To take course 1 you
# should have finished course 0. So the correct course order is [0,1].
# 
# 
# Example 2:
# 
# 
# Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
# Output: [0,2,1,3]
# Explanation: There are a total of 4 courses to take. To take course 3 you
# should have finished both courses 1 and 2. Both courses 1 and 2 should be
# taken after you finished course 0.
# So one correct course order is [0,1,2,3]. Another correct ordering is
# [0,2,1,3].
# 
# 
# Example 3:
# 
# 
# Input: numCourses = 1, prerequisites = []
# Output: [0]
# 
# 
# 
# Constraints:
# 
# 
# 1 <= numCourses <= 2000
# 0 <= prerequisites.length <= numCourses * (numCourses - 1)
# prerequisites[i].length == 2
# 0 <= ai, bi < numCourses
# ai != bi
# All the pairs [ai, bi] are distinct.
# 
# 
#

# @lc code=start
from collections import defaultdict, deque

class Solution:
    def __init__(self):
        self.order = defaultdict(list)
        self.indgree = defaultdict(int)

    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        self._build_indgree(numCourses, prerequisites)
        self._build_prerequisite(prerequisites)

        start = [course for course in range(numCourses) if self.indgree[course] == 0]
        start = deque(start)

        res = []
        while start:
            curr_course = start.popleft()
            res.append(curr_course)
            for next_course in self.order[curr_course]:
                self.indgree[next_course] -= 1
                if self.indgree[next_course] == 0:
                    start.append(next_course)

        return res if len(res) == numCourses else []


    def _build_prerequisite(self, prerequisites):
        for second, first in prerequisites:
            self.order[first].append(second)


    def _build_indgree(self, numCourses, prerequisites):
        for i in range(numCourses):
            self.indgree[i] = 0

        for second, first in prerequisites:
            self.indgree[second] += 1
# @lc code=end

