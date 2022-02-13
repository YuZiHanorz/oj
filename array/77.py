class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        
        def dfs(k: int, lt: int, ans: List[int]):
            if k == 0:
                res.append(ans)
                return
            if lt > n:
                return
            for i in range(lt, n+1):
                tmp = ans[:]
                tmp.append(i)
                dfs(k-1, i+1, tmp)
        dfs(k, 1, [])
        return res
