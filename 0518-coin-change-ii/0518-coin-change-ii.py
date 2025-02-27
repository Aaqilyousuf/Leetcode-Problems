class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = {}
        def unboundedKnapsack(i, target):
            if target == 0:
                return 1
            if target<0 or i>=len(coins):
                return 0
            if (i, target) in memo:
                return memo[(i, target)]
            inc = unboundedKnapsack(i, target-coins[i])
            exc = unboundedKnapsack(i+1, target)
            memo[(i, target)] = inc + exc
            return memo[(i, target)]

        return unboundedKnapsack(0, amount)