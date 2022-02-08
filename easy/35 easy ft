class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if nums[i] == target or (i == 0 and nums[i] > target):
                return i
            if i == len(nums) -1 or nums[i+1] == target or (nums[i] < target and nums[i+1] > target):
                return i+1
