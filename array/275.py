class Solution:
    def hIndex(self, citations: List[int]) -> int:
        low = 0; high = len(citations) - 1
        while low <= high:
            mid = (low + high) // 2
            print(low, mid, high)
            if citations[mid] == len(citations) - mid:
                return len(citations) - mid
            if citations[mid] < len(citations) - mid:
                low = mid + 1
            else:
                high = mid - 1
        return len(citations) - low
