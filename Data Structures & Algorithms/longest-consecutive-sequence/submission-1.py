class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        hashmap = {}

        for i in range(len(nums)):
            hashmap[nums[i]] = hashmap.get(nums[i],0) + 1
        
        
        ans = 1
        for i in nums:
            length = 1
            if i-1 not in hashmap:
                while i+1 in hashmap:
                    length+=1
                    i+=1
                ans = max(ans, length)
        if len(nums)==0:
            return 0
        else: return ans


        