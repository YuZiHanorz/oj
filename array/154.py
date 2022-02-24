class Solution:
    def findMin(self, nums: List[int]) -> int:
        low = 0; high = len(nums) - 1
        while low < high - 1:
            mid = (low + high) // 2
            if nums[low] < nums[high]:
                return nums[low]
            if nums[mid] > nums[low]:
                low = mid + 1
            elif nums[mid] < nums[low]:
                high = mid
            else: # mid = low >= high
                if nums[high] < nums[mid]:
                    low = mid + 1
                else:
                    low += 1
                    while low < high and nums[low] == nums[low - 1]:
                        low += 1
        return min(nums[low], nums[high])
