def isValid(s_hashmap, t_hashmap):

    for i in t_hashmap:
        if i not in s_hashmap:
            return False
        if s_hashmap[i]<t_hashmap[i]:
            return False
    
    return True

class Solution:
    def minWindow(self, s: str, t: str) -> str:

        N = len(s)
        M = len(t)

        t_hashmap = {}
        for char in t:
            t_hashmap[char] = t_hashmap.get(char, 0) + 1
        
        s_hashmap = {}
        l = 0
        ans = ""
        length = N+1
        for r in range(N):
            s_hashmap[s[r]] = s_hashmap.get(s[r], 0) + 1

            while isValid(s_hashmap, t_hashmap):
                if r-l+1 < length:
                    ans = s[l:r+1]
                    length = r-l+1
                
                s_hashmap[s[l]]-=1
                if s_hashmap[s[l]]==0:
                    del s_hashmap[s[l]]
                
                l+=1
        return "" if length==N+1 else ans





        