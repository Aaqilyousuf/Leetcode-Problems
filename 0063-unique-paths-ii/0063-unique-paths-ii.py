class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        row, col = len(obstacleGrid), len(obstacleGrid[0])
        if obstacleGrid[0][0] == 1 or obstacleGrid[-1][-1]==1:
            return 0
        memo = {}
        def backtrack(x, y):
            if x==row-1 and y==col-1:
                return 1
            if (x,y) in memo:
                return memo[(x,y)]
            if x>=row or y>=col or obstacleGrid[x][y]==1:
                return 0
            count = 0
            count += (backtrack(x+1, y) + backtrack(x, y+1))
            memo[(x,y)] = count
            return memo[(x,y)]
        return backtrack(0, 0)
            
            