class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        n = len(cost)

        dp = [-1 for i in range(n+1)]
        
        def costClimb(idx):
            if idx>=n:
                return 0
            
            if dp[idx]!=-1:
                return dp[idx]

            one_step_cost = cost[idx] + costClimb(idx+1)
            two_step_cost = cost[idx] + costClimb(idx+2)

            min_cost = min(one_step_cost, two_step_cost)

            dp[idx] = min_cost

            return dp[idx]
        
        costClimb(0)

        return min(dp[0], dp[1])