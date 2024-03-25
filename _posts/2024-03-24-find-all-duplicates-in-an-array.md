---
layout: post
title: "442. Find All Duplicates in an Array"
category: array
---


## Problem Description

Given an integer array nums of length n where all the integers of nums are in the range `[1, n]` and each integer appears once or twice, return an array of all the integers that appears twice.

You must write an algorithm that runs in `O(n)` time and uses only constant extra space.

Example 1:

```
Input: nums = [4,3,2,7,8,2,3,1]
Output: [2,3]
```

Example 2:

```
Input: nums = [1,1,2]
Output: [1]
```

Example 3:

```
Input: nums = [1]
Output: []
```

### Analysis

Before diving into the solution, let's dissect the problem requirements and constraints:

- **Input**: An integer array `nums` containing integers in the range `[1, n]`.
- **Output**: An array containing all integers that appear **twice** in the input array.
- **Constraints**: The solution must operate in `O(n)` time complexity and use only constant extra space.

### Solution
To solve this problem efficiently, we can employ the cyclic sort algorithm. Here's a step-by-step breakdown of our approach:

1. **Modify the Input Array**: We prepend a placeholder element `"#"` to the input array to make it 1-indexed rather than 0-indexed. This simplifies the implementation of the cyclic sort algorithm.

2. **Cyclic Sort Implementation**:
   - We iterate through the array starting from index `1`.
   - At each index, we swap the current element with the element at the index specified by the current element's value until the current element is in its correct position or until we encounter a duplicate.
   - If a duplicate is encountered, we break out of the loop.

3. **Finding Duplicates**: After completing the cyclic sort, we iterate through the array again from index 1 to find the elements that didn't end up in their correct positions. These elements represent the duplicates in the array, which we append to the result list.

```python
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        nums = ["#"] + nums
        for i in range(1, len(nums)):
            while i != nums[i]:
                if nums[i] == nums[nums[i]]:
                    break

                tmp = nums[i]
                nums[i] = nums[nums[i]]
                nums[tmp] = tmp

        res = []
        for i in range(1, len(nums)):
            if i != nums[i]:
                res.append(nums[i])

        return res
```

### Complexity Analysis

- **Time Complexity**: `O(n)`. We iterate through the array twice, each time taking `O(n)` time.
- **Space Complexity**: `O(1)`. We use only constant extra space as we modify the input array in place.
