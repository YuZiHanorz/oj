class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[]]
        res[0].append(1)
        for i in range(1, numRows):
            res.append([])
            res[i] = [1 for x in range(i+1)]
            for j in range(1, i):
                res[i][j] = res[i-1][j-1] + res[i-1][j]
        return res
                
