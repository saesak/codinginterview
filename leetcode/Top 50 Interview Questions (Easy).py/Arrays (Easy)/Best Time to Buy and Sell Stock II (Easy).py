class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        prev = -1 
        total = 0
        
        
        
        for i in range(n):
            if prev == -1:
                prev = prices[i]
                continue
            
            
            #if there's only 1 element or 0, profit will return 0 
            if prev < prices[i]: #selling conditions
                total = total + (prices[i] - prev)
                prev = prices[i] #if sold, this is minimum price
            else: #not selling
                prev = min(prev, prices[i]) #if not sold, this is min price
        
        
        return total