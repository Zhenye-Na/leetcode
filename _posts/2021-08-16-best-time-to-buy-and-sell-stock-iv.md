---
layout: post
title: "188. Best Time to Buy and Sell Stock IV"
category: dp
---

> This article is the explanation and codes given by Tushar's video on Youtube. Which is the video below. I recommend checking it out first and use this article as a review.


## Problem Description

You are given an integer array prices where prices[i] is the price of a given stock on the ith day, and an integer k.

Find the maximum profit you can achieve. You may complete at most k transactions.

Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

Example 1:

```
Input: k = 2, prices = [2,4,1]
Output: 2
Explanation: Buy on day 1 (price = 2) and sell on day 2 (price = 4), profit = 4-2 = 2.
```

Example 2:

```
Input: k = 2, prices = [3,2,6,5,0,3]
Output: 7
Explanation: Buy on day 2 (price = 2) and sell on day 3 (price = 6), profit = 6-2 = 4. Then buy on day 5 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
```

Constraints:

```
0 <= k <= 100
0 <= prices.length <= 1000
0 <= prices[i] <= 1000
```



## Solution 1

**Dynamic Programming**

`n` - days, `k` - k transactions

- Time Complexity: $O(n^2k)$
- Space Complexity: $O(nk)$

### State

```
f[i][j] represents max profit occurs on i-th transaction on day j 
```


### Initialization

- `f[0][j] = 0`, 0th transaction, profit is zero
- `f[i][0] = 0`, there is only one price, cannot make profit at all

### Function

```
f[i][j] = max{
    f[i][j - 1]                                 # this means we do not make a transaction on day j
    max(f[i - 1][m] + prices[j] - prices[m])    # this means we do make a transaction on day j.
                                                  we need make a for loop of m from 0 to j - 1,
                                                  and find out on which day we should sell and
                                                  buy to make max profit
}
```

### Answer

After calculating the DP array, the answer is `f[-1][-1]`


### Implementation


```python
def max_profit_slow_solution(prices, K):
    if K == 0 or prices == []:
        return 0

    days = len(prices)
    num_transactions = K + 1

    T = [[0 for _ in range(len(prices))] for _ in range(num_transactions)]

    for transaction in range(1, num_transactions):
        for day in range(1, days):
            # This maximum value of either
            # a) No Transaction on the day. We pick the value from day - 1
            # b) Max profit made by selling on the day plus the cost of the previous transaction, considered over m days
            T[transaction][day] = max(T[transaction][day - 1],
                                      max([(prices[day] - prices[m] + T[transaction - 1][m]) for m in range(day)]))

    print_actual_solution(T, prices)
    return T[-1][-1]
```


## Solution 2

**Dynamic Programming with Time Complexity optimization**

`n` - days, `k` - k transactions

- Time Complexity: $O(nk)$
- Space Complexity: $O(nk)$


### State

```
f[i][j] represents max profit occurs on i-th transaction on day j 
```


### Initialization

- `f[0][j] = 0`, 0th transaction, profit is zero
- `f[i][0] = 0`, there is only one price, cannot make profit at all


### Function

```
f[i][j] = max{ f[i][j - 1], prices[j] + maxDiff }
maxDiff = max{ maxDiff, f[i][j - 1] - prices[j] }
```

### Answer

After calculating the DP array, the answer is `f[-1][-1]`


### Implementation

```python
def max_profit(prices, K):
    if K == 0 or prices == []:
        return 0

    days = len(prices)
    num_transactions = K + 1  # 0th transaction up to and including kth transaction is considered.

    T = [[0 for _ in range(days)] for _ in range(num_transactions)]

    for transaction in range(1, num_transactions):
        max_diff = - prices[0]
        for day in range(1, days):
            T[transaction][day] = max(T[transaction][day - 1],     # No transaction
                                      prices[day] + max_diff)      # price on that day with max diff
            max_diff = max(max_diff,
                           T[transaction - 1][day] - prices[day])  # update max_diff

    print_actual_solution(T, prices)

    return T[-1][-1]
```


## Solution 3

**Dynamic Programming with Time and Space Complexity optimization**

`n` - days, `k` - k transactions

- Time Complexity: $O(nk)$
- Space Complexity: $O(n)$


### State

```
f[i][j] represents max profit occurs on i-th transaction on day j 
```


### Initialization

- `f[0][j] = 0`, 0th transaction, profit is zero
- `f[i][0] = 0`, there is only one price, cannot make profit at all


### Function

Rolling Array optimize Space Complexity

```
f[i % 2][j] = max{ f[i % 2][j - 1], prices[j] + maxDiff }
maxDiff = max{ maxDiff, f[(i - 1) % 2][j] - prices[j] }
```

### Answer

After calculating the DP array, the answer is `f[K % 2][-1]`


### Implementation

```python
class Solution:
    """
    @param K: An integer
    @param prices: An integer array
    @return: Maximum profit
    """
    def maxProfit(self, K, prices):
        # write your code here
        if not prices or len(prices) <= 1:
            return 0

        n = len(prices)

        # state: f[i][j] represents until jth day, i transactions have been occured
        f = [[0 for _ in range(n)] for _ in range(2)]

        # function: optimized version
        # f[i][j] = max(f[i][j - 1]  we dont make transactions on day j
        #               prices[j] + maxDiff  make transactions on day j
        # maxDiff = max(maxDiff, f[i - 1][j] - prices[j - 1])

        for i in range(1, K + 1):
            maxDiff = - prices[0]
            for j in range(1, n):
                f[i % 2][j] = max(f[i % 2][j - 1], prices[j] + maxDiff)
                maxDiff = max(maxDiff, f[(i - 1) % 2][j] - prices[j])

        return f[K % 2][-1]
```


## Print solution

```python
def print_actual_solution(T, prices):
    transaction = len(T) - 1
    day = len(T[0]) - 1
    stack = []

    while True:
        if transaction == 0 or day == 0:
            break

        if T[transaction][day] == T[transaction][day - 1]:  # Didn't sell
            day -= 1
        else:
            stack.append(day)          # sold
            max_diff = T[transaction][day] - prices[day]
            for k in range(day - 1, -1, -1):
                if T[transaction - 1][k] - prices[k] == max_diff:
                    stack.append(k)  # bought
                    transaction -= 1
                    break

    for entry in range(len(stack) - 1, -1, -2):
        print("Buy on day {day} at price {price}".format(day=stack[entry], price=prices[stack[transaction]]))
        print("Sell on day {day} at price {price}".format(day=stack[entry], price=prices[stack[transaction - 1]]))
```

## AC Solution in LeetCode

Some minor changes should be added so that it can pass the large testcases

```python
class Solution:
    """
    @param K: An integer
    @param prices: An integer array
    @return: Maximum profit
    """
    def maxProfit(self, K, prices):
        # write your code here
        if not prices or len(prices) <= 1:
            return 0

        if K > len(prices) // 2:
            return self.unlimited_profits(prices)

        n = len(prices)

        # state: f[i][j] represents until jth day, i transactions have been occured
        f = [[0 for _ in range(n)] for _ in range(2)]

        # function: optimized version
        # f[i][j] = max(f[i][j - 1]  we dont make transactions on day j
        #               prices[j] + maxDiff  make transactions on day j
        # maxDiff = max(maxDiff, f[i - 1][j] - prices[j - 1])

        for i in range(1, K + 1):
            maxDiff = - prices[0]
            for j in range(1, n):
                f[i % 2][j] = max(f[i % 2][j - 1], prices[j] + maxDiff)
                maxDiff = max(maxDiff, f[(i - 1) % 2][j] - prices[j])

        return f[K % 2][-1]


    def unlimited_profits(self, prices):
        profits = 0
        closing = prices[0]
        for opening in prices:
            profits += opening - closing if opening > closing else 0
            closing = opening
        return profits
```


## References

Tushar's youtube Channel - [Buy/Sell Stock With K transactions To Maximize Profit Dynamic Programming](https://www.youtube.com/watch?v=oDhu5uGq_ic)







