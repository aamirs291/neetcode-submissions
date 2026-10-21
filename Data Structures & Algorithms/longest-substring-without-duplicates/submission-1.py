class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        N = len(s)

        char_hashmap = {}
        l = 0
        max_length = 0

        for r in range(N):
            char_hashmap[s[r]] = char_hashmap.get(s[r], 0) + 1

            while l<r and char_hashmap[s[r]]>1:
                char_hashmap[s[l]]-=1
                l+=1
            
            max_length = max(max_length, r-l+1)

        return max_length


        