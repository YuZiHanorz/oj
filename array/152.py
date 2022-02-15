class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        firstminus = -1
        minuscnt = 0
        maxpro = float('-inf')
        for i in range(len(nums)):
            if nums[i] == 0:
                maxpro = max(maxpro, 0)
                firstminus = -1
                minuscnt = 0
            else:
                cur = nums[i]
                if i > 0 and nums[i-1] != 0:
                    nums[i] = nums[i] * nums[i-1]
                if cur > 0:
                    if minuscnt % 2 == 0: # even 0
                        maxpro = max(maxpro, nums[i])
                    else: # odd 0
                        maxpro = max(maxpro, nums[i] // nums[firstminus])
                else: #cur < 0
                    if minuscnt % 2 == 0:
                        if minuscnt == 0:
                            maxpro = max(maxpro, nums[i])
                            firstminus = i
                        else:
                            maxpro = max(maxpro, nums[i] // nums[firstminus])
                    else:
                        maxpro = max(maxpro, nums[i])
                    minuscnt += 1
        return maxpro
                            
                            
