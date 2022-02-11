class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        
        def dfs(nums: List[int], t: int, ans: List[int]):
            if t == 0:
                res.append(ans)
                return
            if not nums:
                return
            for i in range(len(nums)):
                if nums[i] > t:
                    return
                if i > 0 and nums[i] == nums[i-1]:
                    continue
                dfs(nums[i+1:], t-nums[i], ans + [nums[i]])
        
        if not candidates: return []
        candidates.sort()
        dfs(candidates, target, [])
        return res
