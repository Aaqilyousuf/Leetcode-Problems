class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        row, col = len(matrix), len(matrix[0])
        dp = [[0]*col for _ in range(row)]

        for j in range(col):#Each column
            dp[0][j] = matrix[0][j]

        for i in range(row):#Each row
            dp[i][0] = matrix[i][0]

        for i in range(1, row):#starting form (1,1)
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
