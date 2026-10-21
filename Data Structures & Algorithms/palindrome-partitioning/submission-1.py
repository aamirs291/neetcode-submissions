class Solution:
    def isPali(self, s, idx, i):
        while idx<=i:
            if s[idx]==s[i]:
                idx+=1
                i-=1
            else:
                return False
        
        return True
    def partition(self, s: str) -> List[List[str]]:

        N = len(s)
        temp = []
        res = []

        def dfs(idx):
            if idx==N:
                res.append(temp.copy())
                return
            
            for i in range(idx, N):
                if self.isPali(s, idx, i):
                    temp.append(s[idx:i+1])
                    dfs(i+1)
                    temp.pop()
                

        dfs(0)
        return res
        