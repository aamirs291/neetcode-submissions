class Solution:
    def longestPalindrome(self, s: str) -> str:

        N = len(s)
        dp = [[False for j in range(N)] for i in range(N)]
        output = ""
        max_len = 1

        for length in range(1, N+1):
            for i in range(N):
                j = length + i -1
                if j>=N:
                    continue
                if length==1:
                    dp[i][j] = True
                elif length==2:
                    if s[i]==s[j]:
                        dp[i][j]=True
                else:
                    if s[i]==s[j] and dp[i+1][j-1]:
                        dp[i][j] = True
                
                if dp[i][j] and max_len>=1:
                    output = s[i:j+1]
                    max_len = j-i+1
        
        return output


        