class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxidx = 0; rt = 0
        for i in range(len(nums)):
            maxidx = max(maxidx, i + nums[i])
            if i == rt:
                if rt >= len(nums) - 1:
                    return True
                rt = maxidx
        return rt >= len(nums) - 1
