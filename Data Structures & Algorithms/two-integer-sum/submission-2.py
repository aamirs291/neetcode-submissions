class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        traverse_map = {}

        for i in range(len(nums)):
            diff = target - nums[i]

            if diff in traverse_map:
                return [traverse_map[diff],i]
            
            traverse_map[nums[i]] = i
        