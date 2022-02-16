class Solution:
    def findMin(self, nums: List[int]) -> int:
        low = 0; high = len(nums) - 1
        while low < high - 1:
            mid = (low + high) // 2
            if nums[mid] < nums[low]:
                high = mid
            elif nums[mid] > nums[high]:
                low = mid + 1
            else:
                high = mid
        return min(nums[low], nums[high])
