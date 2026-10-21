class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        N = len(heights)
        stack = []
        maxArea = 0

        for idx, h in enumerate(heights):
            start = idx
            while stack and stack[-1][1]>h:
                s_idx, height = stack.pop()
                maxArea = max(maxArea, height * (idx-s_idx))
                start = s_idx
            stack.append((start, h))
        
        for i,h in stack:
            maxArea = max(maxArea, (N-i)*h)
        
        return maxArea



        