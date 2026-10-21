class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        temp = []
        res = []
        visited = [False for _ in range(len(nums))]

        def dfs(i, temp):
            
            if len(temp) == len(nums):
                res.append(temp.copy())
                return
            
            for i in range(len(nums)):
                if visited[i]==False:
                    temp.append(nums[i])
                    visited[i] = True
                    dfs(i + 1, temp)
                    temp.pop()
                    visited[i] = False
        
        dfs(0, temp)

        return res



