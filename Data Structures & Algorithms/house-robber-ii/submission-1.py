class Solution:
    def rob(self, nums: List[int]) -> int:
        
        N = len(nums)
        dp = [-1 for i in range(N)]

        def dfs(idx, end):
            if idx>=end:
                return 0
            if dp[idx]!=-1:
                return dp[idx]

            inc = nums[idx] + dfs(idx+2, end)
            exc = dfs(idx+1, end)

            dp[idx] = max(inc, exc)
            return dp[idx]

        first_exc_max = dfs(1, N)
        #print(dp, first_exc_max)
        dp = [-1 for i in range(N)]
        last_exc_max = dfs(0, N-1)
        #print(dp, last_exc_max)
        return nums[0] if N==1 else max(first_exc_max, last_exc_max)


        