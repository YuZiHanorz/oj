class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        idx = 0
        for i, n in enumerate(nums):
            if n != val:
                nums[idx] = n
                idx += 1
        return idx