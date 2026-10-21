class Solution:
    def trap(self, height: List[int]) -> int:
        
        N = len(height)

        max_height = float("-inf")
        max_idx = 0

        for i in range(N):
            if height[i]>max_height:
                max_height = height[i]
                max_idx = i
        
        water_amt = 0
        left_max = float("-inf")
        for i in range(0, max_idx):
            if height[i]>left_max:
                left_max = height[i]
            water_amt += left_max - height[i]
        
        right_max = float("-inf")
        for i in range(N-1,max_idx,-1):
            if height[i]>right_max:
                right_max = height[i]
            water_amt += right_max - height[i]
        
        return water_amt

