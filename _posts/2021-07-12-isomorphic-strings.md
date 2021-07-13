---
layout: post
title: "205. Isomorphic Strings"
category: hashmap
---


## Problem Description

Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

Example 1:

```
Input: s = "egg", t = "add"
Output: true
```

Example 2:

```
Input: s = "foo", t = "bar"
Output: false
```

Example 3:

```
Input: s = "paper", t = "title"
Output: true
```

Constraints:

```
1 <= s.length <= 5 * 104
t.length == s.length
s and t consist of any valid ascii character.
```

## Solution

Use HashMap to store character mapping

### Python

```python
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if not s or not t or len(s) == 0 or len(t) == 0 or len(s) != len(t):
            return False
        
        s2t, t2s = {}, {}
        n = len(s)
        
        for i in range(n):
            if s[i] not in s2t:
                if t[i] in t2s and t2s[t[i]] != s[i]:
                    return False
                s2t[s[i]] = t[i]
                t2s[t[i]] = s[i]
            else:
                # mapping contains s[i]
                if t[i] != s2t[s[i]]:
                    return False

        return True
```

### Java

```java
class Solution {
    public boolean isIsomorphic(String s, String t) {
        HashMap<Character, Character> s2t = new HashMap<>();
        HashMap<Character, Character> t2s = new HashMap<>();

        int n = s.length();
        for (int i = 0; i < n; i++) {
            if (!s2t.containsKey(s.charAt(i))) {
                if (t2s.containsKey(t.charAt(i)) && t2s.get(t.charAt(i)) != s.charAt(i)) {
                    return false;
                }
                s2t.put(s.charAt(i), t.charAt(i));
                t2s.put(t.charAt(i), s.charAt(i));
            } else {
                if (t.charAt(i) != s2t.get(s.charAt(i))) {
                    return false;
                }
            }
        }

        return true;
    }
}
```

**Complexity Analysis**

- Time Complexity
  - O(n)
- Space Complexity
  - O(n)

