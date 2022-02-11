class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        haveNxt = False
        for i in range(len(nums)-1, -1, -1):
            if i < len(nums) - 1 and nums[i] < nums[i+1]:
                for j in range(i+1, len(nums)):
                    if nums[j] <= nums[i]:
                        nums[i], nums[j-1] = nums[j-1], nums[i]
                        break
                    if j == len(nums) - 1:
                        nums[i], nums[j] = nums[j], nums[i]
                tmp = nums[i+1:]
                tmp.sort()
                for j in range(len(tmp)):
                    nums[i+1+j] = tmp[j]
                haveNxt = True
                break
        if not haveNxt:
            nums.sort()
