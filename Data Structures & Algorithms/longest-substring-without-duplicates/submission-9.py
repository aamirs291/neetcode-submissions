class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        l = 0
        n = len(s)
        freq_map = {}
        max_len = 0

        for r in range(n):
            char = s[r]
            freq_map[char] = freq_map.get(char, 0) + 1

            while l<r and freq_map[char]>1:
                freq_map[s[l]] -=1    
                l+=1
            
            # freq_map[char] -=1
            max_len = max(max_len, r-l+1)
        
        return max_len

