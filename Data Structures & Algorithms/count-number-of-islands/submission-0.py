class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        visited = [[ False for j in range(len(grid[0]))] for i in range(len(grid))]

        def island_dfs(row, col):

            if (row<0 or row==len(grid)) or (col<0 or col==len(grid[0])) or grid[row][col]=="0" or visited[row][col]==True:
                return
            
            visited[row][col] = True

            directions = [[1,0],[-1,0],[0,1],[0,-1]]

            for dr, dc in directions:
                r = row + dr
                c = col + dc

                #if visited[r][c]==False:
                island_dfs(r, c)

        island_count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=="1" and visited[i][j]==False:
                    island_dfs(i,j)
                    island_count+=1
        
        #print(visited)
        return island_count

