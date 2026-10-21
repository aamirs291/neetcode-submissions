class Solution:
    def countSubstrings(self, s: str) -> int:

        N = len(s)
        dp = [[False for j in range(N)] for i in range(N)]
        count = 0

        for length in range(1, N+1):
            for i in range(N):
                j = length + i - 1

                if j>=N:
                    continue
                
                if length==1:
                    dp[i][j] = True
                
                elif length==2:
                    if s[i]==s[j]:
                        dp[i][j]= True
                else:
                    if s[i]==s[j] and dp[i+1][j-1]:
                        dp[i][j] = True
                
                if dp[i][j]:
                    count+=1
        print(dp)
        return count
        