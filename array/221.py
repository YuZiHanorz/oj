class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        last = [-1 for _ in range(n)] #每一列的上一个0
        lastj = -1 #每一行的上一个0
        maxlen = 0
        maxa = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            lastj = -1
            for j in range(n):
                if matrix[i][j] == '0':
                    last[j] = i
                    lastj = j
                    continue
                if i == 0 or j == 0:
                    maxa[i][j] = 1
                else:
                    le = min(j - lastj, i - last[j])
                    maxa[i][j] = min(le, maxa[i-1][j-1]+1)
                maxlen = max(maxlen, maxa[i][j])
        return maxlen ** 2
