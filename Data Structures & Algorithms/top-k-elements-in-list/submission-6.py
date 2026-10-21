class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        n = len(nums)

        res = [0] * (n+1)

        freq_map = {}

        res = []

        for num in nums:
            freq_map[num] = freq_map.get(num, 0) + 1
        
        value_freq_map = {}
        for key,value in freq_map.items():
            value_freq_map[value] = value_freq_map.get(value, [])
            value_freq_map[value].append(key)
        

        for i in range(n+1,-1,-1):
            if i not in value_freq_map:
                continue
            
            for num in value_freq_map[i]:
                res.append(num)
                k-=1
                if k==0:
                    return res
        
        return res

        