---
layout: post
title: "25. Reverse Nodes in k-Group"
category: linked-list
---


## Problem Description

Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

You may not alter the values in the list's nodes, only nodes themselves may be changed.

Example 1:

![](https://raw.githubusercontent.com/Zhenye-Na/img-hosting-picgo/master/img/reverse_ex1.jpg)

```
Input: head = [1,2,3,4,5], k = 2
Output: [2,1,4,3,5]
```

Example 2:

![](https://raw.githubusercontent.com/Zhenye-Na/img-hosting-picgo/master/img/reverse_ex2.jpg)

```
Input: head = [1,2,3,4,5], k = 3
Output: [3,2,1,4,5]
```

Example 3:

```
Input: head = [1,2,3,4,5], k = 1
Output: [1,2,3,4,5]
```

Example 4:

```
Input: head = [1], k = 1
Output: [1]
```

Constraints:

```
The number of nodes in the list is in the range sz.
1 <= sz <= 5000
0 <= Node.val <= 1000
1 <= k <= sz
```

**Follow-up**: Can you solve the problem in O(1) extra memory space?


## Solution


### Python

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return head

        dummy = ListNode(0, head)
        head = dummy

        while head:
            head = self._reverseK(head, k)

        return dummy.next

    def _reverseK(self, node, k):
        n1, nk = node.next, node
        for _ in range(k):
            nk = nk.next
            if nk is None:
                return nk

        nk_next = nk.next

        # reverse
        prev, curt = None, n1
        while curt != nk_next:
            tmp = curt.next
            curt.next = prev
            prev = curt
            curt = tmp

        # connect
        node.next = nk
        n1.next = nk_next

        return n1

```


### Java

```java
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode reverseKGroup(ListNode head, int k) {
        ListNode dummy = new ListNode(0);
        dummy.next = head;
        
        head = dummy;
        
        while (head != null) {
            head = reverseKNodes(head, k);
        }
        return dummy.next;
    }

    private ListNode reverseKNodes(ListNode head, int k) {
        
        // head -> n1 -> n2 -> n3 -> ... -> nk -> nk+1
        // head -> nk -> ... -> n1 -> nk+1
        // reverse from n1 ~ nk
        // return n1
        ListNode first = head.next;
        ListNode counter = head;
        for (int i = 0; i < k; i++) {
            counter = counter.next;
            if (counter == null) {
                return null;
            }
        }
        
        // counter => last node to reverse in this batch
        
        ListNode nextNode = counter.next;
        ListNode prev = null;
        ListNode curr = first;
        while (curr != nextNode) {
            ListNode tmp = curr.next;
            curr.next = prev;
            prev = curr;
            curr = tmp;
        }
        
        first.next = nextNode;
        head.next = counter;
        
        return first;
    }
}
```


**Complexity Analysis**

- Time Complexity
  - O(n)
- Space Complexity
  - O(1)
