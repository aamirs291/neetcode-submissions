class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        r = len(nums) - 1
        res = []

        for i in range(len(nums)):
            if nums[i]>0:
                break
            if i>0 and nums[i]==nums[i-1]:
                continue
            l = i+1
            r = len(nums) - 1
            target = abs(nums[i])
            
            while l<r:
                sum = nums[l] + nums[r]
                if sum == target:
                    res.append([nums[i],nums[l],nums[r]])
                    l+=1
                    r-=1
                    while nums[l]==nums[l-1] and l<r:
                        l+=1
                elif sum< target:
                    l+=1
                else:
                    r-=1
        
        return res


        