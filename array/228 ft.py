class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        prev = nums[0]
        res = []
        for i in range(1, len(nums)):
            if nums[i] - nums[i-1] > 1:
                if prev == nums[i-1]:
                    res.append(str(prev))
                else:
                    res.append(str(prev) + '->' + str(nums[i-1]))
                prev = nums[i]
        if prev == nums[-1]:
            res.append(str(prev))
        else:
            res.append(str(prev) + '->' + str(nums[-1]))
        return res
                        
