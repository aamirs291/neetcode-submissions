class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        n = len(s)

        if n==0:
            return 0

        l = 0
        char_freq_map = {}

        length = 1
        max_length = 1

        for r in range(n):
            char = s[r]
            char_freq_map[char] = char_freq_map.get(char, 0) + 1

            while l<r and char_freq_map[char]>1:
                char_freq_map[s[l]]-=1
                l+=1
            
            max_length = max(max_length, r-l+1)

        
        return max_length



        