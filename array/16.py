class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest = float('inf')
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            lt = i + 1; rt = len(nums) - 1
            while lt < rt:
                sum = nums[i] + nums[lt] + nums[rt]
                if abs(sum - target) < abs(closest - target):
                    closest = sum
                if sum < target:
                    lt += 1
                else:
                    rt -= 1
        return closest
