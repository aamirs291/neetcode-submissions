def nearestsmallerleft(arr):

    stack = []
    N = len(arr)
    res = [0]*N
    
    for el_idx in range(N):
        while stack and arr[el_idx] < arr[stack[-1]]:
            stack.pop()
        if stack:
            res[el_idx] = stack[-1]
        else:
            res[el_idx] = -1
        
        stack.append(el_idx)

    return res

def nearestsmallerright(arr):

    stack = []
    N = len(arr)
    res = [0]*N

    for el_idx in range(N-1, -1, -1):
        while stack and arr[el_idx] <= arr[stack[-1]]:
            stack.pop()
        if stack:
            res[el_idx] = stack[-1]
        else:
            res[el_idx] = N
        
        stack.append(el_idx)

    return res
    

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        nearest_smaller_left_val_arr = nearestsmallerleft(heights)
        nearest_smaller_right_val_arr = nearestsmallerright(heights)

        max_area = float("-inf")
        for i in range(len(heights)):
            base = nearest_smaller_right_val_arr[i] - nearest_smaller_left_val_arr[i] - 1
            max_area = max(max_area, base*heights[i])
        
        return max_area

        