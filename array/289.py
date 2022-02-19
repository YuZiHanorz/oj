class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        for i in range(m):
            for j in range(n):
                cnt = 0
                for h in range(max(0, i-1), min(i+2, m)):
                    for d in range(max(0, j-1), min(j+2, n)):
                        if h == i and d == j:
                            continue
                        if board[h][d] >= 1:
                            cnt += 1
                if board[i][j] == 0:
                    if cnt == 3:
                        board[i][j] = -1
                elif cnt < 2 or cnt > 3:
                    board[i][j] = 2
        for i in range(m):
            for j in range(n):
                if board[i][j] == -1:
                    board[i][j] = 1
                elif board[i][j] == 2:
                    board[i][j] = 0
