class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        num_map = {}
        if not nums:
            return 0
    
        for num in nums:
            num_map[num] = num_map.get(num, 0) + 1

        max_length = 1

        for key in num_map:
            length = 1
            if key-1 not in num_map:
                while key+length in num_map:
                    length+=1
                    max_length = max(max_length, length)
        
        return max_length



        