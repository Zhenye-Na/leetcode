---
layout: post
title: "91. Decode Ways"
category: dp
---


## Problem Description

A message containing letters from A-Z can be encoded into numbers using the following mapping:

```
'A' -> "1"
'B' -> "2"
...
'Z' -> "26"
```

To decode an encoded message, all the digits must be grouped then mapped back into letters using the reverse of the mapping above (there may be multiple ways). For example, "11106" can be mapped into:

- "AAJF" with the grouping (1 1 10 6)
- "KJF" with the grouping (11 10 6)

Note that the grouping (1 11 06) is invalid because "06" cannot be mapped into 'F' since "6" is different from "06".

Given a string s containing only digits, return the number of ways to decode it.

The answer is guaranteed to fit in a 32-bit integer.

Example 1:

```
Input: s = "12"
Output: 2
Explanation: "12" could be decoded as "AB" (1 2) or "L" (12).
```

Example 2:

```
Input: s = "226"
Output: 3
Explanation: "226" could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).
```

Example 3:

```
Input: s = "0"
Output: 0
Explanation: There is no character that is mapped to a number starting with 0.
The only valid mappings with 0 are 'J' -> "10" and 'T' -> "20", neither of which start with 0.
Hence, there are no valid ways to decode this since all digits need to be mapped.
```


Example 4:

```
Input: s = "06"
Output: 0
Explanation: "06" cannot be mapped to "F" because of the leading zero ("6" is different from "06").
```

Constraints:

```
1 <= s.length <= 100
s contains only digits and may contain leading zero(s).
```

## Solution

Use Dynamic Programming, where `dp[i]` represents the number of decode ways for string `s[i:]`

### Python

```python
class Solution:
    def numDecodings(self, s: str) -> int:
        s = "#" + s
        n = len(s)

        dp = [0 for _ in range(n)]
        dp[0] = 1

        if s[1] == "0":
            return 0
        else:
            dp[1] = 1

        for i in range(2, n):
            if s[i] == "0":
                if s[i - 1] == "1" or s[i - 1] == "2":
                    dp[i] += dp[i - 2]
                else:
                    return 0

            else:
                # s[i] = 1 ... 9
                dp[i] += dp[i - 1]
                if s[i - 1] == "1" or s[i - 1] == "2" and int(s[i]) <= 6:
                    dp[i] += dp[i - 2]

        return dp[n - 1]
```

### Java

```java
class Solution {
    public int numDecodings(String s) {
        StringBuilder sb = new StringBuilder();
        sb.append("#");
        sb.append(s);
        s = sb.toString();

        int n = s.length();

        // dp initialization
        // dp[i] means the number of ways to decode s[i:]
        int[] dp = new int[n];
        dp[0] = 1;
        if (s.charAt(1) == '0')
            return 0;
        dp[1] = 1;

        // for loop the input string
        for (int i = 2; i < n; i++) {
            if (s.charAt(i) == '0') {
                if (s.charAt(i - 1) == '1' || s.charAt(i - 1) == '2') {
                    dp[i] += dp[i - 2];
                }

            } else {
                // s.charAt(i) == 1 ... 9
                dp[i] += dp[i - 1];
                if (s.charAt(i - 1) == '1' || s.charAt(i - 1) == '2' && s.charAt(i) <= '6') {
                    dp[i] += dp[i - 2];
                }

            }
        }

        for (int i = 0; i < n; i++)
            System.out.println(s.charAt(i) + " : " + dp[i]);
        
        return dp[n - 1];
    }
}
```

**Complexity Analysis**

- Time Complexity
  - O(n)
- Space Complexity
  - O(n)
