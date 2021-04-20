#
# @lc app=leetcode id=207 lang=python3
#
# [207] Course Schedule
#
# https://leetcode.com/problems/course-schedule/description/
#
# algorithms
# Medium (44.28%)
# Likes:    5368
# Dislikes: 218
# Total Accepted:    548.8K
# Total Submissions: 1.2M
# Testcase Example:  '2\n[[1,0]]'
#
# There are a total of numCourses courses you have to take, labeled from 0 to
# numCourses - 1. You are given an array prerequisites where prerequisites[i] =
# [ai, bi] indicates that you must take course bi first if you want to take
# course ai.
# 
# 
# For example, the pair [0, 1], indicates that to take course 0 you have to
# first take course 1.
# 
# 
# Return true if you can finish all courses. Otherwise, return false.
# 
# 
# Example 1:
# 
# 
# Input: numCourses = 2, prerequisites = [[1,0]]
# Output: true
# Explanation: There are a total of 2 courses to take. 
# To take course 1 you should have finished course 0. So it is possible.
# 
# 
# Example 2:
# 
# 
# Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
# Output: false
# Explanation: There are a total of 2 courses to take. 
# To take course 1 you should have finished course 0, and to take course 0 you
# should also have finished course 1. So it is impossible.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= numCourses <= 10^5
# 0 <= prerequisites.length <= 5000
# prerequisites[i].length == 2
# 0 <= ai, bi < numCourses
# All the pairs prerequisites[i] are unique.
# 
# 
#

# @lc code=start
from collections import defaultdict, deque

class Solution:
    def __init__(self):
        self.mapping = defaultdict(list)
        self.indgree = defaultdict(int)


    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        self._build_indgree(numCourses, prerequisites)
        self._build_prerequisite(prerequisites)
        
        start_course = deque([])
        for c in self.indgree:
            if self.indgree[c] == 0:
                start_course.append(c)

        counter = 0
        while start_course:
            course = start_course.popleft()
            counter += 1
            for next_course in self.mapping[course]:
                self.indgree[next_course] -= 1
                if self.indgree[next_course] == 0:
                    start_course.append(next_course)

        return counter == numCourses


    def _build_prerequisite(self, prerequisites):
        for second, first in prerequisites:
            self.mapping[first].append(second)


    def _build_indgree(self, numCourses, prerequisites):
        for i in range(numCourses):
            self.indgree[i] = 0

        for second, first in prerequisites:
            self.indgree[second] += 1


# @lc code=end

