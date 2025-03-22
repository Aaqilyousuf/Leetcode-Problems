class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        def dfs(r, c):
            if r<0 or c<0 or r>=ROWS or c>=COLS or grid[r][c] == 0:
                return
            grid[r][c] = 0
            directions = [[1,0],[0,1],[-1,0],[0,-1]]
            for dr, dc in directions:
                dfs(dr+r, dc+c)
          
  
        for r in range(ROWS):
            if grid[r][0] == 1:
                dfs(r, 0)
            if grid[r][COLS-1] == 1:
                dfs(r, COLS-1)
        for c in range(COLS):
            if grid[0][c] == 1:
                dfs(0, c)
            if grid[ROWS-1][c] == 1:
                dfs(ROWS-1, c)
        noEnclaves = 0
        for r in range(1, ROWS):
            for c in range(1, COLS):
                if grid[r][c] == 1:
                    noEnclaves += 1
        return noEnclaves      