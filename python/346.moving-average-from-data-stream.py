# [346] Moving Average from Data Stream

# Description

# Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.

# Example

# Example 1:

# MovingAverage m = new MovingAverage(3);
# m.next(1) = 1 // return 1.00000
# m.next(10) = (1 + 10) / 2 // return 5.50000
# m.next(3) = (1 + 10 + 3) / 3 // return 4.66667
# m.next(5) = (10 + 3 + 5) / 3 // return 6.00000


from collections import deque

class MovingAverage(object):
    """
    @param: size: An integer
    """
    def __init__(self, size):
        # do intialization if necessary
        self.queue = deque([])
        self.total = 0
        self.size = 0
        self.limit = size



    """
    @param: val: An integer
    @return:  
    """
    def next(self, val):
        # write your code here
        if self.size + 1 > self.limit:
            num = self.queue.popleft()
            self.total -= num
            self.size -= 1

        self.queue.append(val)
        self.total += val
        self.size += 1

        return self.total / self.size


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param = obj.next(val)