class Solution:
    def climbStairs(self, n: int) -> int:

        count = [0]

        def num_ways(idx):
            if idx<0:
                return 0
            
            if idx<=2:
                return idx
            
            return (num_ways(idx-1) + num_ways(idx-2))

        
        #return num_ways(n)

        dp = [-1 for i in range(n+1)]

        for idx in range(n+1):

            if idx<=2:
                dp[idx] = idx
            else:
                dp[idx] = dp[idx-1] + dp[idx-2]
        
        #return dp[n]

        if n<=3:
            return n
        
        n1, n2 = 2, 3

        for i in range(4, n+1):
            temp = n1+n2
            n1 = n2
            n2 = temp
        
        return temp


        