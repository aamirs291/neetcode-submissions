class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0]*len(temperatures)
        temp = temperatures

        for i in range(len(temp)):
            while stack and temp[i]>stack[-1][1]:
                s_idx, s_val = stack.pop()
                res[s_idx] = i-s_idx
            
            stack.append((i, temp[i]))
        
        return res


        