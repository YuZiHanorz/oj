class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        hashmap = {}
        res = []
        for i, x in enumerate(nums):
            hashmap[x] = i
        previ = prevj = float('inf')
        for i in range(len(nums) - 2):
            if nums[i] == previ:
                prevj = float('inf')
                continue
            previ = nums[i]
            for j in range(i+1, len(nums) - 1):
                if nums[j] == prevj:
                    continue
                prevj = nums[j]
                rest = 0 - nums[i] - nums[j]
                if rest < nums[j]:
                    break
                if rest in hashmap:
                    if hashmap[rest] > j:
                        res.append([nums[i], nums[j], rest])
        return res
