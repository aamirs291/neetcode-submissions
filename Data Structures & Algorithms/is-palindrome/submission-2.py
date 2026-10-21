def alpha_num(char):
    
    return ( ord('A') <= ord(char) <= ord('Z') ) or ((ord('a') <= ord(char) <= ord('z'))) or (ord('0') <= ord(char) <= ord('9'))

class Solution:
    def isPalindrome(self, s: str) -> bool:

        l = 0
        r = len(s) - 1

        while l<r:

            while l<r and alpha_num(s[l])==False:
                l+=1
            while r>l and alpha_num(s[r])==False:
                r-=1
            
            if s[l].lower() != s[r].lower():
                return False

            l+=1
            r-=1

        return True
            
        