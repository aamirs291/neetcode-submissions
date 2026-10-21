class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        N = len(nums)
        inc = [0]

        def lis(idx, nxt):
            if idx<0:
                return 0
            
            exc = lis(idx-1, nxt)
            inc[0] = 0
            if nxt==N or nums[idx] < nums[nxt]:
                inc[0] = 1 + lis(idx-1,idx)

            return max(exc,inc[0])
        
        return lis(N-1, N)
        