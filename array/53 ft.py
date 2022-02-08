class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        mid = len(nums) // 2
        lt = nums[0 : mid]; rt = nums[mid : ]
        slt = self.maxSubArray(lt); srt = self.maxSubArray(rt)
        ln = lt[mid-1]; rn = rt[0]
        ma = ln
        for i in range(mid-2, -1, -1):
            ln += lt[i]
            if ma < ln:
                ma = ln
        ln = ma
        
        ma = rn
        for i in range(1, len(rt)):
            rn += rt[i]
            if ma < rn:
                ma = rn
        rn = ma
        s = rn + ln
        return max(s, slt, srt)
