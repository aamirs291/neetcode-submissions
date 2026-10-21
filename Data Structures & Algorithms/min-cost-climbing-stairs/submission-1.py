class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        N = len(cost)
        dp = [-1 for i in range(N+1)]

        def dfs(idx):
            if idx==N:
                return 0
            if idx>N:
                return float("inf")
            if dp[idx]!=-1:
                return dp[idx]
            
            cost_1_step = cost[idx] + dfs(idx+1)
            cost_2_step = cost[idx] + dfs(idx+2)

            dp[idx] = min(cost_1_step, cost_2_step)
            return dp[idx]
        
        
        val =  min(dfs(0), dfs(1))
        print(dp)
        
        dp = [-1 for i in range(N)]
        def tab():
            # if idx==N:
            #     return 0
            # if idx>N:
            #     return float("inf")
            # if dp[idx]!=-1:
            #     return dp[idx]

            for idx in range(N-1,-1,-1):
            
                cost_1_step = cost[idx] + (0 if idx+1==N else dp[idx+1]) 
                cost_2_step = cost[idx] + (0 if idx+2>=N else dp[idx+2]) 

                dp[idx] = min(cost_1_step, cost_2_step)
                #return dp[idx]
        
        tab()
        print(dp)
        return min(dp[0], dp[1])

