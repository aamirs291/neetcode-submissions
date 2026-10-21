from math import ceil

def isValid(mid, piles, h):
    
    time_taken = 0
    for i in piles:
        time_taken += ceil(i/mid)
        if time_taken>h:
            return False
    
    return True

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        l = 1
        r = max(piles)
        ans = float("inf")
        while l<=r:
            mid = l + (r-l)//2
            if isValid(mid, piles, h):
                ans = min(ans, mid)
                r = mid-1
            else:
                l = mid+1
        
        return ans
            



