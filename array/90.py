class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        
        def dfs(nums: List[int], ans: List[int]):
            if not nums:
                res.append(ans)
                return
            for i in range(len(nums)):
                if i > 0 and nums[i] == nums[i-1]:
                    continue
                tmp = ans[:]
                tmp.append(nums[i])
                dfs(nums[i+1:], tmp)
            res.append(ans)
        dfs(nums, [])
        return res
                
