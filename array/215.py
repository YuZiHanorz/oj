class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        import heapq as h #minheap
        q = []
        for i in range(len(nums)):
            h.heappush(q, nums[i])
            if len(q) > k:
                h.heappop(q)
        return h.heappop(q)
