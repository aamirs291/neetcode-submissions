class Solution:
    def rob(self, nums: List[int]) -> int:

        n = len(nums)

        dp = [-1 for i in range(n)]

        def maxAmount(idx):

            if idx>=n:
                return 0
            
            if dp[idx]!=-1:
                return dp[idx]
            
            inc_amount = nums[idx] + maxAmount(idx+2)
            exc_amount = maxAmount(idx+1)

            max_amount = max(inc_amount, exc_amount)

            dp[idx] = max_amount

            return dp[idx]

        maxAmount(0)

        return dp[0]



        