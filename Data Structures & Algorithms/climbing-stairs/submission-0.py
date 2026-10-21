class Solution:
    def climbStairs(self, n: int) -> int:
        ans = [0]
        
        def dfs(num):
            if num==n:
                ans[0]+=1
                return ans[0]
            
            if num>n:
                return 0
            
            return dfs(num+1) + dfs(num+2)
        
        dfs(0)
        return ans[0]


        