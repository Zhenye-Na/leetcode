#
# @lc app=leetcode id=381 lang=python3
#
# [381] Insert Delete GetRandom O(1) - Duplicates allowed
#
# https://leetcode.com/problems/insert-delete-getrandom-o1-duplicates-allowed/description/
#
# algorithms
# Hard (34.74%)
# Likes:    1103
# Dislikes: 89
# Total Accepted:    83.3K
# Total Submissions: 238.1K
# Testcase Example:  '["RandomizedCollection","insert","insert","insert","getRandom","remove","getRandom"]\n' +
#   '[[],[1],[1],[2],[],[1],[]]'
#
# Implement the RandomizedCollection class:
# 
# 
# RandomizedCollection() Initializes the RandomizedCollection object.
# bool insert(int val) Inserts an item val into the multiset if not present.
# Returns true if the item was not present, false otherwise.
# bool remove(int val) Removes an item val from the multiset if present.
# Returns true if the item was present, false otherwise. Note that if val has
# multiple occurrences in the multiset, we only remove one of them.
# int getRandom() Returns a random element from the current multiset of
# elements (it's guaranteed that at least one element exists when this method
# is called). The probability of each element being returned is linearly
# related to the number of same values the multiset contains.
# 
# 
# 
# Example 1:
# 
# 
# Input
# ["RandomizedCollection", "insert", "insert", "insert", "getRandom", "remove",
# "getRandom"]
# [[], [1], [1], [2], [], [1], []]
# Output
# [null, true, false, true, 2, true, 1]
# 
# Explanation
# RandomizedCollection randomizedCollection = new RandomizedCollection();
# randomizedCollection.insert(1);   // return True. Inserts 1 to the
# collection. Returns true as the collection did not contain 1.
# randomizedCollection.insert(1);   // return False. Inserts another 1 to the
# collection. Returns false as the collection contained 1. Collection now
# contains [1,1].
# randomizedCollection.insert(2);   // return True. Inserts 2 to the
# collection, returns true. Collection now contains [1,1,2].
# randomizedCollection.getRandom(); // getRandom should return 1 with the
# probability 2/3, and returns 2 with the probability 1/3.
# randomizedCollection.remove(1);   // return True. Removes 1 from the
# collection, returns true. Collection now contains [1,2].
# randomizedCollection.getRandom(); // getRandom should return 1 and 2 both
# equally likely.
# 
# 
# 
# Constraints:
# 
# 
# -2^31 <= val <= 2^31 - 1
# At most 10^5 calls will be made to insert, remove, and getRandom.
# There will be at least one element in the data structure when getRandom is
# called.
# 
# 
# 
# Follow up: Could you implement the functions of the class with each function
# works in average O(1) time?
#

# @lc code=start
from collections import defaultdict

class RandomizedCollection:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.mapping = defaultdict(set)
        self.array = []


    def insert(self, val: int) -> bool:
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        """
        res = True
        if val in self.mapping:
            res = False

        self.array.append(val)
        self.mapping[val].add(len(self.array) - 1)

        return res
        

    def remove(self, val: int) -> bool:
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        """
        res = False
        if val in self.mapping:
            res = True

        if not res:
            return res

        if self.array[len(self.array) - 1] == val:
            
            self.mapping[val].remove(len(self.array) - 1)
            self.array.pop()

        else:
            # swap valur from last and update
            last_idx = len(self.array) - 1
            first_idx = -1
            for idx in self.mapping[val]:
                first_idx = idx
                break

            if first_idx == -1:
                return False
            
            self.mapping[self.array[last_idx]].add(first_idx)
            self.mapping[self.array[last_idx]].remove(last_idx)
            
            self.array[first_idx], self.array[last_idx] = self.array[last_idx], self.array[first_idx]

            self.mapping[val].remove(first_idx)
            if len(self.mapping[val]) == 0:
                del self.mapping[val]
            self.array.pop()

        return res


    def getRandom(self) -> int:
        """
        Get a random element from the collection.
        """
        return random.choice(self.array)
        

# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
# @lc code=end

