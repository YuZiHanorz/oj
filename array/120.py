class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        '''
        minsum = [0 for _ in range(len(triangle[-1]))]
        minsum[0] = triangle[0][0]
        for i in range(1, len(triangle)):
            tmp = minsum[:]
            tmp[0] = minsum[0] + triangle[i][0]
            tmp[len(triangle[i])-1] = minsum[len(triangle[i-1])-1]+triangle[i][-1]
            for j in range(1, len(triangle[i])-1):
                tmp[j] = min(minsum[j-1], minsum[j]) + triangle[i][j]
            minsum = tmp[:]
        return min(minsum)
        '''
        
        # bottom-up
        for i in range(len(triangle) - 2, -1, -1):
            for j in range(len(triangle[i])):
                triangle[i][j] += min(triangle[i+1][j], triangle[i+1][j+1])
        return triangle[0][0]
