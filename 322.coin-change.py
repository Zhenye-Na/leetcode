#
# @lc app=leetcode id=322 lang=python3
#
# [322] Coin Change
#
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Initialize dp array -> combination of coins
        comb = [sys.maxsize] * (amount + 1)
        comb[0] = 0

        # iterate amout of money
        for i in range(amount + 1):

            # iterate coins
            for coin in coins:
                
                # if current amout is greater than coin value and we can reach the diff of amout and current coin
                if i >= coin and comb[i - coin] != sys.maxsize:
                    
                    # update
                    comb[i] = min(comb[i - coin] + 1, comb[i])
        
        # return if we can give a feasible combination
        return comb[amount] if comb[amount] != sys.maxsize else -1
