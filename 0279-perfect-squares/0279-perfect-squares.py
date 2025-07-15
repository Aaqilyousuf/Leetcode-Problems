class Solution:
    def numSquares(self, n: int) -> int:
        ps = []
        i = 1
        while i*i <= n:
            ps.append(i*i)
            i += 1
        print(ps)
        dp = [float('inf')] * (n+1)
        dp[0] = 0
        for p in ps:
            for i in range(p, n+1):
                dp[i] = min(dp[i], dp[i-p] + 1)
        return dp[n] if dp[n] != float('inf') else -1