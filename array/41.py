class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        i = 0
        N = len(nums)
        cnt = 0
        while i < N:
            while nums[i] != i+1:
                if nums[i] <= 0 or nums[i] > N:
                    break
                #print(i, nums[i], nums[nums[i] - 1], nums)
                tmp = nums[i] - 1
                if nums[i] == nums[tmp]:
                    break
                nums[i], nums[tmp] = nums[tmp], nums[i]
                #print(i, nums[i], nums[nums[i] - 1], nums)
            i += 1
        for i in range(N):
            if nums[i] != i + 1:
                return i + 1
        return N+1
