class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        nums = candidates
        N = len(nums)
        curr_sum = 0
        temp = []
        res = []
        nums.sort()

        def dfs(idx, curr_sum):
            if curr_sum==target:
                res.append(temp.copy())
                return
            if curr_sum>target or idx==N:
                return
            
            for i in range(idx, N):
                if i>idx and nums[i]==nums[i-1]:
                    continue
                
                temp.append(nums[i])
                dfs(i+1, curr_sum + nums[i])
                temp.pop()
            
        dfs(0, 0)
        return res
