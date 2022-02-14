class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        s = set()
        s.add(nums[0])
        res = nums[0]
        for i in range(1, len(nums)):
            val = nums[i]
            if val in s:
                s.remove(val)
            else:
                s.add(val)
                res ^= val
        return res
