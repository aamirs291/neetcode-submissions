class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        s_freq = [0]*26
        t_freq = [0]*26

        if len(s)!=len(t):
            return False

        for i in range(len(s)):
            s_idx = ord(s[i]) - ord('a')
            t_idx = ord(t[i]) - ord('a')

            s_freq[s_idx] += 1
            t_freq[t_idx] += 1
        
        if s_freq == t_freq:
            return True
        else:
            return False
        
        