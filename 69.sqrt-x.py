#
# @lc app=leetcode id=69 lang=python3
#
# [69] Sqrt(x)
#
class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 0:
            return -1
        if x == 0:
            return 0

        start, end = 1, x
        
        while start + 1 < end:
            
            mid = (end - start) // 2 + start
            mul = mid * mid

            if mul < x:
                start = mid
            elif mul > x:
                end = mid
            elif mul == x:
                return mid

        if start * start <= x:
            return start
        else:
            return end


