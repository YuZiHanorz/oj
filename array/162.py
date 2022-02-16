class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        if nums[0] > nums[1]:
            return 0
        if nums[-1] > nums[-2]:
            return len(nums)-1
        low = 0; high = len(nums)-1
        while low < high - 1:
            mid = (low + high) // 2
            if mid > 0 and nums[mid-1] < nums[mid]\
            and mid + 1 < len(nums) and nums[mid + 1] < nums[mid]:
                return mid
            if mid + 1 < len(nums) and nums[mid] < nums[mid+1]:
                low = mid + 1
            else:
                high = mid
        if nums[low] < nums[high]:
            return high
        else:
            return low
                
