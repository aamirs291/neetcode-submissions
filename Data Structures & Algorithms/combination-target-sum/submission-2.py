class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        temp = []
        res = []
        curr_sum = 0

        def dfs(idx, curr_sum, temp):

            if curr_sum==target:
                res.append(temp.copy())
                return
            
            if idx==len(nums) or curr_sum>target:
                return 

            temp.append(nums[idx])
            dfs(idx, curr_sum+nums[idx], temp)
            temp.pop()
            dfs(idx+1, curr_sum, temp)
        
        dfs(0, curr_sum, temp)

        return res




        