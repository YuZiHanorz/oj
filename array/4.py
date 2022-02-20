class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1); n = len(nums2)
        half = (m + n) // 2
        med = (m + n) % 2
        low = 0; high = m - 1
        if m == 0:
            return nums2[n // 2] if med else (nums2[n//2] + nums2[n//2-1]) / 2
        if n == 0:
            return nums1[m // 2] if med else (nums1[m//2] + nums1[m//2-1]) / 2
        while low <= high:
            mid = (low + high) // 2 # nums1 [0-mid] m
            rest = half - (mid + 1) - 1 # nums2 [0-rest] n
            #print(mid, rest, nums1[mid], nums2[rest])
            if rest < -1:
                high = mid - 1
                continue
            elif rest >= n:
                low = mid + 1
                continue
            lt1 = nums1[mid] if mid >= 0 else float('-inf')
            lt2 = nums2[rest] if rest >= 0 else float('-inf')
            if (rest + 1 >= n or lt1 <= nums2[rest+1]) \
            and (mid + 1 >= m or lt2 <= nums1[mid+1]):
                lt = max(lt1, lt2)
                if mid + 1 >= m:
                    rt = nums2[rest+1]
                elif rest + 1 >= n:
                    rt = nums1[mid+1]
                else:
                    rt = min(nums1[mid+1], nums2[rest+1])
                return (lt + rt) / 2 if not med else rt
            elif rest + 1 < n and lt1 > nums2[rest+1]:
                high = mid - 1
            else:
                low = mid + 1
        rest = half - 1 # choose 0 elements from nums1
        if med:
            return min(nums1[0], nums2[rest+1]) if rest+1 < len(nums2) else nums1[0]
        else:
            rt = min(nums1[0], nums2[rest+1]) if rest+1 < len(nums2) else nums1[0]
            lt = nums2[rest]
            return (lt + rt) / 2
