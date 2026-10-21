class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        n = len(heights)
        m = len(heights[0])

        pac_visited = [[False for j in range(m)] for i in range(n)]
        atl_visited = [[False for j in range(m)] for i in range(n)]

        dirs = [[0,1],[0,-1],[1,0],[-1,0]]

        def bfs(source, visited):
            q = deque(source)
            while q:
                r, c = q.popleft()
                visited[r][c] = True

                for dr, dc in dirs:
                    nr = r + dr
                    nc = c + dc

                    if(0<=nr<n) and (0<=nc<m) and visited[nr][nc]==False and heights[nr][nc]>=heights[r][c]:
                        q.append([nr,nc])

        
        pacific_entries = []
        atlantic_entries = []

        for c in range(m):
            pacific_entries.append([0,c])
            atlantic_entries.append([n-1,c])
        
        for r in range(n):
            pacific_entries.append([r,0])
            atlantic_entries.append([r,m-1])

        bfs(pacific_entries, pac_visited)
        bfs(atlantic_entries, atl_visited)

        res = []

        for r in range(n):
            for c in range(m):
                if pac_visited[r][c] and atl_visited[r][c]:
                    res.append([r,c])
        return res
