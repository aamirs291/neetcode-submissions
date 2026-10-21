class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        N = len(cost)

        def dfs(idx):
            if idx>=N:
                return 0
            if idx>N:
                return float("inf")
            
            cost_1_step = cost[idx] + dfs(idx+1)
            cost_2_step = cost[idx] + dfs(idx+2)

            return min(cost_1_step, cost_2_step)

        return min(dfs(0), dfs(1))