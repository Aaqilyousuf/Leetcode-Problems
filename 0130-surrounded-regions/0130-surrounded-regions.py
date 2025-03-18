class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        ROWS, COLS = len(board), len(board[0])
        def dfs(r, c):
            if r<0 or c<0 or r>=ROWS or c>=COLS or board[r][c] != 'O':
                return
            board[r][c] = '#' #making it as marked
            directions = [(1,0),(0,1),(-1,0), (0,-1)]
            for dr, dc in directions:
                dfs(r+dr, c+dc)
        
        #making first column and last column as marked
        for r in range(ROWS):
            if board[r][0] == 'O':
                dfs(r, 0)
            if board[r][COLS-1] == 'O':
                dfs(r, COLS-1)
        #making the first and last rows as marked
        for c in range(COLS):
            if board[0][c] == 'O':
                dfs(0, c)
            if board[ROWS-1][c] == 'O':
                dfs(ROWS-1, c)
        
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                if board[r][c] == '#':
                    board[r][c] = 'O'