class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        n = len(coins)

        dp = [[-1 for j in range(amount+1)] for i in range(n+1)]

        def numWays(idx, total_amount):
            if total_amount==0:
                return 1
            
            if total_amount<0 or idx==n:
                return 0
            
            if dp[idx][total_amount]!=-1:
                return dp[idx][total_amount]
            
            stay = numWays(idx, total_amount - coins[idx])
            move = numWays(idx+1, total_amount)

            dp[idx][total_amount] = stay+move
            return dp[idx][total_amount]
        
        return numWays(0, amount)
        