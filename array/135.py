class Solution:
    def candy(self, ratings: List[int]) -> int:
        lt = rt = 0
        res = 0
        while True:
            inc = True
            while rt < len(ratings) - 1 and ratings[rt+1] > ratings[rt]:
                rt += 1
            if rt == lt:
                while rt < len(ratings) - 1 and ratings[rt+1] < ratings[rt]:
                    rt += 1
                if rt != lt:
                    inc = False
            
            n = rt - lt + 1
            #print(lt, rt, n)
            if rt >= len(ratings) - 1:
                res += n * (n + 1) // 2
                break
            elif ratings[rt+1] == ratings[rt]:
                res += n * (n + 1) // 2
                lt = rt + 1
                rt = lt
                continue
            if not inc:
                if rt < len(ratings) - 1 and ratings[rt+1] > ratings[rt]:
                    res += n * (n + 1) // 2 - 1
                    lt = rt
                else:
                    res += n * (n + 1) // 2
                    lt = rt + 1
                    rt = lt
                continue
            cnt = rt
            while cnt < len(ratings) - 1 and ratings[cnt+1] < ratings[cnt]:
                cnt += 1
            nn = cnt - rt + 1
            if nn > n:
                res += n * (n - 1) // 2 + nn * (nn + 1) // 2
            else:
                res += n * (n + 1) // 2 + nn * (nn - 1) // 2
            if cnt < len(ratings) - 1 and ratings[cnt+1] > ratings[cnt]:
                res -= 1
                lt = rt = cnt
            elif cnt == len(ratings) - 1:
                break
            else:
                lt = rt = cnt + 1
        return res
                
