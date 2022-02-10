class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            lt = i + 1; rt = len(nums) - 1
            while lt < rt:
                sum = nums[i] + nums[lt] + nums[rt]
                if sum == 0:
                    res.append([nums[i], nums[lt], nums[rt]])
                    lt += 1; rt -=1
                    #only can be put here
                    while lt < rt and nums[lt] == nums[lt-1]:
                        lt += 1
                    while lt < rt and nums[rt+1] == nums[rt]:
                        rt -= 1
                elif sum < 0:
                    lt += 1
                else:
                    rt -= 1
                
        return res
