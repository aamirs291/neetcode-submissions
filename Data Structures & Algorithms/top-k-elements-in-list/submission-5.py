class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        res = []
        freq_map = {}
        num_map = {}

        n = len(nums)

        for num in nums:
            freq_map[num] = freq_map.get(num, 0) + 1
        
        for key, value in freq_map.items():
            num_map[value] = num_map.get(value, [])
            num_map[value].append(key)
        

        for i in range(n+1, -1, -1):
            if i not in num_map:
                continue
            for num in num_map[i]:
                res.append(num)
                if len(res)==k:
                    return res
        
        return res

                



        