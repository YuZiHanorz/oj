class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0 for _ in range(n)] for _ in range(n)]
        cnt = 0
        for i in range(math.ceil(n / 2)):
            num = (2 * n - 2 - 4 * i) * 2
            if n - 1 -2 * i == 0:
                num = n - 2 * i
            for j in range(num):
                cnt += 1
                up = n - 2 * i - 1
                right = n + n - 4 * i - 2
                down = 2 * n + n - 6 * i - 3
                if j < up:
                    matrix[i][i+j] = cnt
                elif j < right:
                    matrix[i+j-up][-i-1] = cnt
                elif j < down:
                    matrix[-i-1][-i-j-1+right] = cnt
                else:
                    matrix[-i-j-1+down][i] = cnt
        return matrix
