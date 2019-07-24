#
# @lc app=leetcode id=735 lang=python3
#
# [735] Asteroid Collision
#
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        if not asteroids or len(asteroids) == 0:
            return []

        stack = []
        for asteroid in asteroids:
            while stack and stack[-1] > 0 and stack[-1] < -asteroid:
                stack.pop()
            if stack and stack[-1] > 0 and stack[-1] + asteroid == 0:
                stack.pop()
                continue
            if stack and stack[-1] > 0 and asteroid < 0 and stack[-1] > -asteroid:
                continue
            stack.append(asteroid)

        return stack


