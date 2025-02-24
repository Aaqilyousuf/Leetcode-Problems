class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        memo = {}
        def backtrack(x, y):
            if x>=row or y>=col:
                return float('inf')
            if x==row-1 and y==col-1:
                return grid[x][y]
            if (x,y) in memo:
                return memo[(x,y)]
            
            minSum = grid[x][y]+min(backtrack(x+1, y), backtrack(x, y+1))
            memo[(x,y)] = minSum
            return minSum
        res = backtrack(0,0)
        return res