class Solution:
    def maxArea(self, heights: List[int]) -> int:

        N = len(heights)
        l = 0
        r = N-1
        amt = 0
        max_amt = float("-inf")
        for i in range(N):
            amt = (r-l)* min(heights[l],heights[r])
            max_amt = max(amt, max_amt)

            if heights[l]<heights[r]:
                l+=1
            elif heights[l]>heights[r]:
                r-=1
            else:
                l+=1
        
        return max_amt
        