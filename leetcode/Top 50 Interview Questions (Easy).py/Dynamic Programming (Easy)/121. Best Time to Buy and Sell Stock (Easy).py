class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minprice = -1
        maxprofit = 0
        for idx, ele in enumerate(prices):  
            if minprice == -1 or ele < minprice:
                minprice = ele
            if ele - minprice > maxprofit:
                maxprofit = ele - minprice
        return maxprofit 
'''
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
'''