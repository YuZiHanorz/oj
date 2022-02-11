class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        hashmap = {}
        for i in range(len(board)):
            hashmap.clear()
            for j in range(len(board)):
                n = board[i][j]
                if n != '.' and n in hashmap:
                    return False
                hashmap[n] = 1
        
            hashmap.clear()
            for j in range(len(board)):
                n = board[j][i]
                if n != '.' and n in hashmap:
                    return False
                hashmap[n] = 1
            
            hashmap.clear()
            for j in range(len(board)):
                n = board[i // 3 * 3 + j // 3][i % 3 * 3 + j % 3]
                if n != '.' and n in hashmap:
                    return False
                hashmap[n] = 1
        return True
