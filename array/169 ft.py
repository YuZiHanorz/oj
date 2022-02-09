class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        map = {}
        for i, n in enumerate(nums):
            if n in map:
                map[n] += 1
            else:
                map[n] = 1
            if (map[n] > len(nums)//2):
                return n
