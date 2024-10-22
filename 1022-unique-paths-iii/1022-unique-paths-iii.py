class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        zero, sx, sy = 0, 0, 0
        # Count zeros and find the starting point
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    sx, sy = row, col
                elif grid[row][col] == 0:
                    zero += 1

        def dfs(grid, sx, sy, zero):
            # Out of bounds or hits an obstacle
            if sx < 0 or sy < 0 or sx >= len(grid) or sy >= len(grid[0]) or grid[sx][sy] == -1:
                return 0
            
            # Reached the destination (2), and we must have walked over all 0s (i.e., zero == -1)
            if grid[sx][sy] == 2:
                return 1 if zero == -1 else 0
            
            # Mark the cell as visited
            grid[sx][sy] = -1
            zero -= 1
            
            # Explore all 4 directions
            totalPath = (dfs(grid, sx + 1, sy, zero) + 
                         dfs(grid, sx, sy + 1, zero) + 
                         dfs(grid, sx - 1, sy, zero) + 
                         dfs(grid, sx, sy - 1, zero))
            
            # Unmark the cell (backtracking)
            grid[sx][sy] = 0
            zero += 1

            return totalPath
        
        return dfs(grid, sx, sy, zero)
