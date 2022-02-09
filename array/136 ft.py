class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        map = {}
        for i in range(len(nums)):
            if nums[i] in map:
                map[nums[i]] = 2
            else:
                map[nums[i]] = 1
        for (k, v) in map.items():
            if v == 1:
                return k
