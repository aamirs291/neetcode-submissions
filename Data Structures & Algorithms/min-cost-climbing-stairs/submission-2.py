class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        min_cost = [0]

        n = len(cost)
        dp = [-1 for i in range(n)]

        def mini(idx):
            if idx>=n:
                return 0
            if dp[idx]!=-1:
                return dp[idx]

            min_cost = [0]
            min_cost[0] += cost[idx] + min(mini(idx+1), mini(idx+2))

            dp[idx] = min_cost[0]
            return dp[idx]
        
        mini(0)
        return min(dp[0], dp[1])


        