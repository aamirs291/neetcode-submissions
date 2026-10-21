class Solution:
    def rob(self, nums: List[int]) -> int:

        N = len(nums)
        dp = [-1 for i in range(N)]
        
        def dfs(idx):
            if idx<0:
                return 0
            if dp[idx]!=-1:
                return dp[idx]

            non_adj_0 = nums[idx] + dfs(idx-2)
            # non_adj_1 = max(dfs(idx-1), dfs(idx-2))
            non_adj_1 = dfs(idx-1)
            
            dp[idx] = max(non_adj_0, non_adj_1)
            return dp[idx]
        
        dfs(N-1)
        return max(dp[N-1], dp[N-2])

        



        