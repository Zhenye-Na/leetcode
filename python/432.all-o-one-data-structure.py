#
# @lc app=leetcode id=432 lang=python3
#
# [432] All O`one Data Structure
#
# https://leetcode.com/problems/all-oone-data-structure/description/
#
# algorithms
# Hard (36.53%)
# Likes:    1666
# Dislikes: 183
# Total Accepted:    97.5K
# Total Submissions: 251.2K
# Testcase Example:  '["AllOne","inc","inc","getMaxKey","getMinKey","inc","getMaxKey","getMinKey"]\n' +
#  '[[],["hello"],["hello"],[],[],["leet"],[],[]]'
#
# Design a data structure to store the strings' count with the ability to
# return the strings with minimum and maximum counts.
#
# Implement the AllOne class:
#
#
# AllOne() Initializes the object of the data structure.
# inc(String key) Increments the count of the string key by 1. If key does not
# exist in the data structure, insert it with count 1.
# dec(String key) Decrements the count of the string key by 1. If the count of
# key is 0 after the decrement, remove it from the data structure. It is
# guaranteed that key exists in the data structure before the decrement.
# getMaxKey() Returns one of the keys with the maximal count. If no element
# exists, return an empty string "".
# getMinKey() Returns one of the keys with the minimum count. If no element
# exists, return an empty string "".
#
#
# Note that each function must run in O(1) average time complexity.
#
#
# Example 1:
#
#
# Input
# ["AllOne", "inc", "inc", "getMaxKey", "getMinKey", "inc", "getMaxKey",
# "getMinKey"]
# [[], ["hello"], ["hello"], [], [], ["leet"], [], []]
# Output
# [null, null, null, "hello", "hello", null, "hello", "leet"]
#
# Explanation
# AllOne allOne = new AllOne();
# allOne.inc("hello");
# allOne.inc("hello");
# allOne.getMaxKey(); // return "hello"
# allOne.getMinKey(); // return "hello"
# allOne.inc("leet");
# allOne.getMaxKey(); // return "hello"
# allOne.getMinKey(); // return "leet"
#
#
#
# Constraints:
#
#
# 1 <= key.length <= 10
# key consists of lowercase English letters.
# It is guaranteed that for each call to dec, key is existing in the data
# structure.
# At most 5 * 10^4 calls will be made to inc, dec, getMaxKey, and getMinKey.
#
#
#

# @lc code=start
from collections import defaultdict
from sortedcontainers import SortedDict


class AllOne:

    def __init__(self):
        self.map = defaultdict(int)  # key -> count
        self.reverse_map = SortedDict()  # count -> set of keys

    def inc(self, key: str) -> None:
        curr_count = self.map.get(key, 0)
        next_count = curr_count + 1

        self.map[key] = next_count
        if curr_count > 0:
            self.reverse_map[curr_count].remove(key)
            if not self.reverse_map[curr_count]:
                del self.reverse_map[curr_count]

        if next_count not in self.reverse_map:
            self.reverse_map[next_count] = set()
        self.reverse_map[next_count].add(key)

    def dec(self, key: str) -> None:
        curr_count = self.map.get(key, 0)
        if curr_count == 0:
            return

        next_count = curr_count - 1

        self.reverse_map[curr_count].remove(key)
        if not self.reverse_map[curr_count]:
            del self.reverse_map[curr_count]

        if next_count == 0:
            del self.map[key]
        else:
            self.map[key] = next_count
            if next_count not in self.reverse_map:
                self.reverse_map[next_count] = set()
            self.reverse_map[next_count].add(key)

    def getMaxKey(self) -> str:

        if not self.reverse_map:
            return ""
        max_count = self.reverse_map.peekitem(-1)[0]
        return next(iter(self.reverse_map[max_count]))

    def getMinKey(self) -> str:

        if not self.reverse_map:
            return ""
        min_count = self.reverse_map.peekitem(0)[0]
        return next(iter(self.reverse_map[min_count]))


"""
| Operation     | Time Complexity | Space Complexity |
|---------------|-----------------|------------------|
| `inc(key)`    | O(log k)        | O(n)             |
| `dec(key)`    | O(log k)        | O(n)             |
| `getMaxKey()` | O(1)            | O(n)             |
| `getMinKey()` | O(1)            | O(n)             |

Where:
- `n` is the number of distinct keys.
- `k` is the number of distinct counts (which is less than or equal to `n`).
"""

# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()
# @lc code=end
