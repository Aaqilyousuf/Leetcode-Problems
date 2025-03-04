class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if k>=len(prices)//2:
            profit = 0
            for i in range(1, len(prices)):
                if prices[i] > prices[i-1]:
                    profit += prices[i] - prices[i-1]
            return profit
        n = len(prices) 
        buy = [float('inf')] * (n+1)
        sell = [0] * (n+1)
        for price in prices:
            for j in range(1, k+1):
                buy[j] = min(buy[j], price-sell[j-1])
                sell[j] = max(sell[j], price-buy[j])
        return sell[k]