---
layout: post
title: "382. Linked List Random Node"
category: linked-list
---

## Problem Description

Given a singly linked list, return a random node's value from the linked list. Each node must have the same probability of being chosen.

Implement the Solution class:

- `Solution(ListNode head)` Initializes the object with the integer array nums.
- `int getRandom()` Chooses a node randomly from the list and returns its value. All the nodes of the list should be equally likely to be choosen.


Example 1:

![](https://assets.leetcode.com/uploads/2021/03/16/getrand-linked-list.jpg)

```
Input
["Solution", "getRandom", "getRandom", "getRandom", "getRandom", "getRandom"]
[[[1, 2, 3]], [], [], [], [], []]
Output
[null, 1, 3, 2, 2, 3]

Explanation
Solution solution = new Solution([1, 2, 3]);
solution.getRandom(); // return 1
solution.getRandom(); // return 3
solution.getRandom(); // return 2
solution.getRandom(); // return 2
solution.getRandom(); // return 3
// getRandom() should return either 1, 2, or 3 randomly. Each element should have equal probability of returning.
```

**Constraints:**

- The number of nodes in the linked list will be in the range [1, 104].
- -10^4 <= Node.val <= 10^4
- At most 104 calls will be made to `getRandom()`.

**Follow up:**

- What if the linked list is extremely large and its length is unknown to you?
- Could you solve this efficiently without using extra space?

## Solution

Naive approach is to traverse the list, get the length, and use random.randint(0, length) to select value. But the restriction is that "the linked list is extremely large and its length is unknown"

Core algorithm is [Reservoir sampling](https://www.wikiwand.com/en/Reservoir_sampling)

A naive way to explain the algorithm is as follows

```
the frist element can always be selected, using array represents the linked list visually

[a] <- a is the first element

res = a, 100%

when we move the pointer right, we will get:

[a, b], then there is 50% chance I get a, and 50% chance I get b, which is

res = 50% res, 50% b => 50% a, 50% b

when we have [a, b, c]

res = 2/3 res, 1/3 c => 1/3 a, 1/3 b, 1/3 c

etc..
```

### Python

```python
# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.head = head

    def getRandom(self) -> int:
        count = res = 0
        curr = self.head
        while curr:
            count += 1
            if random.random() <= 1 / count:
                res = curr.val 
            curr = curr.next

        return res


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
# @lc code=end
```


