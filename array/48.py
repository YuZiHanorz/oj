class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n // 2):
            for j in range(n - 1 - 2 * i):
                tmp = matrix[i][i+j]
                matrix[i][i+j] = matrix[-i-1-j][i]
                matrix[-i-1-j][i] = matrix[-i-1][-i-j-1]
                matrix[-i-1][-i-j-1] = matrix[i+j][-i-1]
                matrix[i+j][-i-1] = tmp
            print(matrix)
