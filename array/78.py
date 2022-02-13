class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        '''res = []
        def dfs(nums: List[int], ans: List[int]):
            if not nums:
                res.append(ans)
                return
            else:
                for i in range(len(nums) + 1):
                    tmp = ans[:]
                    if i < len(nums):
                        tmp.append(nums[i])
                    dfs(nums[i+1:], tmp)
                    
        dfs(nums, [])
        return res
        '''
        n = len(nums); res = [[]]
        mask = 2 ** n - 1 #bit manipulation
        while mask:
            subset = []
            tmp = mask
            i = n - 1
            while tmp:
                if tmp & 1:
                    subset.append(nums[i])
                tmp = tmp >> 1
                i -= 1
            mask -= 1
            res.append(subset)
        return res
        
        
