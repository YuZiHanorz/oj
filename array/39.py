class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        if not candidates: 
            return []
        candidates.sort()
        def cs(nums: List[int], t: int, last: int, ans: List[int]):
            if t == 0: 
                res.append(ans)
            if t < nums[0]: return
            for i in range(last, len(nums)):
                if nums[i] > target:
                    return
                tmp = ans + [nums[i]]
                cs(nums, t - nums[i], i, tmp)
        cs(candidates, target, 0, [])
        return res
            
