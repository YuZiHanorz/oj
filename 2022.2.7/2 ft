class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        rec = []
        for i, n in enumerate(nums):
            if n not in rec:
                rec.append(n)
        for i in range(len(rec)):
            nums[i] = rec[i]
        return len(rec)
