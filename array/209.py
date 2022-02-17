class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        lt = 0; rt = 0; minlen = float('inf'); n = len(nums); cursum = nums[0]
        while True:
            while rt < n - 1 and cursum < target:
                rt += 1
                cursum += nums[rt]
            if cursum < target:
                break
            while lt <= rt and cursum >= target:
                cursum -= nums[lt]
                lt += 1
            minlen = min(minlen, rt-lt+2)
        if minlen == float('inf'):
            return 0
        else:
            return minlen
                
        
