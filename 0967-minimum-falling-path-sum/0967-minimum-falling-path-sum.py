class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        row, col = len(matrix), len(matrix[0])
        memo = {}
        def backtrack(x, y):
            if y<0 or y>=col:
                return float('inf')
            if (x,y) in memo:
                return memo[(x,y)]
            if x==row-1:
                return matrix[x][y]
            minSum = matrix[x][y] + min(backtrack(x+1,y-1), backtrack(x+1,y), backtrack(x+1,y+1))
            memo[(x,y)] = minSum
            return minSum

        min_path_sum = float('inf')  
        for y in range(col):
            path_sum = backtrack(0, y)
            if path_sum < min_path_sum:
                min_path_sum = path_sum
        return min_path_sum
        # return min(backtrack(0, y) for y in range(col))
            