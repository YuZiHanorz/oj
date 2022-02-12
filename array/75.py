class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        lt = 0; rt = len(nums) - 1
        no = -1
        while lt <= rt:
            while lt <= rt and nums[lt] != 2:
                if nums[lt] == 0:
                    no += 1
                    if lt != no:
                        nums[lt], nums[no] = nums[no], nums[lt]
                lt += 1
            if lt > rt:
                break
            while lt <= rt and nums[rt] == 2:
                rt -= 1
            if lt > rt:
                break
            nums[rt], nums[lt] = nums[lt], nums[rt]
