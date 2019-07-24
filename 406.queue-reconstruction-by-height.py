#
# @lc app=leetcode id=406 lang=python3
#
# [406] Queue Reconstruction by Height
#
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        if not people or len(people) == 0:
            return []

        result = []
        sorted_people = sorted(people, key=lambda x: (-x[0], x[1]))
        for ppl in sorted_people:
            result.insert(ppl[1], ppl)

        return result

