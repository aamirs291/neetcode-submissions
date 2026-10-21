class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        temp = []
        res = []
        curr_sum = 0
        N = len(nums)

        def comb_sum(curr_sum, idx):
            if curr_sum ==target:
                res.append(temp.copy())
                return
            if curr_sum > target or idx==N:
                return
            
            temp.append(nums[idx])
            curr_sum+= nums[idx]
            comb_sum(curr_sum,idx)
            curr_sum-=nums[idx]
            temp.pop()
            comb_sum(curr_sum,idx+1)
        
        comb_sum(0, 0)
        return res

        