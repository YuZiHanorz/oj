class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = j = 0
        nums = []
        while i < m:
            if j >= n or nums1[i] <= nums2[j]:
                nums.append(nums1[i])
                i += 1
            else:
                nums.append(nums2[j])
                j += 1
            
            print (nums, i, j)
        for k in range(j, n):
            nums.append(nums2[k])
        print (nums)
        for k in range(m+n):
            nums1[k] = nums[k]
