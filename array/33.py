class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0; high = len(nums) - 1
        while low < high - 1:
            mid = (low + high) // 2
            if target == nums[mid]:
                return mid
            '''if nums[low] < nums[high]: #sorted
                if target > nums[mid]:
                    low = mid + 1
                else: high = mid - 1
            else: #has a rotation'''
            if nums[mid] < nums[high]:
                if nums[mid] < target <= nums[high]:
                    low = mid + 1
                else: high = mid - 1
            else:
                if nums[low] <= target < nums[mid]:
                    high = mid - 1
                else: low = mid + 1
                

        if nums[low] == target:
            return low
        if nums[high] == target:
            return high
        else: return -1
