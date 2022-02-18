class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        def bs(sti, edi, stj, edj) -> bool:
            if sti > edi or stj > edj or matrix[sti][stj] > target or matrix[edi][edj] < target:
                return False
            if sti == edi:
                while stj < edj:
                    mid = (stj + edj) // 2
                    if matrix[sti][mid] == target:
                        return True
                    elif matrix[sti][mid] < target:
                        stj = mid + 1
                    else:
                        edj = mid - 1
                return matrix[sti][stj] == target
            elif stj == edj:
                while sti < edi:
                    mid = (sti + edi) // 2
                    if matrix[mid][stj] == target:
                        return True
                    elif matrix[mid][stj] < target:
                        sti = mid + 1
                    else:
                        edi = mid - 1
                return matrix[sti][stj] == target
            else:
                midi = (sti + edi) // 2
                midj = (stj + edj) // 2
                if bs(midi, midi, stj, edj) or bs(sti, edi, midj, midj):
                    return True
                return bs(sti, midi-1, stj, midj-1) or bs(sti, midi-1, midj+1, edj) or bs(midi+1, edi, stj, midj-1) or bs(midi+1, edi, midj+1, edj)
        return bs(0, m-1, 0, n-1)
                
            
