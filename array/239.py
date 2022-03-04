class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = []
        res = []
        for i in range(len(nums)): # q[0] > ... > q[-1]
            while q and q[-1] < nums[i]:
                q.pop(-1)
            q.append(nums[i])
            if i >= k:
                if q[0] == nums[i-k]:
                    q.pop(0)
            if i >= k - 1:
                res.append(q[0])
        return res
