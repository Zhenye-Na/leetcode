# 1921. Eliminate Maximum Number of Monsters

# You are playing a video game where you are defending your city from a group of n monsters.
# You are given a 0-indexed integer array dist of size n, where dist[i] is the initial
# distance in meters of the ith monster from the city.

# The monsters walk toward the city at a constant speed. The speed of each monster is
# given to you in an integer array speed of size n, where speed[i] is the speed of the
# ith monster in meters per minute.

# The monsters start moving at minute 0. You have a weapon that you can choose to use
# at the start of every minute, including minute 0. You cannot use the weapon in the
# middle of a minute. The weapon can eliminate any monster that is still alive.

# You lose when any monster reaches your city. If a monster reaches the city exactly
# at the start of a minute, it counts as a loss, and the game ends before you can use
# your weapon in that minute.

# Return the maximum number of monsters that you can eliminate before you lose, or n
# if you can eliminate all the monsters before they reach the city.

# Example 1:

# Input: dist = [1,3,4], speed = [1,1,1]
# Output: 3
# Explanation:
# At the start of minute 0, the distances of the monsters are [1,3,4], you eliminate the first monster.
# At the start of minute 1, the distances of the monsters are [X,2,3], you don't do anything.
# At the start of minute 2, the distances of the monsters are [X,1,2], you eliminate the second monster.
# At the start of minute 3, the distances of the monsters are [X,X,1], you eliminate the third monster.
# All 3 monsters can be eliminated.


# Example 2:

# Input: dist = [1,1,2,3], speed = [1,1,1,1]
# Output: 1
# Explanation:
# At the start of minute 0, the distances of the monsters are [1,1,2,3], you eliminate the first monster.
# At the start of minute 1, the distances of the monsters are [X,0,1,2], so you lose.
# You can only eliminate 1 monster.


# Example 3:

# Input: dist = [3,2,4], speed = [5,3,2]
# Output: 1
# Explanation:
# At the start of minute 0, the distances of the monsters are [3,2,4], you eliminate the first monster.
# At the start of minute 1, the distances of the monsters are [X,0,2], so you lose.
# You can only eliminate 1 monster.
 

# Constraints:

# n == dist.length == speed.length
# 1 <= n <= 105
# 1 <= dist[i], speed[i] <= 105


# Solution
#   Sort the monsters by arrival times
#   If the moster arrives earlier than we can shoot, then we lost

class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        if not dist or not speed or len(dist) == 0 or len(speed) == 0 or len(dist) != len(speed):
            return 0
        
        l = len(speed)
        orders = []
        for i in range(l):
            orders.append([dist[i], speed[i]])

        orders.sort(key=lambda x: math.ceil(x[0] / x[1]))
        
        for i in range(l):
            if orders[i][0] <= i * orders[i][1]:
                # arrive earlier than we can shoot
                return i
            
        return l
