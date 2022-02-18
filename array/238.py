class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        before = [1 for _ in range(len(nums))]
        after = [1 for _ in range(len(nums))]
        for i in range(1, len(nums)):
            before[i] = before[i-1] * nums[i-1]
            after[-i-1] = after[-i] * nums[-i]
        for i in range(len(nums)):
            before[i] = before[i] * after[i]
        return before
