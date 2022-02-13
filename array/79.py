class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        visit = [[0 for _ in range(n)] for _ in range(m)]
        
        def dfs(row: int, col: int, word: str)-> bool:
            if not word:
                return True
            up = down = left = right = False
            if row > 0 and not visit[row-1][col] and board[row-1][col] == word[0]:
                visit[row-1][col] = 1
                up = dfs(row-1, col, word[1:])
                visit[row-1][col] = 0
            
            if row < m - 1 and not visit[row+1][col] and board[row+1][col] == word[0]:
                visit[row+1][col] = 1
                down = dfs(row+1, col, word[1:])
                visit[row+1][col] = 0
            
            if col > 0 and not visit[row][col-1] and board[row][col-1] == word[0]:
                visit[row][col-1] = 1
                left = dfs(row, col-1, word[1:])
                visit[row][col-1] = 0
            
            if col < n-1 and not visit[row][col+1] and board[row][col+1] == word[0]:
                visit[row][col+1] = 1
                right = dfs(row, col+1, word[1:])
                visit[row][col+1] = 0
            return up or down or left or right
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    visit[i][j] = 1
                    tmp = dfs(i, j, word[1:])
                    if tmp:
                        return True
                    visit[i][j] = 0
        return False
