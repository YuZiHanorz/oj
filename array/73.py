class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        rflag = False; cflag = False
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0 #two marker
                    if i == 0 and not rflag:
                        rflag = True
                    if j == 0 and not cflag:
                        cflag = True
        for i in range(1, m):
            if matrix[i][0] == 0:
                for j in range(n):
                    matrix[i][j] = 0
        for j in range(1, n):
            if matrix[0][j] == 0:
                for i in range(m):
                    matrix[i][j] = 0
        if rflag:
            for j in range(n):
                matrix[0][j] = 0
        if cflag:
            for i in range(m):
                matrix[i][0] = 0
