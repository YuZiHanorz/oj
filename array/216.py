class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        def dfs(k: int, s: int, st: int, com: List[int]):
            if s == 0 and k == 0:
                res.append(com)
                return
            if k > 9 - st + 1 or s <= 0:
                return
            tmp = com[:]
            dfs(k, s, st+1, tmp)
            tmp = com[:]
            tmp.append(st)
            dfs(k-1, s-st, st+1, tmp)
        dfs(k, n, 1, [])
        return res
