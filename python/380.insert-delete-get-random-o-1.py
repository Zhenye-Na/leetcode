#
# @lc app=leetcode id=380 lang=python3
#
# [380] Insert Delete GetRandom O(1)
#
# https://leetcode.com/problems/insert-delete-getrandom-o1/description/
#
# algorithms
# Medium (48.66%)
# Likes:    3462
# Dislikes: 205
# Total Accepted:    323.9K
# Total Submissions: 660.6K
# Testcase Example:  '["RandomizedSet","insert","remove","insert","getRandom","remove","insert","getRandom"]\n' +
#   '[[],[1],[2],[2],[],[1],[2],[]]'
#
# Implement the RandomizedSet class:
# 
# 
# RandomizedSet() Initializes the RandomizedSet object.
# bool insert(int val) Inserts an item val into the set if not present. Returns
# true if the item was not present, false otherwise.
# bool remove(int val) Removes an item val from the set if present. Returns
# true if the item was present, false otherwise.
# int getRandom() Returns a random element from the current set of elements
# (it's guaranteed that at least one element exists when this method is
# called). Each element must have the same probability of being returned.
# 
# 
# 
# Example 1:
# 
# 
# Input
# ["RandomizedSet", "insert", "remove", "insert", "getRandom", "remove",
# "insert", "getRandom"]
# [[], [1], [2], [2], [], [1], [2], []]
# Output
# [null, true, false, true, 2, true, false, 2]
# 
# Explanation
# RandomizedSet randomizedSet = new RandomizedSet();
# randomizedSet.insert(1); // Inserts 1 to the set. Returns true as 1 was
# inserted successfully.
# randomizedSet.remove(2); // Returns false as 2 does not exist in the set.
# randomizedSet.insert(2); // Inserts 2 to the set, returns true. Set now
# contains [1,2].
# randomizedSet.getRandom(); // getRandom() should return either 1 or 2
# randomly.
# randomizedSet.remove(1); // Removes 1 from the set, returns true. Set now
# contains [2].
# randomizedSet.insert(2); // 2 was already in the set, so return false.
# randomizedSet.getRandom(); // Since 2 is the only number in the set,
# getRandom() will always return 2.
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
import random

class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.mapping = {}
        self.array = []
        

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val not in self.mapping:
            self.array.append(val)
            self.mapping[val] = len(self.array) - 1
            return True
        return False
        

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val in self.mapping:
            val_idx = self.mapping[val]

            # swap this val with the last value in self.array
            self.mapping[self.array[len(self.array) - 1]] = val_idx
            self.array[val_idx], self.array[len(self.array) - 1] = self.array[len(self.array) - 1], self.array[val_idx]

            # remove records
            del self.mapping[val]
            self.array.pop()

            return True

        return False


    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return random.choice(self.array)












class ListNode:

    def __init__(self, val, next_node=None):
        self.val = val
        self.next= next_node


class RandomizedSet_LinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = ListNode(0)
        self.prev_node = self.root
        self.mapping = {}
        self.all_nodes = []

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if self.mapping.get(val) is None:
            # create ListNode
            node = ListNode(val)

            # store val with its previous node
            self.mapping[val] = self.prev_node

            # insert to the back
            self.prev_node.next = node

            # update pointer
            self.prev_node = node

            self.all_nodes = list(self.mapping.items())

            return True

        return False



    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        node = self.mapping.get(val)
        if node is not None:

            if node.next.next is None:
                # self.prev_node need to be updated
                self.prev_node = node

            # remove by skipping the next node
            node.next = node.next.next

            # remove from hashmap
            del self.mapping[val]

            self.all_nodes = list(self.mapping.items())

            return True
        
        return False


    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        val, _ = random.choice(self.all_nodes)
        return val
# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
# @lc code=end

