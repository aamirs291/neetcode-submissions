class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        N = len(matrix)
        M = len(matrix[0])
        
        l = 0
        r = M-1
        
        top = 0
        bot = N-1

        mid_row = 0
        while top<=bot:

            mid_row = top + (bot-top)//2

            if target > matrix[mid_row][-1]:
                top = mid_row + 1
            elif target < matrix[mid_row][0]:
                bot = mid_row - 1
            else:
                break
        if top>bot:
            return False        
        
        #row = matrix[top]

        while l<=r:
            mid = l + (r-l)//2

            if matrix[mid_row][mid] == target:
                return True
            elif matrix[mid_row][mid] < target:
                l = mid+1
            else:
                r = mid-1
        
        return False