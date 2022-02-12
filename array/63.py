class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        res = [[1 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    if obstacleGrid[i][j]:
                        res[i][j] = 0
                    else:
                        res[i][j] = 1
                elif i == 0:
                    if obstacleGrid[i][j]:
                        res[i][j] = 0
                    else:
                        res[i][j] = res[i][j-1]
                elif j == 0:
                    if obstacleGrid[i][j]:
                        res[i][j] = 0
                    else:
                        res[i][j] = res[i-1][j]
                else:
                    if obstacleGrid[i][j]:
                        res[i][j] = 0
                    else:
                        res[i][j] = res[i-1][j] + res[i][j-1]
        return res[m-1][n-1]
                    
                
