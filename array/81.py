class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        low = 0; high = len(nums) - 1
        while low < high - 1:
            mid = (low + high) // 2
            if target == nums[mid] or target == nums[low] or target == nums[high]:
                return True
            if nums[low] < nums[high]: # sorted
                if target < nums[low] or target > nums[high]:
                    return False
                if target > nums[mid]:
                    low = mid + 1
                else:
                    high = mid - 1
            else: # has a rot or all equal
                if target > nums[mid]:
                    
                    if target < nums[low]:
                        low = mid + 1
                    else: #target > low
                        if nums[mid] > nums[low]:
                            low = mid + 1
                        elif nums[mid] < nums[low]:
                            high = mid - 1
                        else: # target > low = mid
                            if nums[low] > nums[high]: #targer > low = mid > high
                                return False
                            else:
                                low += 1 # low = mid = high, ex. 4444234, 3, 4234444
                else: #target < mid
                    
                    if target > nums[low]:
                        high = mid - 1
                    else: #target < low
                        if nums[mid] > nums[low]:
                            low = mid + 1
                        elif nums[mid] < nums[low]:
                            high = mid - 1
                        else: # target < low = mid
                            if nums[low] > nums[high]:
                                low = mid + 1
                            else:
                                low += 1
        if nums[low] == target or nums[high] == target:
            return True
        return False
