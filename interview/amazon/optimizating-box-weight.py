# Optimizating Box Weight

# https://aonecode.com/amazon-online-assessment-optimizing-box-weight

from collections import deque

class OptimizatingBoxWeight:

    def solve(self, arr):
        arr.sort()
        total_sum = sum(arr)

        # we split the arr to A and B where sum(A) > sum(B)
        # we can deduct that 2 * sum(A) > total_sum

        running_sum = 0
        res = deque([])

        for i in range(len(arr) - 1, -1 , -1):
            running_sum += arr[i]
            res.appendleft(arr[i])
            if 2 * running_sum > total_sum:
                break


        print(list(res))
        return list(res)


obw = OptimizatingBoxWeight()
obw.solve([5, 3, 2, 4, 1, 2])
obw.solve([1,1,1,1,1,1])
