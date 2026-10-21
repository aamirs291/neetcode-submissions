class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        visited = [[False for j in range(len(grid[0]))] for i in range(len(grid))]

        def bfs(row, col):

            q = deque()
            q.append((row, col))
            visited[row][col] = True

            while q:
                row, col = q.popleft()

                directions = [[0,1], [0,-1], [1,0], [-1, 0]]

                for dr, dc in directions:
                    r = row + dr
                    c = col + dc

                    if r in range(len(grid)) and c in range(len(grid[0])) and grid[r][c] =="1" and visited[r][c]==False:
                        q.append((r,c))
                        visited[r][c] = True
        
        count_islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=="1" and visited[i][j] == False:
                    count_islands +=1
                    bfs(i, j)

        return count_islands
        