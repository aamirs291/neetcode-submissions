class Solution:
    def rob(self, nums: List[int]) -> int:
        
        n = len(nums)

        dp = [-1 for i in range(n)]

        def maxAmount(idx, end):

            if idx>=end:
                return 0
            
            if dp[idx]!=-1:
                return dp[idx]
            
            inc_amount = nums[idx] + maxAmount(idx+2,end)
            exc_amount = maxAmount(idx+1,end)

            max_amount = max(inc_amount, exc_amount)

            dp[idx] = max_amount

            return dp[idx]

        first_exc_max =  maxAmount(1, n)

        dp = [-1 for i in range(n)]
        last_exc_max =  maxAmount(0, n-1)

        return nums[0] if n==1 else max(first_exc_max, last_exc_max)