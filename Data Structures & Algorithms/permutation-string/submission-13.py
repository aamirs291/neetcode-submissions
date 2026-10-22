class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        s1_map = {}

        for char in s1:
            s1_map[char] = s1_map.get(char, 0) + 1

        s2_map = {}
        
        l = 0
        k = len(s1)
        N = len(s2)

        if N<k:
            return False

        for r in range(k):
            s2_map[s2[r]] = s2_map.get(s2[r], 0) + 1

        if s1_map == s2_map:
                return True
        
        for i in range(1, N-k+1):
            s2_map[s2[i-1]]-=1
            if s2_map[s2[i-1]] == 0:
                del s2_map[s2[i-1]]
            
            s2_map[s2[i+k-1]] = s2_map.get(s2[i+k-1], 0) + 1

            if s1_map == s2_map:
                return True
        
        return False
            

