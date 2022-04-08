---
layout: post
title: "703. Kth Largest Element in a Stream"
category: dp
---

## Probelm Description

Design a class to find the kth largest element in a stream. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Implement KthLargest class:

- `KthLargest(int k, int[] nums)` Initializes the object with the integer k and the stream of integers nums.
- `int add(int val)` Appends the integer val to the stream and returns the element representing the kth largest element in the stream.


Example 1:

```
Input
["KthLargest", "add", "add", "add", "add", "add"]
[[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]
Output
[null, 4, 5, 5, 8, 8]

Explanation
KthLargest kthLargest = new KthLargest(3, [4, 5, 8, 2]);
kthLargest.add(3);   // return 4
kthLargest.add(5);   // return 5
kthLargest.add(10);  // return 5
kthLargest.add(9);   // return 8
kthLargest.add(4);   // return 8
```

Constraints:

```
1 <= k <= 10^4
0 <= nums.length <= 10^4
-10^4 <= nums[i] <= 10^4
-10^4 <= val <= 10^4
At most 104 calls will be made to add.
It is guaranteed that there will be at least k elements in the array when you search for the kth element.
```

## Solution

Given the problem, `Kth largest` or `Kth smallest`, we immediatly know we can use Heap (or Priority Queue) as the key data structure to solve this problem. I have two solutions for this question:

- Heap
- Binary Search

Both implementation is very straightforward so lets dive in.


### Heap

```python
# @lc code=start
# Heap
#   Time Complexity N * O(log(k))
#   Space Complexity O(k)

from heapq import heappush, heappop

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = []
        self.k = k
        for num in nums:
            self._insert(num)


    def add(self, val: int) -> int:
        self._insert(val)
        return self.heap[0]


    def _insert(self, num):
        if len(self.heap) < self.k:
            heappush(self.heap, num)
        else:
            if num > self.heap[0]:
                heappush(self.heap, num)
                heappop(self.heap)

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
# @lc code=end
```


### Binary Search

```python
# @lc code=start
# Binary Search
#   Time Complexity N * O(log(n))
#   Space Complexity O(n)

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.nums = nums[:]
        self.nums.sort()
        self.k = k
        self.k_large = float('-inf')


    def add(self, val: int) -> int:

        if val >= self.k_large:
            i = bisect.bisect_left(self.nums, val)
            self.nums = self.nums[:i] + [val] + self.nums[i:]
        
            self.k_large = self.nums[len(self.nums) - self.k]
        return self.k_large


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
# @lc code=end
```


## Similar Questions

- [295. Find Median from Data Stream](https://leetcode.com/problems/find-median-from-data-stream/)
