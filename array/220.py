class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        buckets = {}
        for i in range(len(nums)):
            if i-k > 0:
                del buckets[nums[i-k-1] // (t + 1)]
            idx = nums[i] // (t + 1)
            if idx in buckets:
                return True
            if idx-1 in buckets and abs(buckets[idx-1] - nums[i]) <= t:
                return True
            if idx+1 in buckets and abs(buckets[idx+1] - nums[i]) <= t:
                return True
            buckets[idx] = nums[i]
        return False
