class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        row, col = len(matrix), len(matrix[0])
        dp = [[0]*col for _ in range(row)]
        for i in range(col):
            dp[0][i] = matrix[0][i]
        for j in range(row):
            dp[j][0] = matrix[j][0]
        for i in range(1, row):
            for j in range(1, col):
                if matrix[i][j] == 1:
                    dp[i][j] = 1+min(dp[i-1][j],dp[i-1][j-1],dp[i][j-1])
                else:
                    dp[i][j] = 0
        count = 0
        for i in range(row):
            for j in range(col):
                count += dp[i][j]
        return count
