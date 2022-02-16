class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        tmp = nums[0]
        idx = 0
        start = 0
        cnt = 0
        k = k % len(nums)
        while cnt < len(nums):
            while True:
                if idx >= k:
                    cur = idx - k
                else:
                    cur = len(nums) + idx - k
                if cur != start:
                    nums[idx] = nums[cur]
                else:
                    nums[idx] = tmp
                idx = cur
                cnt += 1
                if idx == start: 
                    break
            start += 1
            idx = start
            if start < len(nums):
                tmp = nums[start]
            
