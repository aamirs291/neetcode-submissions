class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        stack = []
        maxArea = float("-inf")
        N = len(heights)
        
        for idx, h in enumerate(heights):
            start = idx

            while stack and stack[-1][1]>h:
                s_idx, height = stack.pop()
                maxArea = max(maxArea, (idx-s_idx)*height)
                start = s_idx
            
            stack.append((start, h))

        for idx, h in stack:
            maxArea = max(maxArea, (N-idx)*h)
        
        return maxArea


        