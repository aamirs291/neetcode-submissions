class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        rows = len(grid)
        cols = len(grid[0])

        visited = [[False for j in range(cols)] for i in range(rows)]

        def dfs(row, col):

            if row not in range(rows) or col not in range(cols) or grid[row][col]==0 or visited[row][col]==True:

                return 0
            
            visited[row][col] = True

            ans = 1
            directions = [[0,1],[0,-1],[1,0],[-1,0]]

            for dr, dc in directions:
                r = row + dr
                c = col + dc

                ans += dfs(r, c)
            
            return ans

        max_area = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==1 and visited[i][j]==False:
                    max_area = max(max_area, dfs(i,j))
        
        return max_area

        