import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        l = 1
        r = max(piles)
        ans = float("inf")

        while l<=r:

            mid = l + (r-l)//2

            if self.isValid(mid, h, piles):
                ans = min(ans, mid)
                r = mid-1
            else:
                l = mid+1
            
        return ans

    def isValid(self, mid, h, piles):

        hours_taken = 0
        for pile in piles:
            hours_taken+= math.ceil(pile/mid)
        
            if hours_taken>h:
                return False
        
        return True


