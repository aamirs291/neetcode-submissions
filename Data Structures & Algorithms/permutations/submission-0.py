class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        res = []
        temp = []
        visited = [False for i in range(len(nums))]
        N = len(nums)

        def perm_gen(idx):
            if len(temp)==N:
                res.append(temp.copy())
                return
            
            for i in range(N):
                if not visited[i]:
                    visited[i]= True
                    temp.append(nums[i])
                    perm_gen(i+1)
                    temp.pop()
                    visited[i] = False
            
        perm_gen(0)

        return res


        