class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        memo = {}
        def dfs(i, holding):
            if i >= n:
                return 0
            if (i, holding) in memo:
                return memo[(i, holding)]
            if holding:
                memo[(i, holding)] = max(dfs(i+1, 1), prices[i] + dfs(i+2, 0))
            else:
                memo[(i, holding)] = max(dfs(i+1, 0), dfs(i+1, 1) - prices[i])
            return memo[(i, holding)]
        return dfs(0, 0)
