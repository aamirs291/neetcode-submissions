class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        s1_char_freq = {}
        k = len(s1)

        for char in s1:
            s1_char_freq[char] = s1_char_freq.get(char, 0) + 1
        
        N = len(s2)

        if N<k:
            return False
            
        s2_char_freq = {}
        for i in range(k):
            s2_char_freq[s2[i]] = s2_char_freq.get(s2[i],0) + 1
        
        if s1_char_freq == s2_char_freq:
            return True
        
        for i in range(1, N-k+1):
            s2_char_freq[s2[i-1]]-=1
            if s2_char_freq[s2[i-1]]==0:
                del s2_char_freq[s2[i-1]]
            
            s2_char_freq[s2[i+k-1]] = s2_char_freq.get(s2[i+k-1],0) + 1
            if s1_char_freq == s2_char_freq:
                return True
        
        return False


        