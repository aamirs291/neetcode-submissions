class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        N = len(grid)
        M = len(grid[0])

        visited = [[0 for j in range(M)] for i in range(N)]
        count = 0

        def dfs(row_idx, col_idx):

            if (row_idx<0 or row_idx==N) or (col_idx<0 or col_idx==M) or grid[row_idx][col_idx] == "0" or visited[row_idx][col_idx] == True:
                return
            
            visited[row_idx][col_idx]= True

            directions = [[0,1],[1,0],[0,-1],[-1,0]]
            for nr, nc in directions:
                r = row_idx + nr
                c = col_idx + nc

                dfs(r, c)
        
        count = 0
        for i in range(N):
            for j in range(M):
                if grid[i][j]=="1" and not visited[i][j]:
                    dfs(i,j)
                    count+=1
        
        return count





        