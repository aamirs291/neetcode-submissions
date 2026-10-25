class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        n = len(candidates)

        temp = []
        res = []
        candidates.sort()

        def comb_sum(idx, curr_sum):

            if curr_sum>target:
                return
            
            if curr_sum == target:
                res.append(temp.copy())
                return
            
            for i in range(idx, n):
                if i>idx and candidates[i-1]==candidates[i]:
                    continue
                
                temp.append(candidates[i])
                comb_sum(i+1, curr_sum + candidates[i])
                temp.pop()
            
        comb_sum(0, 0)

        return res

