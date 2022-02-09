class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res = [[]]
        res[0].append(1)
        for i in range(1, rowIndex+1):
            res.append([])
            res[i] = [1 for _ in range(i+1)]
            for j in range(1, i):
                res[i][j] = res[i-1][j-1] + res[i-1][j]
        return res[rowIndex]
                
