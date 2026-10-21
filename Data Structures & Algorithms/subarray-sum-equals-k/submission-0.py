class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        n = len(nums)
        sum_map = {}

        sum_map[0] = 1
        res = 0

        currSum = 0
        for i in range(n):
            currSum+= nums[i]
            if currSum-k in sum_map:
                res += sum_map[currSum-k]

            sum_map[currSum] = sum_map.get(currSum, 0) + 1

        return res 

        