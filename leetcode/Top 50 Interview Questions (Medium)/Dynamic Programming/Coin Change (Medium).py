'''
time limit exceeded recursion version
'''

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        vals = set()
        vals_dict = dict()
        
        def recurse(coins, amount, count):
            
            if amount == 0:
                vals.add(count)
                return count
            
            for co in coins:
                if amount - co >= 0:
                    if len(vals) > 0:
                        if count < min(vals):
                            tmp = recurse(coins, amount - co, count + 1)
                    else:
                        tmp = recurse(coins, amount - co, count + 1)
            
            return
        
        recurse(coins, amount, 0)
        
        if len(vals) > 0:
            return min(vals)
        else:
            return -1

'''
top down memoization version
'''

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        cnt = [0 for x in range(amount)]
        
        def recurse(coins, amount, count):
            
            if amount < 0:
                return -1
            if amount == 0:
                return 0
            if count[amount-1] != 0:
                return count[amount-1]
            
            min_coins = float('inf')
            
            for co in coins:
                tmp = recurse(coins, amount - co, count)
                if tmp >= 0 and tmp < min_coins:
                    min_coins = 1 + tmp
            
            if min_coins == float('inf'):
                count[amount - 1] = -1
            else:
                count[amount - 1] = min_coins
            
            return count[amount - 1]
        
        if amount < 1:
            return 0
        else:
            return recurse(coins, amount, cnt)
        
        