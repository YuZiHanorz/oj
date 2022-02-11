class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        low = 0; high = len(nums) - 1
        st = 0; ed = len(nums) - 1
        if not nums:
            return [-1, -1]
        #find ending
        while low < high - 1:
            mid = (low + high) // 2
            if nums[high] < target or nums[low] > target:
                return [-1, -1]
            if nums[mid] <= target:
                low = mid
            else: high = mid - 1
        if nums[high] == target:
            ed = high
        elif nums[low] == target:
            ed = low
        else: return [-1, -1]
        #find starting
        low = 0; high = ed
        while low < high - 1:
            mid = (low + high) // 2
            if nums[high] < target or nums[low] > target:
                return [-1, -1]
            if nums[mid] >= target:
                high = mid
            else: low = mid + 1
        if nums[low] == target:
            st = low
        elif nums[high] == target:
            st = high
        else: return [-1, -1]
        return [st, ed]
