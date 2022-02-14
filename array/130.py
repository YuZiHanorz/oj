class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        visited = [[0 for _ in range(n)] for _ in range(m)]
        
        def dfs(row: int, col: int, change: List[tuple]) -> bool:
            if row == 0 or row == m - 1 or col == 0 or col == n - 1:
                return False
            up = down = left = right = True
            if board[row-1][col] == 'O'and not visited[row-1][col]:
                visited[row-1][col] = 1
                up = dfs(row-1, col, change)
            
            if board[row+1][col] == 'O' and not visited[row+1][col]:
                visited[row+1][col] = 1
                down = dfs(row+1, col, change)
            
            if board[row][col-1] == 'O' and not visited[row][col-1]:
                visited[row][col-1] = 1
                left = dfs(row, col-1, change)
            
            if board[row][col+1] == 'O' and not visited[row][col+1]:
                visited[row][col+1] = 1
                right = dfs(row, col+1, change)
            
            print(row, col, up, down, right, left)
            if up and down and right and left:
                t = (row, col)
                change.append(t)
                return True
            else:
                change.clear()
                return False
        
        for i in range(1, m-1):
            for j in range(1, n-1):
                if board[i][j] == 'O' and not visited[i][j]:
                    visited[i][j] = 1
                    tmp = []
                    if dfs(i, j, tmp):
                        for v in tmp:
                            board[v[0]][v[1]] = 'X'
                    
