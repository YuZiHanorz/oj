class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return 0
        if len(nums) == 2:
            return abs(nums[0] - nums[1])
        bucket = [[] for _ in range(10)]
        d = 0
        while True:
            over = True
            for i in range(len(nums)):
                idx = nums[i] // 10 ** d
                if idx != 0:
                    over = False
                bucket[idx % 10].append(nums[i])
            if over:
                break
            d += 1
            cnt = 0
            for i in range(10):
                while bucket[i]:
                    nums[cnt] = bucket[i].pop(0)
                    cnt += 1
            if cnt != len(nums):
                print ('here')
                break
        maxgap = 0
        print(nums)
        for i in range(len(nums)):
            if i > 0:
                maxgap = max(maxgap, nums[i] - nums[i-1])
        return maxgap
