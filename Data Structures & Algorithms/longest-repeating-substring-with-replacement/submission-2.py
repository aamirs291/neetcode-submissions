class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        n = len(s)

        if n==0:
            return 0
        
        l = 0
        char_freq_map = {}
        max_len = 1

        for r in range(n):
            char = s[r]
            char_freq_map[char] = char_freq_map.get(char, 0)+ 1

            while ((r-l+1) - max(char_freq_map.values())) > k:
                char_freq_map[s[l]] -=1
                if char_freq_map[s[l]]==0:
                    del char_freq_map[s[l]]
                l+=1
                
            max_len = max(max_len, r-l+1)
        
        return max_len


        