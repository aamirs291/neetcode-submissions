class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        N = len(prices)
        l = 0
        r = 1
        profit = 0
        max_profit = 0

        while r<N:
            if prices[r]> prices[l]:
                profit = prices[r]- prices[l]
                max_profit = max(profit, max_profit)
            
            else:
                l = r
            
            r+=1
        
        return max_profit

