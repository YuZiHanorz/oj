class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]: continue
            for j in range(i+1, len(nums)):
                if j > i + 1 and nums[j] == nums[j-1]: continue
                lt = j + 1; rt = len(nums) - 1
                while lt < rt:
                    sum = nums[i] + nums[j] + nums[lt] + nums[rt]
                    if sum == target:
                        res.append([nums[i], nums[j], nums[lt], nums[rt]])
                        lt += 1
                        rt -= 1
                        while lt < rt and nums[lt] == nums[lt-1]:
                            lt += 1
                        while lt < rt and nums[rt] == nums[rt+1]:
                            rt -= 1
                    elif sum < target:
                        lt += 1
                    else:
                        rt -= 1
        return res
