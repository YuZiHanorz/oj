class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        mai = nums[0]
        ma = nums[0]
        for i in range(1, len(nums)):
            mai = max(nums[i], mai + nums[i])
            ma = max(mai, ma)
        return ma
