class Solution:
    def longestPalindrome(self, s: str) -> str:

        n = len(s)

        dp = [[False for i in range(n)] for j in range(n)]

        max_len = 0
        ans = ""

        for gap in range(n):
            for j in range(gap, n):
                i = j - gap
                length = j-i+1

                if gap==0:
                    dp[i][j] = True
                
                elif gap==1:
                    if s[i]==s[j]:
                        dp[i][j] = True
                
                else:
                    if s[i]==s[j]:
                        dp[i][j] = dp[i+1][j-1]

                if dp[i][j]:
                    if length>max_len:
                        max_len = length
                        ans = s[i:j+1]
                    # max_len = max(max_len, length)
        
        return ans




        