---
layout: post
title: "41. First Missing Positive"
category: array
---

## Problem Description

Given an unsorted integer array `nums`. Return the smallest positive integer that is not present in `nums`.

You must implement an algorithm that runs in `O(n)` time and uses `O(1)` auxiliary space.

Example 1:

```
Input: nums = [1,2,0]
Output: 3
Explanation: The numbers in the range [1,2] are all in the array.
```

Example 2:

```
Input: nums = [3,4,-1,1]
Output: 2
Explanation: 1 is in the array but 2 is missing.
```

Example 3:

```
Input: nums = [7,8,9,11,12]
Output: 1
Explanation: The smallest positive integer 1 is missing.
```

**Constraints:**

- `1 <= nums.length <= 105`
- `-2^31 <= nums[i] <= 2^31 - 1`

### Analysis

Before delving into the solution, let's understand the problem's key aspects:

- **Input**: An unsorted integer array `nums`.
- **Output**: The first missing positive integer.
- **Constraints**: The solution should run in `O(n)` time complexity and use only constant extra space.

### Solution

```py
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = ["#"] + nums
        for i in range(1, len(nums)):
            while i != nums[i]:
                if nums[i] < 1 or nums[i] >= len(nums):
                    break

                if nums[i] == nums[nums[i]]:
                    break

                tmp = nums[i]
                nums[i] = nums[nums[i]]
                nums[tmp] = tmp

        for i in range(1, len(nums)):
            if i != nums[i]:
                return i

        return len(nums)
```

The provided solution utilizes a cyclic sort algorithm to rearrange the elements of the array such that each positive integer `i` is placed at index `i`. Here's how the solution works:

1. **Modify Input Array**: A placeholder element `"#"` is prepended to the input array, making it 1-indexed.
2. **Cyclic Sort Implementation**:
   - Iterate through the array starting from index `1`.
   - While the current element is not in its correct position:
     - If the current element is less than `1` or greater than or equal to the length of the array, break the loop.
     - If the current element is equal to the element at the index specified by the current element's value, break the loop.
     - Swap the current element with the element at the index specified by the current element's value.
3. Iterate through the modified array from index `1`:
   - If the index does not match the value at that index, return the index.
4. If no missing positive integer is found in the array, return the length of the array.

### Complexity Analysis

- **Time Complexity**: `O(n)`. We iterate through the array twice, each time taking `O(n)` time.
- **Space Complexity**: `O(1)`. The solution uses only constant extra space as it modifies the input array in place.
