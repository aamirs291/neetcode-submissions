class Solution:
    def numDecodings(self, s: str) -> int:

        N = len(s)
        count = [0]

        def count_ways(idx):
            if idx==N:
                return 1
            
            if s[idx]=="0":
                return 0
            
            count = [0]
            
            count[0]+= count_ways(idx+1)

            if idx+1<N:
                if s[idx]=='1' or (s[idx]=='2' and s[idx+1] in '0123456'):
                    count[0]+= count_ways(idx+2)
            
            return count[0]
        
        return count_ways(0)



        