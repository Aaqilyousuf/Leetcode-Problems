class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        row, col = len(matrix), len(matrix[0])
        # memo = {}
        # def dfs(i, j, memo):
        #     if i>=row or j>=col or i < 0 or j < 0:
        #         return 0
        #     if matrix[i][j] == "0":
        #         memo[(i, j)] = 0
        #         return 0
        #     if (i, j) in memo:
        #         return memo[(i,j)]
        #     up = dfs(i-1, j, memo)
        #     left = dfs(i, j-1, memo)
        #     topLeft = dfs(i-1, j-1, memo)
        #     memo[(i, j)] = 1 + min(up, left, topLeft)
        #     return memo[(i,j)]
        # maxArea = 0
        # for i in range(row):
        #     for j in range(col):
        #         maxArea = max(maxArea, dfs(i,j, memo))

        # return maxArea ** 2
        dp = [[0] * col for _ in range(row)]
        maxArea = 0
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == "0":
                    dp[i][j] = 0
                elif i==0 or j==0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
                maxArea = max(maxArea, dp[i][j])
        return maxArea ** 2