class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        N = len(nums)
        lis = [1 for i in range(N)]
        overall_max = float("-inf")

        for i in range(N):
            max_val = 0
            for j in range(i):
                if nums[j]<nums[i]:
                    max_val = max(max_val, lis[j])
                
            lis[i] = 1 + max_val
        
            if lis[i]>overall_max:
                overall_max = lis[i]
        
        return overall_max

