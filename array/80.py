class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        curNum = nums[0]; curTime = 1; idx = 1
        for i in range(1, len(nums)):
            if nums[i] == curNum:
                curTime += 1
            else:
                curTime = 1
                curNum = nums[i]
            if curTime <= 2:
                nums[idx] = nums[i]
                idx += 1
        return idx
