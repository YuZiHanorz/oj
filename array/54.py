class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix); n = len(matrix[0])
        res = []
        for i in range(math.ceil(min(m, n) / 2)):
            num = (m + n - 2 - 4 * i) * 2
            if min(m , n) - 1 -2 * i == 0:
                num = max(m, n) - 2 * i
            for j in range(num):
                up = n - 2 * i - 1
                right = n + m - 4 * i - 2
                down = 2 * n + m - 6 * i - 3 
                print(i , j, up, right, down)
                if j < up:
                    res.append(matrix[i][i+j])
                elif j < right:
                    res.append(matrix[i+j-up][-i-1])
                elif j < down:
                    res.append(matrix[-i-1][-i-j-1+right])
                else:
                    res.append(matrix[-i-j-1+down][i])
        return res
