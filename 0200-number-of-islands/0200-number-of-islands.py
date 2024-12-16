class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows = len(grid)
        cols = len(grid[0])
        island = 0

        def dfs(grid, r, c):
            n = len(grid)
            m = len(grid[0])
            if r<0 or c<0:
                return
            if r>=n or c>=m:
                return
            if grid[r][c]=="0":
                return
            grid[r][c] = "0"
            dfs(grid, r-1, c)
            dfs(grid, r+1, c)
            dfs(grid, r, c-1)
            dfs(grid, r, c+1)
   
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                     island += 1
                     dfs(grid, r,c)
                   
        return island