class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        low = 0; high = len(matrix) - 1
        while low < high - 1:
            if target < matrix[low][0] or target > matrix[high][-1]:
                return False
            mid = (low + high) // 2
            if target == matrix[mid][0]:
                return True
            if target < matrix[mid][0]:
                high = mid - 1
            else: 
                low = mid
        if target >= matrix[high][0]:
            idx = high
        else: 
            idx = low
        
        num = matrix[idx]
        low = 0; high = len(matrix[0]) - 1
        while low < high - 1:
            if target < num[low] or target > num[high]:
                return False
            mid = (low + high) // 2
            if target == num[mid]:
                return True
            if target < num[mid]:
                high = mid - 1
            else:
                low = mid + 1
        return num[high] == target or num[low] == target
