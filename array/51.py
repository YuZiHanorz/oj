class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        col = [0 for _ in range(n)]
        ld = [0 for _ in range(2*n-1)]
        rd = [0 for _ in range(2*n-1)]
        
        def dfs(i: int, ans: List[int]): # put row i
            if i == n:
                tmp = ["." * n for _ in range(n)] 
                for j in range(n):
                    t = tmp[j][:ans[j]] + 'Q' + tmp[j][ans[j]+1:]# str cannot change
                    tmp[j] = t
                res.append(tmp)
                return
            for j in range(n): # row i, col j
                if col[j] or ld[i+j] or rd[i+n-1-j]:
                    continue
                col[j] = ld[i+j] = rd[i+n-1-j] = 1
                tmp = ans[:]
                tmp.append(j)
                dfs(i + 1, tmp)
                col[j] = ld[i+j] = rd[i+n-1-j] = 0
        dfs(0, [])
        return res
                
