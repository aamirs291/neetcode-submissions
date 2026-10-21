class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        

        N = len(grid)
        M = len(grid[0])
        
        q = deque([])
        fresh_count = 0
        for i in range(N):
            for j in range(M):
                if grid[i][j]==1:
                    fresh_count+=1
                if grid[i][j]==2:
                    q.append([i,j])
        
        dirs = [[1,0],[-1,0],[0,1],[0,-1]]

        time = 0
        while fresh_count> 0 and q:
            length = len(q)
            for i in range(length):
                curr_rotten_r, curr_rotten_c  = q.popleft()

                for nr,nc in dirs:
                    r = curr_rotten_r + nr
                    c = curr_rotten_c + nc

                    if (r>=0 and r<N) and (c>=0 and c<M) and grid[r][c]==1:
                        grid[r][c]=2
                        fresh_count-=1
                        q.append([r,c])
            
            time+=1
        
        return -1 if fresh_count!=0 else time


