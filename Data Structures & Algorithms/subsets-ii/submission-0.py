class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        
        temp = []
        res = []
        N = len(nums)

        def dfs(idx):
            if idx==N:
                res.append(temp.copy())
                return
            
            temp.append(nums[idx])
            dfs(idx+1)
            temp.pop()

            while idx<N-1 and nums[idx]==nums[idx+1]:
                idx+=1
            dfs(idx+1)
        
        dfs(0)
        #print(res)

        return res
            

        