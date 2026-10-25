class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        n = len(nums)
        temp = []
        res = []

        idx = 0

        def dfs(idx):

            if idx==n:
                res.append(temp.copy())
                return
            
            temp.append(nums[idx])
            dfs(idx+1)
            temp.pop()
            dfs(idx+1)

        
        dfs(idx)

        return res