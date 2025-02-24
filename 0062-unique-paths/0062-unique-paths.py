class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = {}
        def backtrack(x, y):
            if x==m-1 and y==n-1:
                return 1
            if (x,y) in memo:
                return memo[(x,y)]
            if x>=m or y>=n:
                return 0
            count = 0
            count += (backtrack(x+1, y) + backtrack(x, y+1))
            memo[(x,y)] = count
            return memo[(x,y)]
        return backtrack(0,0)