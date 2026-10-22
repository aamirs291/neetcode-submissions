class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        cur_min = prices[0]
        max_profit = 0

        for i in range(len(prices)):

            curr_profit = prices[i] - cur_min

            if prices[i] < cur_min:
                cur_min = prices[i]

            if curr_profit > max_profit:
                max_profit = curr_profit
        

        return max_profit
            

                
