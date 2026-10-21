class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        #1,1,2,8
        #48,24,6,1

        n = len(nums)
        l_start = 1
        r_start = 1
        res = [1]*n
        
        for i in range(n):
            res[i] = l_start
            l_start*=nums[i]
        
        for j in range(n-1,-1,-1):
            res[j] *=r_start
            r_start *=nums[j] 

        print(res)
        return res


