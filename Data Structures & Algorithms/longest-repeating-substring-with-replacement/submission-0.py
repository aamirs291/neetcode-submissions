class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        N = len(s)

        char_hashmap = {}
        l = 0
        max_len = 0

        for r in range(N):
            char_hashmap[s[r]] = char_hashmap.get(s[r], 0) + 1

            while (r-l+1) - max(char_hashmap.values()) > k:
                char_hashmap[s[l]] -=1
                l+=1
            
            max_len = max(max_len, r-l+1)
        
        return max_len
