class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        s1 = word1
        s2 = word2
        n = len(s1)
        m = len(s2)

        # print(n,m)
        # return 0
        dp = [[-1 for j in range(m)] for i in range(n)]

        def min_edit(s1_idx, s2_idx):
            if s1_idx==n:
                return m-s2_idx
            if s2_idx==m:
                return n-s1_idx
            
            if dp[s1_idx][s2_idx]!=-1:
                return dp[s1_idx][s2_idx]

            if s1[s1_idx]==s2[s2_idx]:
                dp[s1_idx][s2_idx] = min_edit(s1_idx+1, s2_idx+1)
                return dp[s1_idx][s2_idx]
            else:
                insert = 1 + min_edit(s1_idx, s2_idx+1)
                replace = 1 + min_edit(s1_idx+1, s2_idx+1)
                delete = 1 + min_edit(s1_idx+1, s2_idx)

                dp[s1_idx][s2_idx] = min(insert, replace, delete)
                return dp[s1_idx][s2_idx]
        
        return min_edit(0, 0)
            
            

        