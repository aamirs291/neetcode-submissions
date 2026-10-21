class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        hashmap = {}

        for i in nums:
            hashmap[i] = hashmap.get(i, 0) + 1
        
        for i in hashmap:
            if hashmap[i] >1:
                return True
        
        return False
         