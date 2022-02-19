class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def bSearch(arr, target):
            i = 0
            j = len(arr)
            while i < j:
                mid = (i+j) // 2
                if arr[mid] == target:
                    return mid
                elif arr[mid] < target:
                    i = mid+1
                else:
                    j = mid
            return i
                
        if not nums:
            return 0
        rec = [nums[0]]
        for i in range(1, len(nums)):
            index = bSearch(rec, nums[i])
            if index == len(rec):
                rec.append(nums[i])
            else:
                rec[index] = nums[i]
            print(rec)
        return len(rec)
