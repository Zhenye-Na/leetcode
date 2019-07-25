#
# @lc app=leetcode id=146 lang=python3
#
# [146] LRU Cache
#


class ListNode:
    def __init__(self, key, val, next=None, prev=None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev


class LRUCache:

    def __init__(self, capacity: int):
        self.cache_history = {}
        self.head = ListNode(-1, -1)
        self.tail = ListNode(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.cache_history:
            return -1
        node = self.cache_history[key]
        self._remove(node)
        self._push_back(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if self.get(key) != -1:
            self.cache_history[key].val = value
            return

        if len(self.cache_history) >= self.capacity:
            self._pop_first()

        node = ListNode(key, value)
        self._push_back(node)
        self.cache_history[key] = node

    def _pop_first(self):
        del self.cache_history[self.head.next.key]
        self._remove(self.head.next)

    def _push_back(self, node):
        node.next = self.tail
        self.tail.prev.next = node

        node.prev = self.tail.prev
        self.tail.prev = node

    def _remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
