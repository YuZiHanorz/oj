class Solution:
    def rob(self, nums: List[int]) -> int:
        maxr = lastr = nums[0]
        maxn = lastn = 0
        for i in range(1, len(nums)):
            curr = lastn + nums[i]
            curn = max(lastr, lastn)
            maxr = max(maxr, curr)
            maxn = max(maxn, curn)
            lastr = curr
            lastn = curn
        return max(maxr, maxn)
