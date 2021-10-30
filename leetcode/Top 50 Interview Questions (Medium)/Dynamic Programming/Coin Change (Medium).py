'''
time limit exceeded recursion version
time complexity S*N where S is amount, N is number of types of coins
space complexity is S or amount 
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
        
'''
explaining top down memoization
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
                print('rec', co)
                tmp = recurse(coins, amount - co, count)
                print('tmp', tmp)
                if tmp >= 0 and tmp < min_coins:
                    min_coins = 1 + tmp
            
            if min_coins == float('inf'):
                count[amount - 1] = -1
            else:
                count[amount - 1] = min_coins
            
            print('count', count)
            
            return count[amount - 1]
        
        if amount < 1:
            return 0
        else:
            return recurse(coins, amount, cnt)
        
'''
print statments above return the following

[2,5] coins 
11 amount 

correct answer is 4 


rec 2
rec 2
rec 2
rec 2
rec 2
rec 2
tmp -1
rec 5
tmp -1
count [-1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
tmp -1
rec 5
tmp -1
count [-1, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0]
tmp -1
rec 5
tmp 0
count [-1, 0, -1, 0, 1, 0, 0, 0, 0, 0, 0]
tmp 1
rec 5
rec 2
tmp 0
rec 5
tmp -1
count [-1, 1, -1, 0, 1, 0, 0, 0, 0, 0, 0]
tmp 1
count [-1, 1, -1, 0, 1, 0, 2, 0, 0, 0, 0]
tmp 2
rec 5
rec 2
tmp 1
rec 5
tmp -1
count [-1, 1, -1, 2, 1, 0, 2, 0, 0, 0, 0]
tmp 2
count [-1, 1, -1, 2, 1, 0, 2, 0, 3, 0, 0]
tmp 3
rec 5
rec 2
tmp 2
rec 5
tmp -1
count [-1, 1, -1, 2, 1, 3, 2, 0, 3, 0, 0]
tmp 3
count [-1, 1, -1, 2, 1, 3, 2, 0, 3, 0, 4]

can see it continually building up from the botton 
'''