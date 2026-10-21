class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        n = len(coins)

        dp = [[-1 for j in range(amount+1)] for i in range(n+1)]

        def no_of_coins(idx, tot_amount):
            if tot_amount==0:
                return 0
            if tot_amount<0 or idx==n:
                return float("inf")
            
            if dp[idx][tot_amount]!=-1:
                return dp[idx][tot_amount]

            stay = 1 + no_of_coins(idx, tot_amount - coins[idx])
            move = no_of_coins(idx+1, tot_amount)

            dp[idx][tot_amount] = min(stay, move)
            return dp[idx][tot_amount]

        res = no_of_coins(0, amount)
        # print(res)
        return res if res!=float("inf") else -1

        