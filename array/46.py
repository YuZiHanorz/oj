class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        '''
        res = []
        def dfs(nums: List[int], ans: List[int]):
            if not nums:
                res.append(ans)
                return
            for i in range(len(nums)):
                tans = ans + [nums[i]]
                tmp = nums[:i] + nums[i+1:]
                dfs(tmp, tans)
        
        dfs(nums, [])
        return res
        '''
        res = []
        prev = []
        def dfs(elems: List[int]):
            if not elems:
                res.append(prev[:])
                return
            for e in elems:
                nxt = elems[:]
                nxt.remove(e)
                prev.append(e)
                dfs(nxt)
                prev.pop()
        dfs(nums)
        return res
