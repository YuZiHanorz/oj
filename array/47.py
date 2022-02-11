class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        prev = []
        nums.sort()
        def dfs(elems: List[int]):
            if not elems:
                res.append(prev[:])
                return
            for i in range(len(elems)):
                if i > 0 and elems[i] == elems[i-1]:
                    continue
                nxt = elems[:]
                nxt.pop(i)
                prev.append(elems[i])
                dfs(nxt)
                prev.pop()
        dfs(nums)
        return res
