# [351] Android Unlock Patterns

# Description

# Given an Android 3x3 key lock screen and two integers m and n, where 1 <= m <= n <= 9,
# count the total number of unlock patterns of the Android lock screen, which consist
# of minimum of m keys and maximum n keys.

# Rules for a valid pattern:

# 1) Each pattern must connect at least m keys and at most n keys.
# 2) All the keys must be distinct.
# 3) If the line connecting two consecutive keys in the pattern passes through any other keys,
#    the other keys must have previously selected in the pattern. No jumps through non selected key is allowed.
# 4) The order of keys used matters.

# Explanation:
# | 1 | 2 | 3 |
# | 4 | 5 | 6 |
# | 7 | 8 | 9 |

# Invalid move: 4 - 1 - 3 - 6
# Line 1 - 3 passes through key 2 which had not been selected in the pattern.

# Invalid move: 4 - 1 - 9 - 2
# Line 1 - 9 passes through key 5 which had not been selected in the pattern.

# Valid move: 2 - 4 - 1 - 3 - 6
# Line 1 - 3 is valid because it passes through key 2, which had been selected in the pattern

# Valid move: 6 - 5 - 4 - 1 - 9 - 2
# Line 1 - 9 is valid because it passes through key 5, which had been selected in the pattern.

# Example

# Example 1

# Input: m = 1, n = 1
# Output: 9


# Example 2

# Input: m = 1, n = 2
# Output: 65


class Solution:
    """
    @param m: an integer
    @param n: an integer
    @return: the total number of unlock patterns of the Android lock screen
    """
    def __init__(self):
        self.count = 0
        self.res = []

        self.corners = [[0,0], [0,2], [2,0], [2, 2]]


    def numberOfPatterns(self, m, n):
        # Write your code here
        nums = [i for i in range(9)]
        self.dfs(m, n, [], 0, nums)

        # for res in self.res:
        #     print(res)
        return self.count


    def dfs(self, m, n, curr, start, nums):
        if len(curr) > n:
            return

        if m <= len(curr) <= n:
            self.count += 1
            self.res.append(curr[:])

        for i in range(start, len(nums)):
            if nums[i] not in curr:
                curr.append(nums[i])
                if self.valid(curr):
                    self.dfs(m, n, curr, 0, nums)
                curr.pop()


    def valid(self, points):
        prev_x, prev_y = points[0] // 3, points[0] % 3
        record = set([(prev_x, prev_y)])

        for i in range(1, len(points)):
            x, y = points[i] // 3, points[i] % 3

            if not ( (abs(x - prev_x) == 1 and abs(y - prev_y) == 0) \
                  or (abs(x - prev_x) == 0 and abs(y - prev_y) == 1) \
                  or (abs(x - prev_x) == 1 and abs(y - prev_y) == 1) \
                  or (abs(x - prev_x) == 1 and abs(y - prev_y) == 2) \
                  or (abs(x - prev_x) == 2 and abs(y - prev_y) == 1) ):

                if (abs(x - prev_x) == 0 and abs(y - prev_y) == 2):
                    if (x, max(y, prev_y) - 1) not in record:
                        return False
                
                if (abs(x - prev_x) == 2 and abs(y - prev_y) == 0):
                    if (max(x, prev_x) - 1, y) not in record:
                        return False

                if x + y == prev_x + prev_y or x - y == prev_x - prev_y:
                    if (1, 1) not in record:
                        return False

            record.add((x, y))
            prev_x, prev_y = x, y
        
        return True

