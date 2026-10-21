class Solution:
    def climbStairs(self, n: int) -> int:

        dp = [-1 for i in range(n+1)]
        def numWays(n):

            if n==0 or n==1:
                dp[n] = 1
                return dp[n]
            
            if dp[n]!=-1:
                return dp[n]
            
            dp[n] = numWays(n-1) + numWays(n-2)
            return dp[n]

        numWays(n)
        return dp[n]
        