class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m = len(dungeon)
        n = len(dungeon[0])
        minhealth = [[0 for _ in range(n)] for _ in range(m)] # minhealth reaching i,j
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if i == m - 1 and j == n - 1:
                    minhealth[i][j] = 1 - dungeon[i][j]
                elif i == m - 1:
                    minhealth[i][j] = minhealth[i][j+1] - dungeon[i][j]
                elif j == n - 1:
                    minhealth[i][j] = minhealth[i+1][j] - dungeon[i][j]
                else:
                    tmp = min(minhealth[i][j+1], minhealth[i+1][j])
                    minhealth[i][j] = tmp - dungeon[i][j]
                if minhealth[i][j] < 1:
                    minhealth[i][j] = 1
        return minhealth[0][0]
