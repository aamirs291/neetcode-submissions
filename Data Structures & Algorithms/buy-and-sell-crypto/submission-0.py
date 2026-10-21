class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        N = len(prices)
        curr_min = float("inf")
        profit = 0
        max_profit = 0
        max_price = 0
        min_price = 0

        for r in range(N):
            if prices[r]<curr_min:
                curr_min = prices[r]
            
            else:
                profit = prices[r] - curr_min
                if profit > max_profit:
                    max_profit = profit
                    max_price = prices[r]
                    min_price = curr_min

        print(max_profit, min_price, max_price)
        return max_profit
        


