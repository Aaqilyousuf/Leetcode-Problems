class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        directions = [[1, 0], [0,1],[-1, 0], [0, -1]]
        def dfs(i, j):
            if i<0 or j<0 or i>=m or j>=n or grid[i][j] == 0:
                return 0
            curGold = grid[i][j]
            grid[i][j] = 0 #mark it as visited
            maxgold = 0
            for di, dj in directions:
                ni, nj = i+di, j+dj
                maxgold = max(maxgold, dfs(ni, nj))
            grid[i][j] = curGold #backtracking for other path

            return curGold + maxgold





        maxGold = 0
        for i in range(m):
            for j in range(n):
                maxGold = max(maxGold, dfs(i, j))
        return maxGold