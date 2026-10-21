class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        res = []

        freq_map = {}

        for num in nums:
            freq_map[num] = freq_map.get(num, 0) + 1
        
        max_len = 0

        for key in freq_map:
            len = 1
            if key-1 not in freq_map:
                while key+len in freq_map:
                    len+=1
            
            if len>max_len:
                max_len = len
        
        return max_len


        