class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        sum = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    sum[i][j] = grid[i][j]
                elif i == 0:
                    sum[i][j] = grid[i][j] + sum[i][j-1]
                elif j == 0:
                    sum[i][j] = grid[i][j] + sum[i-1][j]
                else:
                    sum[i][j] = min(sum[i-1][j], sum[i][j-1]) + grid[i][j]
        return sum[-1][-1]
