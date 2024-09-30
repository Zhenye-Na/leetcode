#
# @lc app=leetcode id=1381 lang=python3
#
# [1381] Design a Stack With Increment Operation
#
# https://leetcode.com/problems/design-a-stack-with-increment-operation/description/
#
# algorithms
# Medium (77.13%)
# Likes:    1904
# Dislikes: 101
# Total Accepted:    136K
# Total Submissions: 173.7K
# Testcase Example:  '["CustomStack","push","push","pop","push","push","push","increment","increment","pop","pop","pop","pop"]\n' +
#  '[[3],[1],[2],[],[2],[3],[4],[5,100],[2,100],[],[],[],[]]'
#
# Design a stack that supports increment operations on its elements.
#
# Implement the CustomStack class:
#
#
# CustomStack(int maxSize) Initializes the object with maxSize which is the
# maximum number of elements in the stack.
# void push(int x) Adds x to the top of the stack if the stack has not reached
# the maxSize.
# int pop() Pops and returns the top of the stack or -1 if the stack is
# empty.
# void inc(int k, int val) Increments the bottom k elements of the stack by
# val. If there are less than k elements in the stack, increment all the
# elements in the stack.
#
#
#
# Example 1:
#
#
# Input
#
# ["CustomStack","push","push","pop","push","push","push","increment","increment","pop","pop","pop","pop"]
# [[3],[1],[2],[],[2],[3],[4],[5,100],[2,100],[],[],[],[]]
# Output
# [null,null,null,2,null,null,null,null,null,103,202,201,-1]
# Explanation
# CustomStack stk = new CustomStack(3); // Stack is Empty []
# stk.push(1);                          // stack becomes [1]
# stk.push(2);                          // stack becomes [1, 2]
# stk.pop();                            // return 2 --> Return top of the stack
# 2, stack becomes [1]
# stk.push(2);                          // stack becomes [1, 2]
# stk.push(3);                          // stack becomes [1, 2, 3]
# stk.push(4);                          // stack still [1, 2, 3], Do not add
# another elements as size is 4
# stk.increment(5, 100);                // stack becomes [101, 102, 103]
# stk.increment(2, 100);                // stack becomes [201, 202, 103]
# stk.pop();                            // return 103 --> Return top of the
# stack 103, stack becomes [201, 202]
# stk.pop();                            // return 202 --> Return top of the
# stack 202, stack becomes [201]
# stk.pop();                            // return 201 --> Return top of the
# stack 201, stack becomes []
# stk.pop();                            // return -1 --> Stack is empty return
# -1.
#
#
#
# Constraints:
#
#
# 1 <= maxSize, x, k <= 1000
# 0 <= val <= 100
# At most 1000 calls will be made to each method of increment, push and pop
# each separately.
#
#
#


# @lc code=start
class CustomStack:

    def __init__(self, max_size: int):
        self.size = 0
        self.max_size = max_size
        self.stack = []

    def push(self, x: int) -> None:
        if self.size <= self.max_size - 1:
            self.stack.append(x)
            self.size += 1

    def pop(self) -> int:
        if self.size > 0:
            self.size -= 1
            return self.stack.pop()
        return -1

    def increment(self, k: int, val: int) -> None:
        for i in range(min(k, self.size)):
            self.stack[i] += val


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)
# @lc code=end
