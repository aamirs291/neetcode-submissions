class Solution:
    def numDecodings(self, s: str) -> int:

        N = len(s)
        count = [0]
        dp = [-1 for i in range(N)]

        def count_ways(idx):
            if idx==N:
                return 1
            
            if s[idx]=="0":
                return 0
            
            if dp[idx]!=-1:
                return dp[idx]
            
            count = [0]
            
            count[0]+= count_ways(idx+1)

            if idx+1<N:
                if s[idx]=='1' or (s[idx]=='2' and s[idx+1] in '0123456'):
                    count[0]+= count_ways(idx+2)
            
            dp[idx] = count[0]
            return dp[idx]
        
        return count_ways(0)



        