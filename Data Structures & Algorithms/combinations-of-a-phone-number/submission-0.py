class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        digit_alpha_mapping = {2:'abc', 3:'def', 4:'ghi', 5:'jkl', 
        6:'mno', 7:'pqrs', 8:'tuv', 9:'wxyz'}

        temp = []
        res = []
        # N = len(digits)

        def comb_gen(idx):

            if len(temp)==len(digits):
                res.append("".join(temp.copy()))
                return

            for i in range(idx,len(digits)):
                letters = digit_alpha_mapping[int(digits[i])]
                N = len(letters)
                for j in range(N):
                    temp.append(letters[j])
                    comb_gen(i+1)
                    temp.pop()
            
        if digits:
            comb_gen(0)
        
        return res

        