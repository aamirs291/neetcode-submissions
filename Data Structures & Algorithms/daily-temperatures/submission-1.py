class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        '''
        Input: temperatures = [30,38,30,36,35,40,28]

        Output: [1,4,1,2,1,0,0] '''
        temp = temperatures
        res = [0]*len(temp)
        stack = []
        pair = [(idx,val) for idx,val in enumerate(temp)]

        for i in range(len(temp)):
            while stack and temp[i]>stack[-1][1]:
                s_idx, val = stack.pop()
                res[s_idx] = i-s_idx
                print(i, s_idx,res[s_idx])
            
            stack.append((i, temp[i]))
        
        return res

