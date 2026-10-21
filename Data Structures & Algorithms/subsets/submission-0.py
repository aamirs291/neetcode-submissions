class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        temp = []
        res = []
        N = len(nums)

        def dfs(idx):
            if idx==N:
                res.append(temp.copy())
                return res
            
            dfs(idx+1)
            temp.append(nums[idx])
            dfs(idx+1)
            temp.pop()
        
        dfs(0)
        #print(res)

        return res

        