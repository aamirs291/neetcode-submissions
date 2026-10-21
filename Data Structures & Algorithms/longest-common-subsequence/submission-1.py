class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        s1 = text1
        s2 = text2

        N = len(s1)
        M = len(s2)
        dp = [[0 for j in range(M)] for i in range(N)]

        def lcs(s1_idx, s2_idx):
            if s1_idx==N or s2_idx==M:
                return 0
            if dp[s1_idx][s2_idx]!=0:
                return dp[s1_idx][s2_idx]

            length = 0
            if s1[s1_idx]==s2[s2_idx]:
                length = 1 + lcs(s1_idx+1, s2_idx+1)
            else:
                length += max(lcs(s1_idx+1, s2_idx), lcs(s1_idx, s2_idx+1))
            
            dp[s1_idx][s2_idx] = length
            return dp[s1_idx][s2_idx]
        
        return lcs(0,0)
        