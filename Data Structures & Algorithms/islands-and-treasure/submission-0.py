class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        n = len(grid)
        m = len(grid[0])
        visit = [[False for j in range(m)] for i in range(n)]

        q = deque()

        def addCell(r, c):

            if (r<0 or r==n) or (c<0 or c==m) or visit[r][c]==True or grid[r][c]==-1:
                return

            visit[r][c] = True
            q.append([r,c])

        for r in range(n):
            for c in range(m):
                if grid[r][c]==0:
                    visit[r][c]=True
                    q.append([r,c])
        
        dist = 0

        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dist
                addCell(r+1, c)
                addCell(r-1,c)
                addCell(r, c+1)
                addCell(r,c-1)

            dist+=1
        
        # return grid
