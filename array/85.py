class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        h = [[0 for _ in range(n+1)] for _ in range(m)]
        maxa = 0
        for i in range(m):
            for j in range(n+1):
                if j == n:
                    h[i][j] = -1
                    continue
                if matrix[i][j] == '1':
                    if i == 0:
                        h[i][j] = 1
                    else:
                        h[i][j] = h[i-1][j] + 1
        for i in range(m):
            ms = []
            for j in range(n+1):
                while ms and h[i][j] < h[i][ms[-1]]:
                    idx = ms.pop(-1)
                    height = h[i][idx]
                    width = j - ms[-1] - 1 if ms else j
                    maxa = max(maxa, height * width)
                ms.append(j)
        return maxa
