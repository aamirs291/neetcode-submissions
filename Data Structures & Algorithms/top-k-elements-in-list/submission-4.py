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
            if i in num_map:
                values = num_map[i]
                idx = 0
                val_len = len(values)
                while idx<val_len and k>0:
                    res.append(values[idx])
                    k-=1
                    idx+=1
                if k==0:
                    return res
        
        return res

                



        