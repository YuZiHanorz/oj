class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        visited = [[0 for _ in range(n)] for _ in range(m)]
        cnt = 0
        
        def bfs(i: int, j: int):
            q = [(i,j)]
            visited[i][j] = 1
            while q:
                tmp = q.pop(0)
                x = tmp[0]; y = tmp[1]
                if x > 0 and grid[x-1][y] == '1' and not visited[x-1][y]:
                    visited[x-1][y] = 1
                    q.append((x-1, y))
                if x < m-1 and grid[x+1][y] == '1' and not visited[x+1][y]:
                    visited[x+1][y] = 1
                    q.append((x+1, y))
                if y > 0 and grid[x][y-1] == '1' and not visited[x][y-1]:
                    visited[x][y-1] = 1
                    q.append((x, y-1))
                if y < n-1 and grid[x][y+1] == '1' and not visited[x][y+1]:
                    visited[x][y+1] = 1
                    q.append((x, y+1))

                    
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and not visited[i][j]:
                    bfs(i, j)
                    cnt += 1
        return cnt
        
        
