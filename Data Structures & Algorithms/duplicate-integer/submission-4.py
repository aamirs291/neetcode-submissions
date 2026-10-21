class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        duplicate_set = set()

        if len(nums)==0:
            return False
            
        duplicate_set.add(nums[0])

        for i in range(1, len(nums)):

            if(nums[i] in duplicate_set):
                return True
            
            duplicate_set.add(nums[i])
        
        return False

        