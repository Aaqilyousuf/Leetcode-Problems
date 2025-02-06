class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        #GREEDY FAILS
        # if amount == 0:
        #     return 0
        # ans = 0
        # n = len(coins)
        # for i in range(n-1, -1, -1):
        #     while amount>=coins[i]:
        #         amount -= coins[i]
        #         ans += 1
        # return ans
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for coin in coins:
            for i in range(coin, amount+1):
                dp[i] = min(dp[i], dp[i-coin]+1)
        return dp[amount] if dp[amount] != float("inf") else -1