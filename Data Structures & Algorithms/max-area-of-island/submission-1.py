class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        rows = len(grid)
        cols = len(grid[0])

        visited = [[False for j in range(cols)] for i in range(rows)]

        def bfs(row, col):

            q = deque()

            q.append((row, col))
            visited[row][col]=True

            area = 1

            while q:
                row, col = q.popleft()
                
                directions = [[0,1],[0,-1],[1,0],[-1,0]]

                for dr, dc in directions:
                    r = row + dr
                    c = col + dc

                    if r in range(rows) and c in range(cols) and visited[r][c]==False and grid[r][c]==1:
                        area+=1
                        q.append((r,c))
                        visited[r][c]=True
                
            return area

        max_area = 0
        #area = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==1 and visited[i][j]==False:
                    max_area = max(max_area, bfs(i,j))
        
        return max_area


        